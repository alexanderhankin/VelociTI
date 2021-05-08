import sys
import json
from math import comb
import pprint 
pp = pprint.PrettyPrinter(indent=4)

def run(config_file_path):

    with open (config_file_path) as config_file:
        config = json.load(config_file)
    
    #pp.pprint(config)
    
    # sample config
    #{   'circuit': {   '1-qubit gate latency [ns]': '5',
    #                   '1-qubit gates': '70',
    #                   '2-qubit gate latency inside chain [ns]': '10',
    #                   '2-qubit gates': '30',
    #                   'circuit depth': '3',
    #                   'penalty for 2-qubit gate between chains': '2'}}
    
    d = int(config["circuit"]["circuit depth"])
    q = int(config["circuit"]["1-qubit gates"])
    p = int(config["circuit"]["2-qubit gates"])
    alpha = float(config["circuit"]["penalty for 2-qubit gate between chains"])
    delta = float(config["circuit"]["1-qubit gate latency [ns]"])
    gamma = float(config["circuit"]["2-qubit gate latency inside chain [ns]"])
    
    pwl = 1/(comb(32,2)+1)
    upper_gamma = pwl*alpha*gamma+(1-pwl)*gamma
    t = d*(q*delta+p*upper_gamma)
    #print("execution time [ns] = ", t)
    return(t)
