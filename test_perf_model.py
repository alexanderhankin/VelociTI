import unittest
import perf_model
import circuit


class TestPerfModel(unittest.TestCase):


    def test_circuit_1(self):
        
        num_1q_gates, num_2q_gates, alpha, delta, gamma, qubits_per_chain, num_qubits, num_chains, qubit_placement_dict, operation_list = circuit.load_config_simple('configs/test/circuit_1.json')
        DG = perf_model.generate_parallel_architecture(operation_list, qubit_placement_dict)
        parallel_t = perf_model.compute_parallel_t(DG)
        self.assertEqual(parallel_t, 400)

    def test_circuit_2(self):
        
        num_1q_gates, num_2q_gates, alpha, delta, gamma, qubits_per_chain, num_qubits, num_chains, qubit_placement_dict, operation_list = circuit.load_config_simple('configs/test/circuit_2.json')
        DG = perf_model.generate_parallel_architecture(operation_list, qubit_placement_dict)
        parallel_t = perf_model.compute_parallel_t(DG)
        self.assertEqual(parallel_t, 300)

    def test_circuit_3(self):
        
        num_1q_gates, num_2q_gates, alpha, delta, gamma, qubits_per_chain, num_qubits, num_chains, qubit_placement_dict, operation_list = circuit.load_config_simple('configs/test/circuit_3.json')
        DG = perf_model.generate_parallel_architecture(operation_list, qubit_placement_dict)
        parallel_t = perf_model.compute_parallel_t(DG)
        self.assertEqual(parallel_t, 700)

    def test_circuit_4(self):
        
        num_1q_gates, num_2q_gates, alpha, delta, gamma, qubits_per_chain, num_qubits, num_chains, qubit_placement_dict, operation_list = circuit.load_config_simple('configs/test/circuit_4.json')
        DG = perf_model.generate_parallel_architecture(operation_list, qubit_placement_dict)
        parallel_t = perf_model.compute_parallel_t(DG)
        self.assertEqual(parallel_t, 401)

    def test_circuit_5(self):
        
        num_1q_gates, num_2q_gates, alpha, delta, gamma, qubits_per_chain, num_qubits, num_chains, qubit_placement_dict, operation_list = circuit.load_config_simple('configs/test/circuit_5.json')
        DG = perf_model.generate_parallel_architecture(operation_list, qubit_placement_dict)
        parallel_t = perf_model.compute_parallel_t(DG)
        self.assertEqual(parallel_t, 1001)

if __name__ == '__main__':
    unittest.main()
