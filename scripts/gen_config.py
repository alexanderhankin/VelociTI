import json
import os
import pandas as pd
import csv
import matplotlib.pyplot as plt
from run import *

plt.rc('xtick',labelsize=16)
plt.rc('ytick',labelsize=16)
plt.rc('legend', fontsize=16)
plt.rc('axes', labelsize=16)

if not os.path.exists('./configs'):
    os.makedirs('./configs')
if not os.path.exists('./output'):
    os.makedirs('./output')

# sweep configurations
#d = [1, 2, 3, 4] # circuit depth
#q = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] # number of 1-qubit gates
#p = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] # number of 2-qubit gates
#alpha = [1.5, 2, 2.5, 3] # latency penalty
#delta = [5, 10, 20, 30] # time for 1-qubit gate
#gamma = [10, 20, 30, 40, 50] # time for 2-qubit gate inside chain

# circuit depth sweep
#d = [1, 2, 3, 4] # circuit depth
#q = [50] # number of 1-qubit gates
#p = [50] # number of 2-qubit gates
#alpha = [2] # latency penalty
#delta = [10] # time for 1-qubit gate [ns]
#gamma = [20] # time for 2-qubit gate inside chain [ns]

# number of 1-qubit gates sweep
d = [3] # circuit depth
q = [10, 20, 30, 40, 50] # number of 1-qubit gates
p = [50] # number of 2-qubit gates
alpha = [2] # latency penalty
delta = [10] # time for 1-qubit gate [ns]
gamma = [20] # time for 2-qubit gate inside chain [ns]

# number of 2-qubit gates sweep
#d = [3] # circuit depth
#q = [50] # number of 1-qubit gates
#p = [10, 20, 30, 40, 50] # number of 2-qubit gates
#alpha = [2] # latency penalty
#delta = [10] # time for 1-qubit gate [ns]
#gamma = [20] # time for 2-qubit gate inside chain [ns]

# time for 2-qubit gates sweep
#d = [3] # circuit depth
#q = [50] # number of 1-qubit gates
#p = [50] # number of 2-qubit gates
#alpha = [2] # latency penalty
#delta = [10] # time for 1-qubit gate [ns]
#gamma = [15, 20, 25, 30, 40, 50] # time for 2-qubit gate inside chain [ns]

# time for 1-qubit gates sweep
#d = [3] # circuit depth
#q = [50] # number of 1-qubit gates
#p = [50] # number of 2-qubit gates
#alpha = [2] # latency penalty
#delta = [5, 7.5, 10, 12.5, 15] # time for 1-qubit gate [ns]
#gamma = [20] # time for 2-qubit gate inside chain [ns]

# latency penalty sweep 
#d = [3] # circuit depth
#q = [50] # number of 1-qubit gates
#p = [50] # number of 2-qubit gates
#alpha = [1.5, 2, 2.5, 3, 5, 10] # latency penalty
#delta = [10] # time for 1-qubit gate [ns]
#gamma = [20] # time for 2-qubit gate inside chain [ns]

config = {}
results_list = []

# generate config files and run timing model
for _d in d:
    for _q in q:
        for _p in p:
            for _alpha in alpha:
                for _delta in delta:
                    for _gamma in gamma:
                        print("[INFO]: Generating config {}_{}_{}_{}_{}_{}".format(_delta, _q, _gamma, _p, _d, _alpha))
                        config = {   'circuit': {   '1-qubit gate latency [ns]': _delta,
                                               '1-qubit gates': _q,
                                               '2-qubit gate latency inside chain [ns]': _gamma,
                                               '2-qubit gates': _p,
                                               'circuit depth': _d,
                                               'penalty for 2-qubit gate between chains': _alpha}}
                        filename = 'configs/{}_{}_{}_{}_{}_{}.json'.format(_delta, _q, _gamma, _p, _d, _alpha)
                        with open(filename, 'w') as fp:
                            json.dump(config, fp)
                        print("[INFO]: Simulating {}_{}_{}_{}_{}_{}".format(_delta, _q, _gamma, _p, _d, _alpha))
                        t = run(filename)
                        result = {}
                        result = config["circuit"]
                        result["execution time [ns]"] = t
                        results_list.append(result)
                       
# post-process results
print("[INFO]: Processing results") 

# save results as csv
keys = results_list[0].keys()
with open("./output/{}_{}_{}_{}_{}_{}.csv".format(delta, q, gamma, p, d, alpha), 'w', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(results_list)

df = pd.DataFrame(results_list)
if len(d) > 0:
    df.plot.bar(x="circuit depth", y="execution time [ns]", rot=0).grid(axis='y')
    plt.savefig('./output/circuit_depth.png')
if len(q) > 0:
    df.plot(x="1-qubit gates", y="execution time [ns]").grid(axis='y')
    plt.savefig('./output/1-qubit_gates.png')
if len(p) > 0:
    df.plot(x="2-qubit gates", y="execution time [ns]").grid(axis='y')
    plt.savefig('./output/2-qubit_gates.png')
if len(gamma) > 0:
    df.plot(x="2-qubit gate latency inside chain [ns]", y="execution time [ns]").grid(axis='y')
    plt.savefig('./output/2-qubit_gate_latency_inside_chain.png')
if len(delta) > 0:
    df.plot(x="1-qubit gate latency [ns]", y="execution time [ns]").grid(axis='y')
    plt.savefig('./output/1-qubit_gate_latency.png')
if len(alpha) > 0:
    df.plot(x="penalty for 2-qubit gate between chains", y="execution time [ns]").grid(axis='y')
    plt.savefig('./output/penalty_for_2-qubit_gate_between_chains.png')
