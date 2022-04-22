import networkx as nx
import matplotlib.pyplot as plt
import random
import sys
import json
import math
import pickle


COLORS = ['lightsteelblue', 'red', 'lime', 'yellow', 'orange', 'navajowhite', 'plum', 'cyan', 'brown']

def load_config(config_file_path):

    # sample config
    #{   'circuit': {   '1-qubit gate latency [ns]': '5',
    #                   '1-qubit gates': '70',
    #                   '2-qubit gate latency inside chain [ns]': '10',
    #                   '2-qubit gates': '30',
    #                   'circuit depth': '3',
    #                   'penalty for 2-qubit gate between chains': '2'}}
    
    with open (config_file_path) as config_file:
        config = json.load(config_file)
    
    #pp.pprint(config)
    
    d = int(config["circuit"]["circuit depth"])
    delta = float(config["circuit"]["1-qubit gate latency [ns]"])
    gamma = float(config["circuit"]["2-qubit gate latency inside chain [ns]"])
    alpha = float(config["circuit"]["penalty for 2-qubit gate between chains"])

    if d == 1:
        q = int(config["circuit"]["1-qubit gates"])
        p = int(config["circuit"]["2-qubit gates"])
    else:
        q = []
        p = []
        for layer in range(d):
            q.append(float(config["circuit"]["layer{}".format(layer+1)]["1-qubit gates"]))
            p.append(float(config["circuit"]["layer{}".format(layer+1)]["2-qubit gates"]))

    return d, q, p, alpha, delta, gamma


def sum_to_n(n, size, limit=None):
    """Produce all lists of `size` positive integers in decreasing order
    that add up to `n`."""
    if size == 1:
        yield [n]
        return
    if limit is None:
        limit = n
    start = (n + size - 1) // size
    stop = min(limit, n - size + 1) + 1
    for i in range(start, stop):
        for tail in sum_to_n(n - i, size - 1, i):
            yield [i] + tail


def gen_random_circuit():
    
    chain_size = 4
    print("Chain size: ", chain_size)
    num_qubits = random.randint(3, 16)
    print("Num qubits: ", num_qubits)
    num_2q_gates = random.randint(num_qubits, num_qubits + 5)
    print("Num 2-qubit gates: ", num_2q_gates)
    num_1q_gates = random.randint(0, num_qubits + 10)
    print("Num 1-qubit gates: ", num_1q_gates)
    qubit_list = list(range(num_qubits))
    print("Qubit list: ", qubit_list)
    delta = 1
    gamma = 100
    alpha = 2
    return chain_size, num_qubits, num_2q_gates, num_1q_gates, qubit_list, delta, gamma, alpha


def place_gates(num_1q_gates, num_2q_gates, qubit_list, G):

    remaining_2q_gates = num_2q_gates - len(qubit_list) # first randomly assign a 2q gate to each qubit

    operation_list = []

    for qubit in range(len(qubit_list)):
        q_id = random.sample(range(0, max(qubit_list)), 1)  # sample a distinct qubit
        q_id = q_id[0]
        
        while q_id == qubit:
            q_id = random.sample(range(0, max(qubit_list)), 1)  # sample a distinct qubit
            q_id = q_id[0]
        if (G.has_edge('q{}'.format(qubit), 'q{}'.format(q_id))): # edge already exists; update edge weight
            G['q{}'.format(qubit)]['q{}'.format(q_id)]['weight'] = G['q{}'.format(qubit)]['q{}'.format(q_id)]['weight'] + 1
        else: #no edge; add edge
            G.add_edge('q{}'.format(qubit), 'q{}'.format(q_id), weight=1)
         
        operation_list.append(['q{}'.format(qubit), 'q{}'.format(q_id)])
        

    for two_q_gate in range(remaining_2q_gates): # randomly assign the remaining qubits
        q_id = random.sample(range(0, max(qubit_list)), 2)  # sample 2 distinct qubits
        q1_id = q_id[0]
        q2_id = q_id[1]

        if (G.has_edge('q{}'.format(q1_id), 'q{}'.format(q2_id))): # edge already exists; update edge weight
            G['q{}'.format(q1_id)]['q{}'.format(q2_id)]['weight'] = G['q{}'.format(q1_id)]['q{}'.format(q2_id)]['weight'] + 1
        else: #no edge; add edge
            G.add_edge('q{}'.format(q1_id), 'q{}'.format(q2_id), weight=1)
        
        operation_list.append(['q{}'.format(q1_id), 'q{}'.format(q2_id)]) 

    for one_q_gate in range(num_1q_gates):
        q_id = random.sample(range(0, max(qubit_list)), 1)  # sample a distinct qubit
        q_id = q_id[0]
        operation_list.append(['q{}'.format(q_id)])
       

    return G, operation_list


def draw_graph(G, indices):

    color_map = []
    colorIndex = -1
    index = 0
    indices.insert(0, 0)
    indices.append(G.number_of_nodes())
    for i in range(len(indices) - 1):
        count = indices[i+1] - indices[i]
        for j in range(count):
            color_map.append(COLORS[i])

    # pos=nx.random_layout(G)
    pos=nx.circular_layout(G)
    nx.draw(G, pos, node_color=color_map, with_labels = True)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    plt.axis('off')
    plt.savefig('my_graph.png')


def get_indices(partitions):
    indices = []
    index = -1
    first = 1
    for partition_size in partitions:
        if first:
            indices.append(partition_size)
            index = partition_size
            first = 0
        else:
            indices.append(index + partition_size)
            index = index + partition_size

    indices.pop()
    print("Indices: ", indices)

    return indices


def prep_subgroups(subgroups):
    
    prepped_subgroups = []
    # Append 'q' to subgroups
    for group in subgroups:
        group = [str(qub) for qub in group]
        group = ["q" + qub for qub in group]
        prepped_subgroups.append(group)

    return prepped_subgroups


def compute_num_weak_links(num_chains, G, prepped_subgroups):

    cut_sizes = []
    first = 1
    for i in range(num_chains):
        if first == 1:
            first = 0
            continue
        else:
            cut_sizes.append(nx.cut_size(G,prepped_subgroups[i-1],prepped_subgroups[i]))

    return cut_sizes


def get_placement_possibilities(chain_size, qubit_list, num_chains, num_qubits, G):
    
    # get all ways to break up the graph into subgraphs 
    partition_list = list(sum_to_n(len(qubit_list)-1, num_chains))
    
    print("Partitions: ", partition_list)
    
    # choose one of those ways randomly
    idx = random.randint(0, len(partition_list)-1)

    while any(partition > chain_size for partition in partition_list[idx]):
        # choose one of those ways randomly
        idx = random.randint(0, len(partition_list)-1)
    
    # get the indices (no duplicates)
    indices = get_indices(partition_list[idx])
    
    subgroups = []
    
    if len(indices) != 0:
        first = 1
        for ind in indices:
           if first == 1: 
               subgroups.append(list(range(0, ind))) 
               old_ind = ind
               first = 0
           else:
               subgroups.append(list(range(old_ind, ind)))
               old_ind = ind
        
        subgroups.append(list(range(indices[len(indices)-1], num_qubits)))
    else:
        subgroups.append(list(range(0, num_qubits)))
    
    # prep subgroups (e.g., append q to qubit id's)
    prepped_subgroups = prep_subgroups(subgroups)
    
    print("Subgroups: ")
    print(prepped_subgroups)
       
    # compute number of weak links (cut sizes between chains)
    cut_sizes = compute_num_weak_links(num_chains, G, prepped_subgroups)

    return prepped_subgroups, cut_sizes, indices


def place_qubits_into_chains(G, num_qubits, chain_size, qubit_list):

    num_chains = math.ceil(float(num_qubits)/float(chain_size)) #BUG if num_qubits <= chain_size. Evaluates to 1 (we don't want that in the denominator later)
    
    print("Num chains: ", num_chains)
    print()
    
    random.shuffle(qubit_list)
    
    print("PLACEMENT ATTEMPT")
    prepped_subgroups, cut_sizes, indices = get_placement_possibilities(chain_size, qubit_list, num_chains, num_qubits, G)
    print("Cut sizes: ", cut_sizes)
    print()
    
    while not all(i <= 2 for i in cut_sizes):
        print("PLACEMENT ATTEMPT")
        prepped_subgroups, cut_sizes, indices = get_placement_possibilities(chain_size, qubit_list, num_chains, num_qubits, G)
        print("Cut sizes: ", cut_sizes)
        print()

    return prepped_subgroups, cut_sizes, indices


def main():
 
    if (sys.argv[1] == 'random'):# generate random circuit
        print("GENERATING RANDOM CIRCUIT")
        chain_size, num_qubits, num_2q_gates, num_1q_gates, qubit_list, delta, gamma, alpha = gen_random_circuit()
    else: # load circuit from config
        d, num_1q_gates, num_2q_gates, alpha, delta, gamma = load_config("./configs/3layer_test.json")
    
    G = nx.Graph()
    #G = pickle.load(open('./saved_graphs/graph.pkl'))
    
    # initialize qubits (add nodes)
    for qubit_num in qubit_list:
        G.add_node('q{}'.format(qubit_num))
    
    print("Nodes: ", G.nodes())
    
    # place gates (add edges)
    G, operation_list = place_gates(num_1q_gates, num_2q_gates, qubit_list, G)
    
    print("Edges: ", G.edges())

    #Place qubits into chains
    # number of sequences is equal to number of chains
    # break qubit list into X random groups where X is equal to number of chains
    prepped_subgroups, cut_sizes, indices = place_qubits_into_chains(G, num_qubits, chain_size, qubit_list)

    # draw graph for visualization purposes
    draw_graph(G, indices)

    pickle.dump(G, open('./saved_graphs/graph.pkl', 'wb'))

    print("RESULTS")
    print("Subgroups: ")
    print(prepped_subgroups)
    print("Cut sizes: ", cut_sizes)
    
    serial_t = delta*num_1q_gates # 1 qubit-gate latencies
    serial_t = serial_t + (num_2q_gates-sum(cut_sizes))*gamma + sum(cut_sizes)*gamma*alpha # 2-qubit gate latencies
    
    print("Serial performance [us]: ", serial_t)

    print("Operation list: ", operation_list)
    random.shuffle(operation_list) # randomize order of operations
    print("Operation list: ", operation_list)
    
    #parallel_t = new_algorithm(operation_list)
    #print("Parallel performance [us]: ", parallel_t)


if __name__ == "__main__":
    main()

