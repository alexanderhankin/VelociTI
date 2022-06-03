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
