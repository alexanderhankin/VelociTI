import networkx as nx
import matplotlib.pyplot as plt
import random
from run import load_config
import json

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


num_qubits = 5
qubits_per_chain = 4
num_one_qubit_gates = 1
num_two_qubit_gates = 2

d, q, p, alpha, delta, gamma = load_config('configs/3layer_test.json')

G = nx.Graph()
G.add_node('q1')
G.add_node('q2')
G.add_node('q3')
G.add_node('q4')
G.add_node('q5')
G.add_edge('q2', 'q3', weight=2)
G.add_edge('q2', 'q4')
G.add_edge('q2', 'q5')
#pos=nx.random_layout(G)
#nx.draw(G, pos, with_labels = True)
#labels = nx.get_edge_attributes(G,'weight')
#nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
#plt.axis('off')
#plt.savefig('my_graph.png')

weak_links_cut_1 = nx.cut_size(G,{'q1', 'q2', 'q3'}, {'q4', 'q5'})
weak_links_cut_2 = nx.cut_size(G,{'q1'}, {'q2', 'q3', 'q4', 'q5'})
#print(weak_links_cut_1)
#print(weak_links_cut_2)

t_cut_1 = delta*num_one_qubit_gates # 1 qubit-gate latencies
t_cut_1 = t_cut_1 + (num_two_qubit_gates-weak_links_cut_1)*gamma + weak_links_cut_1*gamma*alpha # 2-qubit gate latencies

t_cut_2 = delta*num_one_qubit_gates # 1 qubit-gate latencies
t_cut_2 = t_cut_2 + (num_two_qubit_gates-weak_links_cut_2)*gamma + weak_links_cut_2*gamma*alpha # 2-qubit gate latencies

print("t for cut 1 [ns]:", t_cut_1)
print("t for cut 2 [ns]:", t_cut_2)


