import logging
import json
import random


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


def gen_random_circuit():
    
    chain_size = 16
    logging.info("Chain size: %s", chain_size)
    num_qubits = random.randint(4, 48)
    logging.info("Num qubits: %d", num_qubits)
    num_2q_gates = random.randint(num_qubits, num_qubits + 4)
    logging.info("Num 2-qubit gates: %d", num_2q_gates)
    num_1q_gates = random.randint(0, num_qubits + 60)
    logging.info("Num 1-qubit gates: %d", num_1q_gates)
    qubit_list = list(range(num_qubits))
    logging.info("Qubit list: %s", qubit_list)
    delta = 1
    gamma = 100
    alpha = 2

    print("Chain size: ", chain_size)
    print("Num qubits: ", num_qubits)
    print("Num 2-qubit gates: ", num_2q_gates)
    print("Num 1-qubit gates: ", num_1q_gates)

    return chain_size, num_qubits, num_2q_gates, num_1q_gates, qubit_list, delta, gamma, alpha



def gen_supremacy():

    chain_size = 16 
    logging.info("Chain size: %s", chain_size)
    num_qubits = 64
    logging.info("Num qubits: %d", num_qubits)
    num_2q_gates = 560
    logging.info("Num 2-qubit gates: %d", num_2q_gates)
    num_1q_gates = 0
    logging.info("Num 1-qubit gates: %d", num_1q_gates)
    qubit_list = list(range(num_qubits))
    logging.info("Qubit list: %s", qubit_list)
    delta = 1
    gamma = 100
    alpha = 2

    print("Chain size: ", chain_size)
    print("Num qubits: ", num_qubits)
    print("Num 2-qubit gates: ", num_2q_gates)
    print("Num 1-qubit gates: ", num_1q_gates)

    return chain_size, num_qubits, num_2q_gates, num_1q_gates, qubit_list, delta, gamma, alpha


def gen_qaoa():

    chain_size = 16 
    logging.info("Chain size: %s", chain_size)
    num_qubits = 64
    logging.info("Num qubits: %d", num_qubits)
    num_2q_gates = 1260
    logging.info("Num 2-qubit gates: %d", num_2q_gates)
    num_1q_gates = 0
    logging.info("Num 1-qubit gates: %d", num_1q_gates)
    qubit_list = list(range(num_qubits))
    logging.info("Qubit list: %s", qubit_list)
    delta = 1
    gamma = 100
    alpha = 2

    print("Chain size: ", chain_size)
    print("Num qubits: ", num_qubits)
    print("Num 2-qubit gates: ", num_2q_gates)
    print("Num 1-qubit gates: ", num_1q_gates)

    return chain_size, num_qubits, num_2q_gates, num_1q_gates, qubit_list, delta, gamma, alpha


def gen_squareroot():

    chain_size = 16 
    logging.info("Chain size: %s", chain_size)
    num_qubits = 78
    logging.info("Num qubits: %d", num_qubits)
    num_2q_gates = 1028
    logging.info("Num 2-qubit gates: %d", num_2q_gates)
    num_1q_gates = 0
    logging.info("Num 1-qubit gates: %d", num_1q_gates)
    qubit_list = list(range(num_qubits))
    logging.info("Qubit list: %s", qubit_list)
    delta = 1
    gamma = 100
    alpha = 2

    print("Chain size: ", chain_size)
    print("Num qubits: ", num_qubits)
    print("Num 2-qubit gates: ", num_2q_gates)
    print("Num 1-qubit gates: ", num_1q_gates)

    return chain_size, num_qubits, num_2q_gates, num_1q_gates, qubit_list, delta, gamma, alpha


def gen_qft():

    chain_size = 16 
    logging.info("Chain size: %s", chain_size)
    num_qubits = 64
    logging.info("Num qubits: %d", num_qubits)
    num_2q_gates = 4032
    logging.info("Num 2-qubit gates: %d", num_2q_gates)
    num_1q_gates = 0
    logging.info("Num 1-qubit gates: %d", num_1q_gates)
    qubit_list = list(range(num_qubits))
    logging.info("Qubit list: %s", qubit_list)
    delta = 1
    gamma = 100
    alpha = 2

    print("Chain size: ", chain_size)
    print("Num qubits: ", num_qubits)
    print("Num 2-qubit gates: ", num_2q_gates)
    print("Num 1-qubit gates: ", num_1q_gates)

    return chain_size, num_qubits, num_2q_gates, num_1q_gates, qubit_list, delta, gamma, alpha


def gen_adder():

    chain_size = 16 
    logging.info("Chain size: %s", chain_size)
    num_qubits = 64
    logging.info("Num qubits: %d", num_qubits)
    num_2q_gates = 4032
    logging.info("Num 2-qubit gates: %d", num_2q_gates)
    num_1q_gates = 0
    logging.info("Num 1-qubit gates: %d", num_1q_gates)
    qubit_list = list(range(num_qubits))
    logging.info("Qubit list: %s", qubit_list)
    delta = 1
    gamma = 100
    alpha = 2
    
    outfile = "adder.out"

    print("Chain size: ", chain_size)
    print("Num qubits: ", num_qubits)
    print("Num 2-qubit gates: ", num_2q_gates)
    print("Num 1-qubit gates: ", num_1q_gates)

    return chain_size, num_qubits, num_2q_gates, num_1q_gates, qubit_list, delta, gamma, alpha


def gen_bv():

    chain_size = 16 
    logging.info("Chain size: %s", chain_size)
    num_qubits = 64
    logging.info("Num qubits: %d", num_qubits)
    num_2q_gates = 64
    logging.info("Num 2-qubit gates: %d", num_2q_gates)
    num_1q_gates = 0
    logging.info("Num 1-qubit gates: %d", num_1q_gates)
    qubit_list = list(range(num_qubits))
    logging.info("Qubit list: %s", qubit_list)
    delta = 1
    gamma = 100
    alpha = 2

    outfile = "bv.out"

    print("Chain size: ", chain_size)
    print("Num qubits: ", num_qubits)
    print("Num 2-qubit gates: ", num_2q_gates)
    print("Num 1-qubit gates: ", num_1q_gates)

    return chain_size, num_qubits, num_2q_gates, num_1q_gates, qubit_list, delta, gamma, alpha
