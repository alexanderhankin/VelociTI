import logging
import sys
import perf_model
import circuit
from util import *
import pickle


def main():

    check_args()
    if getVerbose(): printArgs()
    logging.basicConfig(filename='perf_model.log', filemode='w', level=logging.INFO)

    qubit_placement_dict = {}

    # if (sys.argv[1] == 'random'):# generate random circuit
    if (getCircuitInput() == 'random'):# generate random circuit
        logging.info("GENERATING RANDOM CIRCUIT")
        print("GENERATING RANDOM CIRCUIT")
        chain_size, num_qubits, num_2q_gates, num_1q_gates, qubit_list, delta, gamma, alpha = circuit.gen_random_circuit()
        cut_sizes, indices, qubit_placement_dict, operation_list = perf_model.generate_serial_architecture(qubit_list, num_1q_gates, num_2q_gates, num_qubits, chain_size)

    elif (getCircuitInput() == 'json'): # load circuit from config
        logging.info("LOADING CIRCUIT FROM JSON")
        print("LOADING CIRCUIT FROM JSON")
        num_1q_gates, num_2q_gates, alpha, delta, gamma, qubits_per_chain, num_qubits, num_chains, qubit_placement_dict, cut_sizes, indices, operation_list = circuit.load_config(getJsonFile())

    elif (getCircuitInput() == 'cmd'):
        logging.info("GENERATING CIRCUIT FROM CMDLINE ARGS")
        print("GENERATING CIRCUIT FROM CMDLINE ARGS")

        chain_size, num_qubits, num_2q_gates, num_1q_gates, qubit_list, delta, gamma, alpha = circuit.gen_random_circuit(chain_size=getChainSize(),
                                                                                                                         num_qubits_min=getNumQubits(),
                                                                                                                         num_qubits_max=getNumQubits(),
                                                                                                                         latency_1q=getq1latency(),
                                                                                                                         latency_2q=getq2latency(),
                                                                                                                         num_1q_gates=getnum1qGates(),
                                                                                                                         num_2q_gates=getnum2qGates(),
                                                                                                                         weaklink_scale_factor=getWeakLinkPen(),
                                                                                                                         verbose=getVerbose(),
                                                                                                                         )
        cut_sizes, indices, qubit_placement_dict, operation_list = \
            perf_model.generate_serial_architecture(qubit_list, num_1q_gates, num_2q_gates, num_qubits, chain_size)

    else:
        exit("ERROR: Unrecognized input for circuit")


    assert(bool(qubit_placement_dict))
    DG = perf_model.generate_parallel_architecture(operation_list, qubit_placement_dict)
    
    logging.info("Cut sizes: %s", cut_sizes)
    logging.info("Indices: %s", indices)
    logging.info("Qubit placement: %s", qubit_placement_dict)
    
    logging.info("RESULTS")
    serial_t = perf_model.compute_serial_t(delta, num_1q_gates, num_2q_gates, cut_sizes, gamma, alpha)
    parallel_t = perf_model.compute_parallel_t(DG)


if __name__ == "__main__":
    main()

