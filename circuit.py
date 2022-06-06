import networkx as nx
import logging
import json
import random
from datetime import date
import graphviz

def load_config_simple(config_file_path):

    with open (config_file_path) as config_file:
        config = json.load(config_file)
    
    delta = float(config["circuit"]["1-qubit gate latency [ns]"])/1000
    gamma = float(config["circuit"]["2-qubit gate latency inside chain [ns]"])/1000
    alpha = float(config["circuit"]["penalty for 2-qubit gate between chains"])
    qubits_per_chain = int(config["circuit"]["qubits per chain"])
    num_qubits = int(config["circuit"]["num qubits"])
    num_chains = int(config["circuit"]["num chains"])
    q = int(config["circuit"]["num 1q gates"])
    p = int(config["circuit"]["num 2q gates"])
    qubit_placement = config["circuit"]["qubit placement dict"]
    operation_list = config["circuit"]["operation list"]

    logging.info("Chain size: %s", qubits_per_chain)
    logging.info("Num qubits: %d", num_qubits)
    logging.info("Num 2-qubit gates: %d", p)
    logging.info("Num 1-qubit gates: %d", q)
    print("Chain size: ", qubits_per_chain)
    print("Num qubits: ", num_qubits)
    print("Num 2-qubit gates: ", p)
    print("Num 1-qubit gates: ", q)

    return q, p, alpha, delta, gamma, qubits_per_chain, num_qubits, num_chains, qubit_placement, operation_list


def load_config(config_file_path):

    with open (config_file_path) as config_file:
        config = json.load(config_file)
    
    delta = float(config["circuit"]["1-qubit gate latency [ns]"])/1000
    gamma = float(config["circuit"]["2-qubit gate latency inside chain [ns]"])/1000
    alpha = float(config["circuit"]["penalty for 2-qubit gate between chains"])
    qubits_per_chain = int(config["circuit"]["qubits per chain"])
    num_qubits = int(config["circuit"]["num qubits"])
    num_chains = int(config["circuit"]["num chains"])
    q = int(config["circuit"]["num 1q gates"])
    p = int(config["circuit"]["num 2q gates"])
    qubit_placement = config["circuit"]["qubit placement dict"]
    cut_sizes = config["circuit"]["cut sizes"]
    indices = config["circuit"]["indices"]
    operation_list = config["circuit"]["operation list"]

    logging.info("Chain size: %s", qubits_per_chain)
    logging.info("Num qubits: %d", num_qubits)
    logging.info("Num 2-qubit gates: %d", p)
    logging.info("Num 1-qubit gates: %d", q)
    print("Chain size: ", qubits_per_chain)
    print("Num qubits: ", num_qubits)
    print("Num 2-qubit gates: ", p)
    print("Num 1-qubit gates: ", q)

    return q, p, alpha, delta, gamma, qubits_per_chain, num_qubits, num_chains, qubit_placement, cut_sizes, indices, operation_list


def gen_random_circuit(chain_size=4,
                       num_qubits_min=3, num_qubits_max=16,
                       num_1q_gates=15, num_2q_gates=10,
                       latency_1q=1, latency_2q=100, weaklink_scale_factor=2,
                       verbose=True):

    num_qubits = random.randint(num_qubits_min, num_qubits_max)
    num_1q_gates = random.randint(0, num_qubits + num_1q_gates)
    num_2q_gates = random.randint(num_qubits, num_qubits + num_2q_gates)
    delta = latency_1q
    gamma = latency_2q
    alpha = weaklink_scale_factor
    qubit_list = list(range(num_qubits))

    logging.info("Chain size: %s", chain_size)
    logging.info("Num qubits: %d", num_qubits)
    logging.info("Num 2-qubit gates: %d", num_2q_gates)
    logging.info("Num 1-qubit gates: %d", num_1q_gates)
    logging.info("Qubit list: %s", qubit_list)

    if verbose:
        print("Chain size: ", chain_size)
        print("Num qubits: ", num_qubits)
        print("Num 2-qubit gates: ", num_2q_gates)
        print("Num 1-qubit gates: ", num_1q_gates)

    return chain_size, num_qubits, num_2q_gates, num_1q_gates, qubit_list, delta, gamma, alpha


def place_gates(num_1q_gates, num_2q_gates, qubit_list):
    G = nx.Graph()

    # initialize qubits (add nodes)
    for qubit_num in qubit_list:
        G.add_node('q{}'.format(qubit_num))
    logging.info("Nodes: %s", G.nodes())

    remaining_2q_gates = num_2q_gates - len(qubit_list)  # first randomly assign a 2q gate to each qubit

    operation_list = []

    for qubit in range(len(qubit_list)):
        q_id = random.sample(range(0, max(qubit_list)), 1)[0]  # sample a distinct qubit

        while q_id == qubit:
            q_id = random.sample(range(0, max(qubit_list)), 1)[0]  # sample a distinct qubit
        if (G.has_edge('q{}'.format(qubit), 'q{}'.format(q_id))):  # edge already exists; update edge weight
            G['q{}'.format(qubit)]['q{}'.format(q_id)]['weight'] = G['q{}'.format(qubit)]['q{}'.format(q_id)][
                                                                       'weight'] + 1
        else:  # no edge; add edge
            G.add_edge('q{}'.format(qubit), 'q{}'.format(q_id), weight=1)

        operation_list.append(['q{}'.format(qubit), 'q{}'.format(q_id)])

    for two_q_gate in range(remaining_2q_gates):  # randomly assign the remaining qubits
        q_id = random.sample(range(0, max(qubit_list)), 2)  # sample 2 distinct qubits
        q1_id = q_id[0]
        q2_id = q_id[1]

        if (G.has_edge('q{}'.format(q1_id), 'q{}'.format(q2_id))):  # edge already exists; update edge weight
            G['q{}'.format(q1_id)]['q{}'.format(q2_id)]['weight'] = G['q{}'.format(q1_id)]['q{}'.format(q2_id)][
                                                                        'weight'] + 1
        else:  # no edge; add edge
            G.add_edge('q{}'.format(q1_id), 'q{}'.format(q2_id), weight=1)

        operation_list.append(['q{}'.format(q1_id), 'q{}'.format(q2_id)])

    for one_q_gate in range(num_1q_gates):
        q_id = random.sample(range(0, max(qubit_list)), 1)[0]  # sample a distinct qubit
        operation_list.append(['q{}'.format(q_id)])

    return G, operation_list

def gen_qasm(qubit_list, operation_list, verbose=False):

    if verbose:
        for i in operation_list:
            if len(i) == 1:
                print("\tqubit\t%s" %(i[0]))
            elif len(i) == 2:
                print("\tUtwo\t%s,%s" %(i[0], i[1]))

    file_name = "circuit"
    with open(file_name + '.qasm', 'w') as f:
        line1= "# File:\t" + file_name + ".qasm\n"
        f.write(line1)
        line2= "# Date:\t" + date.today().strftime("%B %d, %Y") + "\n"
        f.write(line2)

        # print qubits
        for i in qubit_list:
            str_row = " qubit q" + str(i) + "\n"
            f.write(str_row)

        # print gates
        for i in operation_list:
            str_row = ''
            if len(i) == 1:
                str_row += " X %s\n" % (i[0])
            elif len(i) == 2:
                q1 = i[0]
                q2 = i[1]
                if q1[1] < q2[1]:
                    str_row += " Utwo %s,%s\n" % (i[0], i[1])
                else:
                    str_row += " Utwo %s,%s\n" % (i[1], i[0])

            f.write(str_row)
    return