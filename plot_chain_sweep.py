import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import gmean

#Chain size:  16
#Num qubits:  64
#Num 2-qubit gates:  560
#Num 1-qubit gates:  0
#Num chains:  4
#Number of weak links:  4

# set edgecolor param (this is a global setting, so only set it once)
plt.rcParams["patch.force_edgecolor"] = True
plt.rcParams['errorbar.capsize'] = 10
plt.rcParams.update({'font.size': 16})

supremacy8_num_weak_links = []
supremacy16_num_weak_links = []
supremacy24_num_weak_links = []
supremacy32_num_weak_links = []
supremacy8_serial_perf = []
supremacy8_parallel_perf = []
supremacy16_serial_perf = []
supremacy16_parallel_perf = []
supremacy24_serial_perf = []
supremacy24_parallel_perf = []
supremacy32_serial_perf = []
supremacy32_parallel_perf = []
supremacy_error_serial_perf = []
supremacy_error_parallel_perf = []

qaoa8_num_weak_links = []
qaoa16_num_weak_links = []
qaoa24_num_weak_links = []
qaoa32_num_weak_links = []
qaoa8_serial_perf = []
qaoa8_parallel_perf = []
qaoa16_serial_perf = []
qaoa16_parallel_perf = []
qaoa24_serial_perf = []
qaoa24_parallel_perf = []
qaoa32_serial_perf = []
qaoa32_parallel_perf = []
qaoa_error_serial_perf = []
qaoa_error_parallel_perf = []

squareroot8_num_weak_links = []
squareroot16_num_weak_links = []
squareroot24_num_weak_links = []
squareroot32_num_weak_links = []
squareroot8_serial_perf = []
squareroot8_parallel_perf = []
squareroot16_serial_perf = []
squareroot16_parallel_perf = []
squareroot24_serial_perf = []
squareroot24_parallel_perf = []
squareroot32_serial_perf = []
squareroot32_parallel_perf = []
squareroot_error_serial_perf = []
squareroot_error_parallel_perf = []

qft8_num_weak_links = []
qft16_num_weak_links = []
qft24_num_weak_links = []
qft32_num_weak_links = []
qft8_serial_perf = []
qft8_parallel_perf = []
qft16_serial_perf = []
qft16_parallel_perf = []
qft24_serial_perf = []
qft24_parallel_perf = []
qft32_serial_perf = []
qft32_parallel_perf = []
qft_error_serial_perf = []
qft_error_parallel_perf = []

adder8_num_weak_links = []
adder16_num_weak_links = []
adder24_num_weak_links = []
adder32_num_weak_links = []
adder8_serial_perf = []
adder8_parallel_perf = []
adder16_serial_perf = []
adder16_parallel_perf = []
adder24_serial_perf = []
adder24_parallel_perf = []
adder32_serial_perf = []
adder32_parallel_perf = []
adder_error_serial_perf = []
adder_error_parallel_perf = []

bv8_num_weak_links = []
bv16_num_weak_links = []
bv24_num_weak_links = []
bv32_num_weak_links = []
bv8_serial_perf = []
bv8_parallel_perf = []
bv16_serial_perf = []
bv16_parallel_perf = []
bv24_serial_perf = []
bv24_parallel_perf = []
bv32_serial_perf = []
bv32_parallel_perf = []
bv_error_serial_perf = []
bv_error_parallel_perf = []

# supremacy8
with open('supremacy8.out') as file:
    for line in file:
        if 'Number of weak links:' in line:
            val = line.rstrip().split(":")[-1]
            supremacy8_num_weak_links.append(int(val)) 
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            supremacy8_serial_perf.append(int(val)/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            supremacy8_parallel_perf.append(int(val)/1000) 

supremacy8_max_serial = max(supremacy8_serial_perf)
supremacy8_min_serial = min(supremacy8_serial_perf)
supremacy8_max_parallel = max(supremacy8_parallel_perf)
supremacy8_min_parallel = min(supremacy8_parallel_perf)
supremacy8_avg_serial = sum(supremacy8_serial_perf)/len(supremacy8_serial_perf)
supremacy8_avg_parallel = sum(supremacy8_parallel_perf)/len(supremacy8_parallel_perf)
print(supremacy8_num_weak_links)


# supremacy16
with open('supremacy16.out') as file:
    for line in file:
        if 'Number of weak links:' in line:
            val = line.rstrip().split(":")[-1]
            supremacy16_num_weak_links.append(int(val)) 
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            supremacy16_serial_perf.append(int(val)/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            supremacy16_parallel_perf.append(int(val)/1000) 

supremacy16_max_serial = max(supremacy16_serial_perf)
supremacy16_min_serial = min(supremacy16_serial_perf)
supremacy16_max_parallel = max(supremacy16_parallel_perf)
supremacy16_min_parallel = min(supremacy16_parallel_perf)
supremacy16_avg_serial = sum(supremacy16_serial_perf)/len(supremacy16_serial_perf)
supremacy16_avg_parallel = sum(supremacy16_parallel_perf)/len(supremacy16_parallel_perf)
print(supremacy16_num_weak_links)


# supremacy24
with open('supremacy24.out') as file:
    for line in file:
        if 'Number of weak links:' in line:
            val = line.rstrip().split(":")[-1]
            supremacy24_num_weak_links.append(int(val)) 
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            supremacy24_serial_perf.append(int(val)/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            supremacy24_parallel_perf.append(int(val)/1000) 

supremacy24_max_serial = max(supremacy24_serial_perf)
supremacy24_min_serial = min(supremacy24_serial_perf)
supremacy24_max_parallel = max(supremacy24_parallel_perf)
supremacy24_min_parallel = min(supremacy24_parallel_perf)
supremacy24_avg_serial = sum(supremacy24_serial_perf)/len(supremacy24_serial_perf)
supremacy24_avg_parallel = sum(supremacy24_parallel_perf)/len(supremacy24_parallel_perf)
print(supremacy24_num_weak_links)


# supremacy32
with open('supremacy32.out') as file:
    for line in file:
        if 'Number of weak links:' in line:
            val = line.rstrip().split(":")[-1]
            supremacy32_num_weak_links.append(int(val)) 
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            supremacy32_serial_perf.append(int(val)/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            supremacy32_parallel_perf.append(int(val)/1000) 

supremacy32_max_serial = max(supremacy32_serial_perf)
supremacy32_min_serial = min(supremacy32_serial_perf)
supremacy32_max_parallel = max(supremacy32_parallel_perf)
supremacy32_min_parallel = min(supremacy32_parallel_perf)
supremacy32_avg_serial = sum(supremacy32_serial_perf)/len(supremacy32_serial_perf)
supremacy32_avg_parallel = sum(supremacy32_parallel_perf)/len(supremacy32_parallel_perf)
print(supremacy32_num_weak_links)


# qaoa8
with open('qaoa8.out') as file:
    for line in file:
        if 'Number of weak links:' in line:
            val = line.rstrip().split(":")[-1]
            qaoa8_num_weak_links.append(int(val)) 
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qaoa8_serial_perf.append(int(val)/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qaoa8_parallel_perf.append(int(val)/1000) 

qaoa8_max_serial = max(qaoa8_serial_perf)
qaoa8_min_serial = min(qaoa8_serial_perf)
qaoa8_max_parallel = max(qaoa8_parallel_perf)
qaoa8_min_parallel = min(qaoa8_parallel_perf)
qaoa8_avg_serial = sum(qaoa8_serial_perf)/len(qaoa8_serial_perf)
qaoa8_avg_parallel = sum(qaoa8_parallel_perf)/len(qaoa8_parallel_perf)
print(qaoa8_num_weak_links)


# qaoa16
with open('qaoa16.out') as file:
    for line in file:
        if 'Number of weak links:' in line:
            val = line.rstrip().split(":")[-1]
            qaoa16_num_weak_links.append(int(val)) 
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qaoa16_serial_perf.append(int(val)/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qaoa16_parallel_perf.append(int(val)/1000) 

qaoa16_max_serial = max(qaoa16_serial_perf)
qaoa16_min_serial = min(qaoa16_serial_perf)
qaoa16_max_parallel = max(qaoa16_parallel_perf)
qaoa16_min_parallel = min(qaoa16_parallel_perf)
qaoa16_avg_serial = sum(qaoa16_serial_perf)/len(qaoa16_serial_perf)
qaoa16_avg_parallel = sum(qaoa16_parallel_perf)/len(qaoa16_parallel_perf)
print(qaoa16_num_weak_links)


# qaoa24
with open('qaoa24.out') as file:
    for line in file:
        if 'Number of weak links:' in line:
            val = line.rstrip().split(":")[-1]
            qaoa24_num_weak_links.append(int(val)) 
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qaoa24_serial_perf.append(int(val)/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qaoa24_parallel_perf.append(int(val)/1000) 

qaoa24_max_serial = max(qaoa24_serial_perf)
qaoa24_min_serial = min(qaoa24_serial_perf)
qaoa24_max_parallel = max(qaoa24_parallel_perf)
qaoa24_min_parallel = min(qaoa24_parallel_perf)
qaoa24_avg_serial = sum(qaoa24_serial_perf)/len(qaoa24_serial_perf)
qaoa24_avg_parallel = sum(qaoa24_parallel_perf)/len(qaoa24_parallel_perf)
print(qaoa24_num_weak_links)


# qaoa32
with open('qaoa32.out') as file:
    for line in file:
        if 'Number of weak links:' in line:
            val = line.rstrip().split(":")[-1]
            qaoa32_num_weak_links.append(int(val)) 
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qaoa32_serial_perf.append(int(val)/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qaoa32_parallel_perf.append(int(val)/1000) 

qaoa32_max_serial = max(qaoa32_serial_perf)
qaoa32_min_serial = min(qaoa32_serial_perf)
qaoa32_max_parallel = max(qaoa32_parallel_perf)
qaoa32_min_parallel = min(qaoa32_parallel_perf)
qaoa32_avg_serial = sum(qaoa32_serial_perf)/len(qaoa32_serial_perf)
qaoa32_avg_parallel = sum(qaoa32_parallel_perf)/len(qaoa32_parallel_perf)
print(qaoa32_num_weak_links)


# squareroot8
with open('squareroot8.out') as file:
    for line in file:
        if 'Number of weak links:' in line:
            val = line.rstrip().split(":")[-1]
            squareroot8_num_weak_links.append(int(val)) 
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            squareroot8_serial_perf.append(int(val)/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            squareroot8_parallel_perf.append(int(val)/1000) 

squareroot8_max_serial = max(squareroot8_serial_perf)
squareroot8_min_serial = min(squareroot8_serial_perf)
squareroot8_max_parallel = max(squareroot8_parallel_perf)
squareroot8_min_parallel = min(squareroot8_parallel_perf)
squareroot8_avg_serial = sum(squareroot8_serial_perf)/len(squareroot8_serial_perf)
squareroot8_avg_parallel = sum(squareroot8_parallel_perf)/len(squareroot8_parallel_perf)
print(squareroot8_num_weak_links)


# squareroot16
with open('squareroot16.out') as file:
    for line in file:
        if 'Number of weak links:' in line:
            val = line.rstrip().split(":")[-1]
            squareroot16_num_weak_links.append(int(val)) 
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            squareroot16_serial_perf.append(int(val)/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            squareroot16_parallel_perf.append(int(val)/1000) 

squareroot16_max_serial = max(squareroot16_serial_perf)
squareroot16_min_serial = min(squareroot16_serial_perf)
squareroot16_max_parallel = max(squareroot16_parallel_perf)
squareroot16_min_parallel = min(squareroot16_parallel_perf)
squareroot16_avg_serial = sum(squareroot16_serial_perf)/len(squareroot16_serial_perf)
squareroot16_avg_parallel = sum(squareroot16_parallel_perf)/len(squareroot16_parallel_perf)
print(squareroot16_num_weak_links)


# squareroot24
with open('squareroot24.out') as file:
    for line in file:
        if 'Number of weak links:' in line:
            val = line.rstrip().split(":")[-1]
            squareroot24_num_weak_links.append(int(val)) 
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            squareroot24_serial_perf.append(int(val)/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            squareroot24_parallel_perf.append(int(val)/1000) 

squareroot24_max_serial = max(squareroot24_serial_perf)
squareroot24_min_serial = min(squareroot24_serial_perf)
squareroot24_max_parallel = max(squareroot24_parallel_perf)
squareroot24_min_parallel = min(squareroot24_parallel_perf)
squareroot24_avg_serial = sum(squareroot24_serial_perf)/len(squareroot24_serial_perf)
squareroot24_avg_parallel = sum(squareroot24_parallel_perf)/len(squareroot24_parallel_perf)
print(squareroot24_num_weak_links)


# squareroot32
with open('squareroot32.out') as file:
    for line in file:
        if 'Number of weak links:' in line:
            val = line.rstrip().split(":")[-1]
            squareroot32_num_weak_links.append(int(val)) 
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            squareroot32_serial_perf.append(int(val)/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            squareroot32_parallel_perf.append(int(val)/1000) 

squareroot32_max_serial = max(squareroot32_serial_perf)
squareroot32_min_serial = min(squareroot32_serial_perf)
squareroot32_max_parallel = max(squareroot32_parallel_perf)
squareroot32_min_parallel = min(squareroot32_parallel_perf)
squareroot32_avg_serial = sum(squareroot32_serial_perf)/len(squareroot32_serial_perf)
squareroot32_avg_parallel = sum(squareroot32_parallel_perf)/len(squareroot32_parallel_perf)
print(squareroot32_num_weak_links)


# qft8
with open('qft8.out') as file:
    for line in file:
        if 'Number of weak links:' in line:
            val = line.rstrip().split(":")[-1]
            qft8_num_weak_links.append(int(val)) 
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qft8_serial_perf.append(int(val)/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qft8_parallel_perf.append(int(val)/1000) 

qft8_max_serial = max(qft8_serial_perf)
qft8_min_serial = min(qft8_serial_perf)
qft8_max_parallel = max(qft8_parallel_perf)
qft8_min_parallel = min(qft8_parallel_perf)
qft8_avg_serial = sum(qft8_serial_perf)/len(qft8_serial_perf)
qft8_avg_parallel = sum(qft8_parallel_perf)/len(qft8_parallel_perf)
print(qft8_num_weak_links)


# qft16
with open('qft16.out') as file:
    for line in file:
        if 'Number of weak links:' in line:
            val = line.rstrip().split(":")[-1]
            qft16_num_weak_links.append(int(val)) 
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qft16_serial_perf.append(int(val)/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qft16_parallel_perf.append(int(val)/1000) 

qft16_max_serial = max(qft16_serial_perf)
qft16_min_serial = min(qft16_serial_perf)
qft16_max_parallel = max(qft16_parallel_perf)
qft16_min_parallel = min(qft16_parallel_perf)
qft16_avg_serial = sum(qft16_serial_perf)/len(qft16_serial_perf)
qft16_avg_parallel = sum(qft16_parallel_perf)/len(qft16_parallel_perf)
print(qft16_num_weak_links)


# qft24
with open('qft24.out') as file:
    for line in file:
        if 'Number of weak links:' in line:
            val = line.rstrip().split(":")[-1]
            qft24_num_weak_links.append(int(val)) 
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qft24_serial_perf.append(int(val)/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qft24_parallel_perf.append(int(val)/1000) 

qft24_max_serial = max(qft24_serial_perf)
qft24_min_serial = min(qft24_serial_perf)
qft24_max_parallel = max(qft24_parallel_perf)
qft24_min_parallel = min(qft24_parallel_perf)
qft24_avg_serial = sum(qft24_serial_perf)/len(qft24_serial_perf)
qft24_avg_parallel = sum(qft24_parallel_perf)/len(qft24_parallel_perf)
print(qft24_num_weak_links)


# qft32
with open('qft32.out') as file:
    for line in file:
        if 'Number of weak links:' in line:
            val = line.rstrip().split(":")[-1]
            qft32_num_weak_links.append(int(val)) 
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qft32_serial_perf.append(int(val)/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qft32_parallel_perf.append(int(val)/1000) 

qft32_max_serial = max(qft32_serial_perf)
qft32_min_serial = min(qft32_serial_perf)
qft32_max_parallel = max(qft32_parallel_perf)
qft32_min_parallel = min(qft32_parallel_perf)
qft32_avg_serial = sum(qft32_serial_perf)/len(qft32_serial_perf)
qft32_avg_parallel = sum(qft32_parallel_perf)/len(qft32_parallel_perf)
print(qft32_num_weak_links)


# adder8
with open('adder8.out') as file:
    for line in file:
        if 'Number of weak links:' in line:
            val = line.rstrip().split(":")[-1]
            adder8_num_weak_links.append(int(val)) 
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            adder8_serial_perf.append(int(val)/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            adder8_parallel_perf.append(int(val)/1000) 

adder8_max_serial = max(adder8_serial_perf)
adder8_min_serial = min(adder8_serial_perf)
adder8_max_parallel = max(adder8_parallel_perf)
adder8_min_parallel = min(adder8_parallel_perf)
adder8_avg_serial = sum(adder8_serial_perf)/len(adder8_serial_perf)
adder8_avg_parallel = sum(adder8_parallel_perf)/len(adder8_parallel_perf)
print(adder8_num_weak_links)


# adder16
with open('adder16.out') as file:
    for line in file:
        if 'Number of weak links:' in line:
            val = line.rstrip().split(":")[-1]
            adder16_num_weak_links.append(int(val)) 
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            adder16_serial_perf.append(int(val)/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            adder16_parallel_perf.append(int(val)/1000) 

adder16_max_serial = max(adder16_serial_perf)
adder16_min_serial = min(adder16_serial_perf)
adder16_max_parallel = max(adder16_parallel_perf)
adder16_min_parallel = min(adder16_parallel_perf)
adder16_avg_serial = sum(adder16_serial_perf)/len(adder16_serial_perf)
adder16_avg_parallel = sum(adder16_parallel_perf)/len(adder16_parallel_perf)
print(adder16_num_weak_links)


# adder24
with open('adder24.out') as file:
    for line in file:
        if 'Number of weak links:' in line:
            val = line.rstrip().split(":")[-1]
            adder24_num_weak_links.append(int(val)) 
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            adder24_serial_perf.append(int(val)/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            adder24_parallel_perf.append(int(val)/1000) 

adder24_max_serial = max(adder24_serial_perf)
adder24_min_serial = min(adder24_serial_perf)
adder24_max_parallel = max(adder24_parallel_perf)
adder24_min_parallel = min(adder24_parallel_perf)
adder24_avg_serial = sum(adder24_serial_perf)/len(adder24_serial_perf)
adder24_avg_parallel = sum(adder24_parallel_perf)/len(adder24_parallel_perf)
print(adder24_num_weak_links)


# adder32
with open('adder32.out') as file:
    for line in file:
        if 'Number of weak links:' in line:
            val = line.rstrip().split(":")[-1]
            adder32_num_weak_links.append(int(val)) 
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            adder32_serial_perf.append(int(val)/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            adder32_parallel_perf.append(int(val)/1000) 

adder32_max_serial = max(adder32_serial_perf)
adder32_min_serial = min(adder32_serial_perf)
adder32_max_parallel = max(adder32_parallel_perf)
adder32_min_parallel = min(adder32_parallel_perf)
adder32_avg_serial = sum(adder32_serial_perf)/len(adder32_serial_perf)
adder32_avg_parallel = sum(adder32_parallel_perf)/len(adder32_parallel_perf)
print(adder32_num_weak_links)


# bv8
with open('bv8.out') as file:
    for line in file:
        if 'Number of weak links:' in line:
            val = line.rstrip().split(":")[-1]
            bv8_num_weak_links.append(int(val)) 
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            bv8_serial_perf.append(int(val)/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            bv8_parallel_perf.append(int(val)/1000) 

bv8_max_serial = max(bv8_serial_perf)
bv8_min_serial = min(bv8_serial_perf)
bv8_max_parallel = max(bv8_parallel_perf)
bv8_min_parallel = min(bv8_parallel_perf)
bv8_avg_serial = sum(bv8_serial_perf)/len(bv8_serial_perf)
bv8_avg_parallel = sum(bv8_parallel_perf)/len(bv8_parallel_perf)
print(bv8_num_weak_links)


# bv16
with open('bv16.out') as file:
    for line in file:
        if 'Number of weak links:' in line:
            val = line.rstrip().split(":")[-1]
            bv16_num_weak_links.append(int(val)) 
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            bv16_serial_perf.append(int(val)/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            bv16_parallel_perf.append(int(val)/1000) 

bv16_max_serial = max(bv16_serial_perf)
bv16_min_serial = min(bv16_serial_perf)
bv16_max_parallel = max(bv16_parallel_perf)
bv16_min_parallel = min(bv16_parallel_perf)
bv16_avg_serial = sum(bv16_serial_perf)/len(bv16_serial_perf)
bv16_avg_parallel = sum(bv16_parallel_perf)/len(bv16_parallel_perf)
print(bv16_num_weak_links)


# bv24
with open('bv24.out') as file:
    for line in file:
        if 'Number of weak links:' in line:
            val = line.rstrip().split(":")[-1]
            bv24_num_weak_links.append(int(val)) 
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            bv24_serial_perf.append(int(val)/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            bv24_parallel_perf.append(int(val)/1000) 

bv24_max_serial = max(bv24_serial_perf)
bv24_min_serial = min(bv24_serial_perf)
bv24_max_parallel = max(bv24_parallel_perf)
bv24_min_parallel = min(bv24_parallel_perf)
bv24_avg_serial = sum(bv24_serial_perf)/len(bv24_serial_perf)
bv24_avg_parallel = sum(bv24_parallel_perf)/len(bv24_parallel_perf)
print(bv24_num_weak_links)


# bv32
with open('bv32.out') as file:
    for line in file:
        if 'Number of weak links:' in line:
            val = line.rstrip().split(":")[-1]
            bv32_num_weak_links.append(int(val)) 
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            bv32_serial_perf.append(int(val)/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            bv32_parallel_perf.append(int(val)/1000) 

bv32_max_serial = max(bv32_serial_perf)
bv32_min_serial = min(bv32_serial_perf)
bv32_max_parallel = max(bv32_parallel_perf)
bv32_min_parallel = min(bv32_parallel_perf)
bv32_avg_serial = sum(bv32_serial_perf)/len(bv32_serial_perf)
bv32_avg_parallel = sum(bv32_parallel_perf)/len(bv32_parallel_perf)
print(bv32_num_weak_links)


# setup the dataframe
#Num_weak_links = ['8', '4', '3', '2', '8', '4', '3', '2']
#Num_weak_links = ['8', '16', '24', '32', '8', '4', '3', '2']
Applications = ['Supremacy', 'Supremacy', 'Supremacy', 'Supremacy', 'QAOA', 'QAOA', 'QAOA', 'QAOA', 'SquareRoot', 'SquareRoot', 'SquareRoot', 'SquareRoot', 'QFT', 'QFT', 'QFT', 'QFT', 'Adder', 'Adder', 'Adder', 'Adder', 'BV', 'BV', 'BV', 'BV', 'geomean', 'geomean', 'geomean', 'geomean']

geomean8_parallel = gmean([supremacy8_avg_parallel, qaoa8_avg_parallel, squareroot8_avg_parallel, qft8_avg_parallel, adder8_avg_parallel, bv8_avg_parallel])
geomean16_parallel = gmean([supremacy16_avg_parallel, qaoa16_avg_parallel, squareroot16_avg_parallel, qft16_avg_parallel, adder16_avg_parallel, bv16_avg_parallel])
geomean24_parallel = gmean([supremacy24_avg_parallel, qaoa24_avg_parallel, squareroot24_avg_parallel, qft24_avg_parallel, adder24_avg_parallel, bv24_avg_parallel])
geomean32_parallel = gmean([supremacy32_avg_parallel, qaoa32_avg_parallel, squareroot32_avg_parallel, qft32_avg_parallel, adder32_avg_parallel, bv32_avg_parallel])

Performance = [supremacy8_avg_parallel, supremacy16_avg_parallel,supremacy24_avg_parallel, supremacy32_avg_parallel, qaoa8_avg_parallel, qaoa16_avg_parallel, qaoa24_avg_parallel, qaoa32_avg_parallel, squareroot8_avg_parallel, squareroot16_avg_parallel, squareroot24_avg_parallel, squareroot32_avg_parallel, qft8_avg_parallel, qft16_avg_parallel, qft24_avg_parallel, qft32_avg_parallel, adder8_avg_parallel, adder16_avg_parallel, adder24_avg_parallel, adder32_avg_parallel, bv8_avg_parallel, bv16_avg_parallel, bv24_avg_parallel, bv32_avg_parallel, geomean8_parallel, geomean16_parallel, geomean24_parallel, geomean32_parallel]

Chain_length = ['8', '16', '24', '32', '8', '16', '24', '32', '8', '16', '24', '32', '8', '16', '24', '32', '8', '16', '24', '32', '8', '16', '24', '32', '8', '16', '24', '32']

df = pd.DataFrame({'':Applications,'Execution Time [ms]':Performance, 'Chain length':Chain_length})

print(df)

error = {
supremacy8_avg_parallel: {'max': supremacy8_max_parallel,'min': supremacy8_min_parallel}, supremacy16_avg_parallel: {'max': supremacy16_max_parallel,'min': supremacy16_min_parallel}, supremacy24_avg_parallel: {'max': supremacy24_max_parallel,'min': supremacy24_min_parallel}, supremacy32_avg_parallel: {'max': supremacy32_max_parallel,'min': supremacy32_min_parallel}, qaoa8_avg_parallel: {'max': qaoa8_max_parallel,'min': qaoa8_min_parallel}, qaoa16_avg_parallel: {'max': qaoa16_max_parallel,'min': qaoa16_min_parallel}, qaoa24_avg_parallel: {'max': qaoa24_max_parallel,'min': qaoa24_min_parallel}, qaoa32_avg_parallel: {'max': qaoa32_max_parallel,'min': qaoa32_min_parallel}, squareroot8_avg_parallel: {'max': squareroot8_max_parallel,'min': squareroot8_min_parallel}, squareroot16_avg_parallel: {'max': squareroot16_max_parallel,'min': squareroot16_min_parallel}, squareroot24_avg_parallel: {'max': squareroot24_max_parallel,'min': squareroot24_min_parallel}, squareroot32_avg_parallel: {'max': squareroot32_max_parallel,'min': squareroot32_min_parallel}, qft8_avg_parallel: {'max': qft8_max_parallel,'min': qft8_min_parallel}, qft16_avg_parallel: {'max': qft16_max_parallel,'min': qft16_min_parallel}, qft24_avg_parallel: {'max': qft24_max_parallel,'min': qft24_min_parallel}, qft32_avg_parallel: {'max': qft32_max_parallel,'min': qft32_min_parallel}, adder8_avg_parallel: {'max': adder8_max_parallel,'min': adder8_min_parallel}, adder16_avg_parallel: {'max': adder16_max_parallel,'min': adder16_min_parallel}, adder24_avg_parallel: {'max': adder24_max_parallel,'min': adder24_min_parallel}, adder32_avg_parallel: {'max': adder32_max_parallel,'min': adder32_min_parallel}, bv8_avg_parallel: {'max': bv8_max_parallel,'min': bv8_min_parallel}, bv16_avg_parallel: {'max': bv16_max_parallel,'min': bv16_min_parallel}, bv24_avg_parallel: {'max': bv24_max_parallel,'min': bv24_min_parallel}, bv32_avg_parallel: {'max': bv32_max_parallel,'min': bv32_min_parallel}, geomean8_parallel: {'max': 0,'min': 0}, geomean16_parallel: {'max': 0,'min': 0}, geomean24_parallel: {'max': 0,'min': 0}, geomean32_parallel: {'max': 0,'min': 0}}

# plot the figure
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x='', y='Execution Time [ms]', hue='Chain length', data=df, ax=ax)

#plt.title('Supremacy')
#plt.ylim(0, 13)
plt.xticks(rotation = 45)
plt.ylim(0, 30)

# add the lines for the errors 
for p in ax.patches:
    x = p.get_x()  # get the bottom left x corner of the bar
    w = p.get_width()  # get width of bar
    h = p.get_height()  # get height of bar
    min_y = error[h]['min']  # use h to get min from dict z
    max_y = error[h]['max']  # use h to get max from dict z
    plt.vlines(x+w/2, min_y, max_y, color='k')  # draw a vertical line

#plt.show()
fig.savefig('chain_sweep.png', bbox_inches='tight')
