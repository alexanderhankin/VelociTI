import networkx as nx
import matplotlib.pyplot as plt
import random
import sys
import json
import math


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
    
    chain_size = 8 
    print("Chain size: ", chain_size)
    num_qubits = random.randint(5,50)
    print("Num qubits: ", num_qubits)
    num_2q_gates = random.randint(0, num_qubits)
    #num_1q_gates = random.randint(0, num_qubits)
    num_1q_gates = 0
    qubit_list = list(range(num_qubits))
    print("Qubit list: ", qubit_list)
    delta = 1
    gamma = 100
    alpha = 2
    return chain_size, num_qubits, num_2q_gates, num_1q_gates, qubit_list, delta, gamma, alpha


def place_gates(num_2q_gates, qubit_list, G):

    for gate in range(num_2q_gates):
        q1_id = random.randint(0,max(qubit_list))
        q2_id = random.randint(0,max(qubit_list))
        
        while (q1_id == q2_id):
            q1_id = random.randint(0,max(qubit_list))
            q2_id = random.randint(0,max(qubit_list))
        
        if (G.has_edge('q{}'.format(q1_id), 'q{}'.format(q2_id))): # edge already exists; update edge weight
            G['q{}'.format(q1_id)]['q{}'.format(q2_id)]['weight'] = G['q{}'.format(q1_id)]['q{}'.format(q2_id)]['weight'] + 1
        else: #no edge; add edge
            G.add_edge('q{}'.format(q1_id), 'q{}'.format(q2_id), weight=1)
    return G


def draw_graph(G):

    pos=nx.random_layout(G)
    nx.draw(G, pos, with_labels = True)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    plt.axis('off')
    plt.savefig('my_graph.png')


def get_indices(idx, partitions):

    # get the indices
    indices = partitions[idx]
    indices.sort()
    indices_set = set(indices)
    
    # check if duplicates and regen until there aren't
    while (len(indices) != len(indices_set)):
        # choose one of those ways randomly
        idx = random.randint(0, len(partitions)-1)
        indices = partitions[idx]
        indices.sort()
        indices_set = set(indices)

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


def get_placement_possibilities(qubit_list, num_chains, num_qubits, G):
    
    # get all ways to break up the graph into subgraphs 
    partitions = list(sum_to_n(len(qubit_list)-1, num_chains-1))
    
    # choose one of those ways randomly
    idx = random.randint(0, len(partitions)-1)
    
    # get the indices (no duplicates)
    indices = get_indices(idx, partitions)
    
    print("Indices: ")
    print(indices)
    
    subgroups = []
    
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
    
    print("Subgroups: ")
    print(subgroups)

    # prep subgroups (e.g., append q to qubit id's)
    prepped_subgroups = prep_subgroups(subgroups)
    
    print("Prepped subgroups: ")
    print(prepped_subgroups)
    print()
       
    # compute number of weak links (cut sizes between chains)
    cut_sizes = compute_num_weak_links(num_chains, G, prepped_subgroups)

    return cut_sizes


def place_qubits_into_chains(G, num_qubits, chain_size, qubit_list):

    num_chains = math.ceil(float(num_qubits)/float(chain_size))
    
    print("Num chains: ", num_chains)
    print()
    
    random.shuffle(qubit_list)
    
    print("PLACEMENT ATTEMPT")
    cut_sizes = get_placement_possibilities(qubit_list, num_chains, num_qubits, G)
    
    while not all(i <= 2 for i in cut_sizes):
        print("PLACEMENT ATTEMPT")
        cut_sizes = get_placement_possibilities(qubit_list, num_chains, num_qubits, G)

    return cut_sizes


def main():
 
    if (sys.argv[1] == 'random'):# generate random circuit
        print("GENERATING RANDOM CIRCUIT")
        chain_size, num_qubits, num_2q_gates, num_1q_gates, qubit_list, delta, gamma, alpha = gen_random_circuit()
    else: # load circuit from config
        d, q, p, alpha, delta, gamma = load_config("./configs/3layer_test.json")
    
    G = nx.Graph()
    
    # initialize qubits (add nodes)
    for qubit_num in qubit_list:
        G.add_node('q{}'.format(qubit_num))
    
    print("Nodes: ", G.nodes())
    
    # place gates (add edges)
    G = place_gates(num_2q_gates, qubit_list, G)
    
    print("Edges: ", G.edges())
    
    # draw graph for visualization purposes
    draw_graph(G)
    
    #Place qubits into chains
    # number of sequences is equal to number of chains
    # break qubit list into X random groups where X is equal to number of chains
    cut_sizes = place_qubits_into_chains(G, num_qubits, chain_size, qubit_list) 

    print("RESULTS")
    print("Cut sizes: ", cut_sizes)
    
    t = delta*num_1q_gates # 1 qubit-gate latencies
    t = t + (num_2q_gates-sum(cut_sizes))*gamma + sum(cut_sizes)*gamma*alpha # 2-qubit gate latencies
    
    print("Total time [us]: ", t)


if __name__ == "__main__":
    main()

