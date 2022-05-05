import networkx as nx
import logging
import matplotlib.pyplot as plt
import random
import sys
import json
import math
import pickle
import circuit


COLORS = ['lightsteelblue', 'red', 'lime', 'yellow', 'orange', 'navajowhite', 'plum', 'cyan', 'brown']


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


def draw_graph(G, indices, filename):

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
    plt.savefig(filename)


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
    logging.info("Indices: %s", indices)

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
    
    logging.info("Partitions: %s", partition_list)
    
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
    
    logging.info("Subgroups: %s", prepped_subgroups)
       
    # compute number of weak links (cut sizes between chains)
    cut_sizes = compute_num_weak_links(num_chains, G, prepped_subgroups)

    return prepped_subgroups, cut_sizes, indices


def place_qubits_into_chains(G, num_qubits, chain_size, qubit_list, valid):

    num_chains = math.ceil(float(num_qubits)/float(chain_size)) #BUG if num_qubits <= chain_size. Evaluates to 1 (we don't want that in the denominator later)
    
    attempts = 0
    
    logging.info("Num chains: %d", num_chains)
    
    random.shuffle(qubit_list)
    
    logging.info("PLACEMENT ATTEMPT")
    prepped_subgroups, cut_sizes, indices = get_placement_possibilities(chain_size, qubit_list, num_chains, num_qubits, G)
    logging.info("Cut sizes: %s", cut_sizes)
    
    while (not all(i <= 2 for i in cut_sizes)) and attempts < 100:
        logging.info("PLACEMENT ATTEMPT")
        prepped_subgroups, cut_sizes, indices = get_placement_possibilities(chain_size, qubit_list, num_chains, num_qubits, G)
        logging.info("Cut sizes: %s", cut_sizes)
        attempts = attempts + 1

    if attempts == 100:
        valid = False
        print("Valid: ", valid)
    
    return prepped_subgroups, cut_sizes, indices, valid


def update_edge_weight(DG, is_2q_gate, qubit_placement_dict, q1, q2, previous_operation, previous_node_id, current_node_id, start_nodes):

    if is_2q_gate:
        if qubit_placement_dict[q1] != qubit_placement_dict[q2]:
            if previous_node_id in start_nodes:
                # add latency of start node operation
                if len(previous_operation) >= 2 and "q" in str(previous_operation[1]): #2q gate
                    if qubit_placement_dict[previous_operation[0]] != qubit_placement_dict[previous_operation[1]]:
                        DG.add_edge(previous_node_id, current_node_id, weight=400)
                    else:
                        DG.add_edge(previous_node_id, current_node_id, weight=300)
                else: # 1q gate
                    DG.add_edge(previous_node_id, current_node_id, weight=201)
            else:
                DG.add_edge(previous_node_id, current_node_id, weight=200)
        else:
            if previous_node_id in start_nodes:
                # add latency of start node operation
                if len(previous_operation) >= 2 and "q" in str(previous_operation[1]): #2q gate
                    if qubit_placement_dict[previous_operation[0]] != qubit_placement_dict[previous_operation[1]]:
                        DG.add_edge(previous_node_id, current_node_id, weight=300)
                    else:
                        DG.add_edge(previous_node_id, current_node_id, weight=200)
                else: # 1q gate
                    DG.add_edge(previous_node_id, current_node_id, weight=101)
            else:
                DG.add_edge(previous_node_id, current_node_id, weight=100)
    else:
        DG.add_edge(previous_node_id, current_node_id, weight=1)

    return DG



def build_operation_graph(operation_list, qubit_placement_dict):
    
    operation_dict = {}

    DG = nx.DiGraph()

    is_2q_gate = False
    start_nodes = []
   
    for index, operation in enumerate(operation_list):
        logging.info("OPERATION %d", index)
        logging.info("Operation dict: %s", operation_dict)

        # check if 1q or 2q gate and separate qubit IDs
        if len(operation) == 2:
            is_2q_gate = True
            q1 = operation[0]
            q2 = operation[1]
            current_operation = "{}{}".format(q1, q2)
            current_operation_swapped = "{}{}".format(q2, q1)
        else:
            is_2q_gate = False
            q1 = operation[0]
            current_operation = "{}".format(q1)

        logging.info("Current_operation: %s", current_operation)
        ## make node
        # check if node exists 
        if is_2q_gate:
            if current_operation in operation_dict:
               # node already exists, make a new node with counter appended, e.g., q1q2_2
               num_previous_occurences = operation_dict[current_operation]
               current_node_id = "{}_{}".format(current_operation, num_previous_occurences+1)
               DG.add_node(current_node_id)
               operation_dict[current_operation] = operation_dict[current_operation] + 1
               operation_list[index].append(operation_dict[current_operation])
            
            elif current_operation_swapped in operation_dict:
               operation_list[index] = [q2, q1] 
               current_operation = current_operation_swapped
               # node already exists, make a new node with counter appended, e.g., q1q2_2
               num_previous_occurences = operation_dict[current_operation]
               current_node_id = "{}_{}".format(current_operation, num_previous_occurences+1)
               DG.add_node(current_node_id)
               operation_dict[current_operation] = operation_dict[current_operation] + 1
               operation_list[index].append(operation_dict[current_operation])

            else: # node doesn't exist, make new one
               current_node_id = current_operation 
               DG.add_node(current_node_id)
               operation_dict[current_operation] = 1

        else:
            if current_operation in operation_dict:
               # node already exists, make a new node with counter appended, e.g., q1q2_2
               num_previous_occurences = operation_dict[current_operation]
               current_node_id = "{}_{}".format(current_operation, num_previous_occurences+1)
               DG.add_node(current_node_id)
               operation_dict[current_operation] = operation_dict[current_operation] + 1
               operation_list[index].append(operation_dict[current_operation])

            else: # node doesn't exist, make new one
               current_node_id = current_operation 
               DG.add_node(current_node_id)
               operation_dict[current_operation] = 1
           
        logging.info("Current_node_id: %s", current_node_id)
        logging.info("Operation list: %s", operation_list)

        ## check if edge should be added
        previous_node_id = ""
        first_operand_linked = False
        second_operand_linked = False

        for history_index in reversed(range(index)):
            logging.info("GOING THROUGH HISTORY")
            logging.info("history_index: %d", history_index)
            previous_operation = operation_list[history_index] # either ["q1", "q2"] or ["q3"] for example
            logging.info("Previous_operation: %s", previous_operation)
            
            ## check for operand matching
            # current gate is 2q gate
            if is_2q_gate:
                
                # previous operation under scrutiny is 2q gate
                if len(previous_operation) >= 2 and "q" in str(previous_operation[1]):
                   
                    if not first_operand_linked and not second_operand_linked:
                        if (q1 == previous_operation[0] or q1 == previous_operation[1]) and (q2 == previous_operation[0] or q2 == previous_operation[1]):

                            first_operand_linked = True
                            second_operand_linked = True

                            # obtain node id for previous operation and exit loop
                            if len(previous_operation) == 3:
                                num_previous_occurences_of_previous_operation = previous_operation[2]
                                previous_node_id = "{}{}_{}".format(previous_operation[0], previous_operation[1], num_previous_occurences_of_previous_operation)
                            else:
                                previous_node_id = "{}{}".format(previous_operation[0], previous_operation[1])
                            
                            logging.info("Previous_node_id: %s", previous_node_id)
                            DG = update_edge_weight(DG, is_2q_gate, qubit_placement_dict, q1, q2, previous_operation, previous_node_id, current_node_id, start_nodes)

                    
                    if not first_operand_linked:
                        if q1 == previous_operation[0] or q1 == previous_operation[1]:

                            first_operand_linked = True

                            # obtain node id for previous operation and exit loop
                            if len(previous_operation) == 3:
                                num_previous_occurences_of_previous_operation = previous_operation[2]
                                previous_node_id = "{}{}_{}".format(previous_operation[0], previous_operation[1], num_previous_occurences_of_previous_operation)
                            else:
                                previous_node_id = "{}{}".format(previous_operation[0], previous_operation[1])
                            
                            
                            logging.info("Previous_node_id: %s", previous_node_id)
                            DG = update_edge_weight(DG, is_2q_gate, qubit_placement_dict, q1, q2, previous_operation, previous_node_id, current_node_id, start_nodes)

                    if not second_operand_linked:
                        if q2 == previous_operation[0] or q2 == previous_operation[1]:

                            second_operand_linked = True

                            # obtain node id for previous operation and exit loop
                            if len(previous_operation) == 3:
                                num_previous_occurences_of_previous_operation = previous_operation[2]
                                previous_node_id = "{}{}_{}".format(previous_operation[0], previous_operation[1], num_previous_occurences_of_previous_operation)
                            else:
                                previous_node_id = "{}{}".format(previous_operation[0], previous_operation[1])
                            
                            
                            logging.info("Previous_node_id: %s", previous_node_id)
                            DG = update_edge_weight(DG, is_2q_gate, qubit_placement_dict, q1, q2, previous_operation, previous_node_id, current_node_id, start_nodes)
                
                # previous operation under scrutiny is 1q gate
                else: 

                    if not first_operand_linked:
                        if q1 == previous_operation[0]:

                            first_operand_linked = True

                            # obtain node id for previous operation and exit loop
                            if len(previous_operation) == 2:
                                num_previous_occurences_of_previous_operation = previous_operation[1]
                                previous_node_id = "{}_{}".format(previous_operation[0], num_previous_occurences_of_previous_operation)
                            else:
                                previous_node_id = "{}".format(previous_operation[0])
                
                            
                            logging.info("Previous_node_id: %s", previous_node_id)
                            DG = update_edge_weight(DG, is_2q_gate, qubit_placement_dict, q1, q2, previous_operation, previous_node_id, current_node_id, start_nodes)
                    
                    if not second_operand_linked:
                        if q2 == previous_operation[0]:

                            second_operand_linked = True

                            # obtain node id for previous operation and exit loop
                            if len(previous_operation) == 2:
                                num_previous_occurences_of_previous_operation = previous_operation[1]
                                previous_node_id = "{}_{}".format(previous_operation[0], num_previous_occurences_of_previous_operation)
                            else:
                                previous_node_id = "{}".format(previous_operation[0])
                
                            
                            logging.info("Previous_node_id: %s", previous_node_id)
                            DG = update_edge_weight(DG, is_2q_gate, qubit_placement_dict, q1, q2, previous_operation, previous_node_id, current_node_id, start_nodes)

            # current gate is 1q gate
            else: 
                
                # previous operation under scrutiny is 2q gate
                if len(previous_operation) >= 2 and "q" in str(previous_operation[1]):

                    if not first_operand_linked:
                        if q1 == previous_operation[0] or q1 == previous_operation[1]:

                            first_operand_linked = True

                            # obtain node id for previous operation and exit loop
                            if len(previous_operation) == 3:
                                num_previous_occurences_of_previous_operation = previous_operation[2]
                                previous_node_id = "{}{}_{}".format(previous_operation[0], previous_operation[1], num_previous_occurences_of_previous_operation)
                            else:
                                previous_node_id = "{}{}".format(previous_operation[0], previous_operation[1])
                            
                            
                            logging.info("Previous_node_id: %s", previous_node_id)
                            DG = update_edge_weight(DG, is_2q_gate, qubit_placement_dict, q1, q2, previous_operation, previous_node_id, current_node_id, start_nodes)

                # previous operation under scrutiny is 1q gate
                else: 
                    if not first_operand_linked:
                        if q1 == previous_operation[0]:

                            first_operand_linked = True

                            # obtain node id for previous operation and exit loop
                            if len(previous_operation) == 2:
                                num_previous_occurences_of_previous_operation = previous_operation[1]
                                previous_node_id = "{}_{}".format(previous_operation[0], num_previous_occurences_of_previous_operation)
                            else:
                                previous_node_id = "{}".format(previous_operation[0])
                            
                            
                            logging.info("Previous_node_id: %s", previous_node_id)
                            DG = update_edge_weight(DG, is_2q_gate, qubit_placement_dict, q1, q2, previous_operation, previous_node_id, current_node_id, start_nodes)

            ## exit loop if all operand(s) have been linked to previous nodes
            if is_2q_gate:
                if first_operand_linked and second_operand_linked:
                    break

            else:
                if first_operand_linked:
                    break

        # It's a start node
        if previous_node_id == "":
            start_nodes.append(current_node_id)

    return DG


def generate_serial_architecture(qubit_list, num_1q_gates, num_2q_gates, num_qubits, chain_size):
    
    valid = True
    
    G = nx.Graph()
    #G = pickle.load(open('./saved_graphs/graph.pkl'))
    
    # initialize qubits (add nodes)
    for qubit_num in qubit_list:
        G.add_node('q{}'.format(qubit_num))
    
    logging.info("Nodes: %s", G.nodes())
    
    # place gates (add edges)
    G, operation_list = place_gates(num_1q_gates, num_2q_gates, qubit_list, G)
    
    logging.info("Edges: %s", G.edges())

    #Place qubits into chains
    # number of sequences is equal to number of chains
    # break qubit list into X random groups where X is equal to number of chains
    prepped_subgroups, cut_sizes, indices, valid = place_qubits_into_chains(G, num_qubits, chain_size, qubit_list, valid)
    print("Valid: ", valid)

    while not valid:

        print("Valid: ", valid)
        
        print("Trying new random circuit...")
        chain_size, num_qubits, num_2q_gates, num_1q_gates, qubit_list, delta, gamma, alpha = circuit.gen_random_circuit()
    
        valid = True

        G = nx.Graph()
        #G = pickle.load(open('./saved_graphs/graph.pkl'))
        
        # initialize qubits (add nodes)
        for qubit_num in qubit_list:
            G.add_node('q{}'.format(qubit_num))
        
        logging.info("Nodes: %s", G.nodes())
        
        # place gates (add edges)
        G, operation_list = place_gates(num_1q_gates, num_2q_gates, qubit_list, G)
        
        logging.info("Edges: %s", G.edges())

        #Place qubits into chains
        # number of sequences is equal to number of chains
        # break qubit list into X random groups where X is equal to number of chains
        prepped_subgroups, cut_sizes, indices, valid = place_qubits_into_chains(G, num_qubits, chain_size, qubit_list, valid)
        print("Valid: ", valid)
        
        logging.info("Trying new random circuit...")


    qubit_placement_dict = {}
    
    for index, subgroup in enumerate(prepped_subgroups):
        for qubit in subgroup:
            qubit_placement_dict[qubit] = index

    # draw graph for visualization purposes
    draw_graph(G, indices, "qubit_graph.png")

    pickle.dump(G, open('./saved_graphs/graph.pkl', 'wb'))

    random.shuffle(operation_list) # randomize order of operations
    logging.info("Operation list: %s", operation_list)

    return cut_sizes, indices, qubit_placement_dict, operation_list


def compute_serial_t(delta, num_1q_gates, num_2q_gates, cut_sizes, gamma, alpha):

    serial_t = delta*num_1q_gates # 1 qubit-gate latencies
    serial_t = serial_t + (num_2q_gates-sum(cut_sizes))*gamma + sum(cut_sizes)*gamma*alpha # 2-qubit gate latencies
    
    logging.info("Serial performance [us]: %f", serial_t)
    print("Serial performance [us]: ", serial_t)
    return serial_t


def generate_parallel_architecture(operation_list, qubit_placement_dict):

    DG = build_operation_graph(operation_list, qubit_placement_dict)
    subax1 = plt.subplot(111)
    nx.draw(DG, nx.circular_layout(DG), with_labels=True, font_weight='bold')
    return DG


def compute_parallel_t(DG):

    parallel_t = nx.dag_longest_path_length(DG)
    logging.info("Longest path: %s", nx.dag_longest_path(DG))
    logging.info("Parallel performance [us]: %f", parallel_t)
    print("Parallel performance [us]: ", parallel_t)
    plt.savefig("operation_graph.png")

    return parallel_t
