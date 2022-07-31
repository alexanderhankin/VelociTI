import logging
import sys
import perf_model
import circuit
import pickle
import time


#def gen_benchmarks():
#
#    for i in range(10):
#        gen_supremacy()
#        gen_qaoa()
#        gen_squareroot()
#        gen_qft()
#        gen_adder()
#        gen_bv()


def main():

    logging.basicConfig(filename='perf_model.log', filemode='w', level=logging.INFO)
 
    if (sys.argv[1] == 'random'):# generate random circuit
        logging.info("GENERATING RANDOM CIRCUIT")
        print("GENERATING RANDOM CIRCUIT")
        chain_length = int(sys.argv[2])
        number_of_qubits = int(sys.argv[3])
        number_of_2q_gates = int(sys.argv[4])
        weak_link_penalty = float(sys.argv[5])
        chain_size, num_qubits, num_2q_gates, num_1q_gates, qubit_list, delta, gamma, alpha = circuit.gen_random_circuit(chain_length, number_of_qubits, number_of_2q_gates, weak_link_penalty)
        #t0 = time.time()
        num_weak_links, indices, qubit_placement_dict, operation_list = perf_model.generate_serial_architecture3(qubit_list, num_1q_gates, num_2q_gates, num_qubits, chain_size)
    elif (sys.argv[1] == 'random2'):# generate random circuit
        logging.info("GENERATING RANDOM CIRCUIT")
        print("GENERATING RANDOM CIRCUIT")
        chain_length = int(sys.argv[2])
        number_of_qubits = int(sys.argv[3])
        number_of_2q_gates = int(number_of_qubits*2)
        weak_link_penalty = float(sys.argv[4])
        chain_size, num_qubits, num_2q_gates, num_1q_gates, qubit_list, delta, gamma, alpha = circuit.gen_random_circuit(chain_length, number_of_qubits, number_of_2q_gates, weak_link_penalty)
        #t0 = time.time()
        num_weak_links, indices, qubit_placement_dict, operation_list = perf_model.generate_serial_architecture3(qubit_list, num_1q_gates, num_2q_gates, num_qubits, chain_size)
    elif (sys.argv[1] == 'supremacy'):# generate benchmark circuit
        logging.info("GENERATING SUPREMACY CIRCUIT")
        print("GENERATING SUPREMACY CIRCUIT")
        chain_length = int(sys.argv[2])
        chain_size, num_qubits, num_2q_gates, num_1q_gates, qubit_list, delta, gamma, alpha = circuit.gen_supremacy(chain_length)
        num_weak_links, indices, qubit_placement_dict, operation_list = perf_model.generate_serial_architecture3(qubit_list, num_1q_gates, num_2q_gates, num_qubits, chain_size)
    elif (sys.argv[1] == 'qaoa'):# generate benchmark circuit
        logging.info("GENERATING QAOA CIRCUIT")
        print("GENERATING QAOA CIRCUIT")
        chain_length = int(sys.argv[2])
        chain_size, num_qubits, num_2q_gates, num_1q_gates, qubit_list, delta, gamma, alpha = circuit.gen_qaoa(chain_length)
        num_weak_links, indices, qubit_placement_dict, operation_list = perf_model.generate_serial_architecture3(qubit_list, num_1q_gates, num_2q_gates, num_qubits, chain_size)
    elif (sys.argv[1] == 'squareroot'):# generate benchmark circuit
        logging.info("GENERATING SQUARE ROOT CIRCUIT")
        print("GENERATING SQUARE ROOT CIRCUIT")
        chain_length = int(sys.argv[2])
        chain_size, num_qubits, num_2q_gates, num_1q_gates, qubit_list, delta, gamma, alpha = circuit.gen_squareroot(chain_length)
        num_weak_links, indices, qubit_placement_dict, operation_list = perf_model.generate_serial_architecture3(qubit_list, num_1q_gates, num_2q_gates, num_qubits, chain_size)
    elif (sys.argv[1] == 'qft'):# generate benchmark circuit
        logging.info("GENERATING QFT CIRCUIT")
        print("GENERATING QFT CIRCUIT")
        chain_length = int(sys.argv[2])
        chain_size, num_qubits, num_2q_gates, num_1q_gates, qubit_list, delta, gamma, alpha = circuit.gen_qft(chain_length)
        num_weak_links, indices, qubit_placement_dict, operation_list = perf_model.generate_serial_architecture3(qubit_list, num_1q_gates, num_2q_gates, num_qubits, chain_size)
    elif (sys.argv[1] == 'adder'):# generate benchmark circuit
        logging.info("GENERATING ADDER CIRCUIT")
        print("GENERATING ADDER CIRCUIT")
        chain_length = int(sys.argv[2])
        chain_size, num_qubits, num_2q_gates, num_1q_gates, qubit_list, delta, gamma, alpha = circuit.gen_adder(chain_length)
        num_weak_links, indices, qubit_placement_dict, operation_list = perf_model.generate_serial_architecture3(qubit_list, num_1q_gates, num_2q_gates, num_qubits, chain_size)
    elif (sys.argv[1] == 'bv'):# generate benchmark circuit
        logging.info("GENERATING BV CIRCUIT")
        print("GENERATING BV CIRCUIT")
        chain_length = int(sys.argv[2])
        chain_size, num_qubits, num_2q_gates, num_1q_gates, qubit_list, delta, gamma, alpha = circuit.gen_bv(chain_length)
        num_weak_links, indices, qubit_placement_dict, operation_list = perf_model.generate_serial_architecture3(qubit_list, num_1q_gates, num_2q_gates, num_qubits, chain_size)
    elif (sys.argv[1] == 'qv'):# generate benchmark circuit
        logging.info("GENERATING QUANTUM VOLUME CIRCUIT")
        print("GENERATING QUANTUM VOLUME CIRCUIT")
        chain_length = int(sys.argv[2])
        number_of_qubits = int(sys.argv[3])
        number_of_2q_gates = int(number_of_qubits/2) 
        weak_link_penalty = float(sys.argv[4])
        chain_size, num_qubits, num_2q_gates, num_1q_gates, qubit_list, delta, gamma, alpha = circuit.gen_QV(chain_length, number_of_qubits, number_of_2q_gates, weak_link_penalty)
        num_weak_links, indices, qubit_placement_dict, operation_list = perf_model.generate_serial_architecture3(qubit_list, num_1q_gates, num_2q_gates, num_qubits, chain_size)
    else: # load circuit from config
        logging.info("LOADING CIRCUIT FROM JSON")
        print("LOADING CIRCUIT FROM JSON")
        num_1q_gates, num_2q_gates, alpha, delta, gamma, qubits_per_chain, num_qubits, num_chains, qubit_placement_dict, cut_sizes, indices, operation_list = circuit.load_config(sys.argv[1])

    DG = perf_model.generate_parallel_architecture(operation_list, qubit_placement_dict, alpha)
    
    #logging.info("Cut sizes: %s", cut_sizes)
    #logging.info("Indices: %s", indices)
    #logging.info("Qubit placement: %s", qubit_placement_dict)
    
    logging.info("RESULTS")
    serial_t = perf_model.compute_serial_t2(delta, num_1q_gates, num_2q_gates, num_weak_links, gamma, alpha)
    parallel_t = perf_model.compute_parallel_t(DG)
    #t1 = time.time()
    #total = t1 - t0
    #print("Simulation time [s]: ", total)


if __name__ == "__main__":
    main()

