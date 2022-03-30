import sys
import json
from math import comb
from math import ceil
import pprint 
import numpy as np
pp = pprint.PrettyPrinter(indent=4)


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


def compute_num_weak_links(num_chains):
    
    if num_chains == 1:
        num_weak_links = 0
    elif num_chains/2 == 0:
        num_weak_links = num_chains
    else:
        num_weak_links = num_chains - 1

    return num_weak_links


def compute_layer_t_old(d, q, p, alpha, delta, gamma):

    pwl = 1/(comb(32,2)+1)
    upper_gamma = pwl*alpha*gamma+(1-pwl)*gamma
    t = d*(q*delta+p*upper_gamma)
    return t
    

def compute_layer_t(d, q, p, alpha, delta, gamma, num_chains, num_weak_links, weak_links_used):    

    t = 0.0

    t = t + q*delta # add latency from 1-qubit gates

    # loop through number of 2-qubit gates
    for gate in range(int(p)): 
        if weak_links_used < num_weak_links: # there could still be a weak link
            sample = np.random.randint(0,32*num_chains) 
            if sample in list(range(num_weak_links)):
                t += alpha*gamma # weak link present
                weak_links_used = weak_links_used + 1
            else:
                t = t + gamma
        else: # no weak links left
            t = t + gamma
    
    return t, weak_links_used
    

def run(config_file_path):

    d, q, p, alpha, delta, gamma = load_config(config_file_path)
    
    t = 0.0
    num_qubits = 2*sum(p) + sum(q) # calculate number of qubits across all layers
    num_chains = ceil(num_qubits/32)
    num_weak_links = compute_num_weak_links(num_chains)
    weak_links_used = 0

    print("Num qubits: ", num_qubits)
    print("Num chains: ", num_chains)
    print("Num weak links: ", num_weak_links)

    for layer in range(d):
        old_weak_links_used = weak_links_used # to keep track of weak links used in different layers
        t_layer, weak_links_used = compute_layer_t(d, q[layer], p[layer], alpha, delta, gamma, num_chains, num_weak_links, weak_links_used)
        t = t + t_layer
        print("Timing of layer{}: {}".format(layer+1, t))
        print("Number of weak links used in layer{}: {}".format(layer+1, weak_links_used-old_weak_links_used))

    return t

def main():

    print("Timing [ns]: ", run(sys.argv[1]))

if __name__ == "__main__":
    main()
