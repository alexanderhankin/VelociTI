import networkx as nx
import matplotlib.pyplot as plt
import random


num_qubits = 5
qubits_per_chain = 4
num_1-qubit_gates = 1
num_2-qubit_gates = 2

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



#G = nx.gnp_random_graph(10, 0.2, 138)
#nx.set_edge_attributes(G, {e: {'weight': random.randint(1, 10)} for e in G.edges})
#pos=nx.random_layout(G)
##pos=nx.get_node_attributes(G,'pos')
#nx.draw(G, pos, with_labels = True)
#labels = nx.get_edge_attributes(G,'weight')
#nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
#plt.axis('off')
#plt.savefig('my_graph.png')
#
#print(type(G))
#largest_cc = max(nx.connected_components(G), key=len)
#print("Largest component: ", largest_cc)
##E = nx.minimum_edge_cut(G)
##print(E)
