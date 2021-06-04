import networkx as nx
import matplotlib.pyplot as plt
import random

G = nx.gnp_random_graph(10, 0.3, 138)
nx.set_edge_attributes(G, {e: {'weight': random.randint(1, 10)} for e in G.edges})
pos=nx.random_layout(G)
#pos=nx.get_node_attributes(G,'pos')
nx.draw(G, pos)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.axis('off')
plt.savefig('my_graph.png')
