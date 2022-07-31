import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

random2wl2_8_serial_perf = []
random2wl2_28_serial_perf = []
random2wl2_48_serial_perf = []
random2wl2_68_serial_perf = []
random2wl2_88_serial_perf = []
random2wl2_108_serial_perf = []
random2wl2_128_serial_perf = []
random2wl2_8_parallel_perf = []
random2wl2_28_parallel_perf = []
random2wl2_48_parallel_perf = []
random2wl2_68_parallel_perf = []
random2wl2_88_parallel_perf = []
random2wl2_108_parallel_perf = []
random2wl2_128_parallel_perf = []

random2wl2_error_serial_perf = []
random2wl2_error_parallel_perf = []

random2wl1_8_8_serial_perf = []
random2wl1_8_28_serial_perf = []
random2wl1_8_48_serial_perf = []
random2wl1_8_68_serial_perf = []
random2wl1_8_88_serial_perf = []
random2wl1_8_108_serial_perf = []
random2wl1_8_128_serial_perf = []
random2wl1_8_8_parallel_perf = []
random2wl1_8_28_parallel_perf = []
random2wl1_8_48_parallel_perf = []
random2wl1_8_68_parallel_perf = []
random2wl1_8_88_parallel_perf = []
random2wl1_8_108_parallel_perf = []
random2wl1_8_128_parallel_perf = []

random2wl1_8_error_serial_perf = []
random2wl1_8_error_parallel_perf = []

random2wl1_6_8_serial_perf = []
random2wl1_6_28_serial_perf = []
random2wl1_6_48_serial_perf = []
random2wl1_6_68_serial_perf = []
random2wl1_6_88_serial_perf = []
random2wl1_6_108_serial_perf = []
random2wl1_6_128_serial_perf = []
random2wl1_6_8_parallel_perf = []
random2wl1_6_28_parallel_perf = []
random2wl1_6_48_parallel_perf = []
random2wl1_6_68_parallel_perf = []
random2wl1_6_88_parallel_perf = []
random2wl1_6_108_parallel_perf = []
random2wl1_6_128_parallel_perf = []

random2wl1_6_error_serial_perf = []
random2wl1_6_error_parallel_perf = []

random2wl1_4_8_serial_perf = []
random2wl1_4_28_serial_perf = []
random2wl1_4_48_serial_perf = []
random2wl1_4_68_serial_perf = []
random2wl1_4_88_serial_perf = []
random2wl1_4_108_serial_perf = []
random2wl1_4_128_serial_perf = []
random2wl1_4_8_parallel_perf = []
random2wl1_4_28_parallel_perf = []
random2wl1_4_48_parallel_perf = []
random2wl1_4_68_parallel_perf = []
random2wl1_4_88_parallel_perf = []
random2wl1_4_108_parallel_perf = []
random2wl1_4_128_parallel_perf = []

random2wl1_4_error_serial_perf = []
random2wl1_4_error_parallel_perf = []

random2wl1_2_8_serial_perf = []
random2wl1_2_28_serial_perf = []
random2wl1_2_48_serial_perf = []
random2wl1_2_68_serial_perf = []
random2wl1_2_88_serial_perf = []
random2wl1_2_108_serial_perf = []
random2wl1_2_128_serial_perf = []
random2wl1_2_8_parallel_perf = []
random2wl1_2_28_parallel_perf = []
random2wl1_2_48_parallel_perf = []
random2wl1_2_68_parallel_perf = []
random2wl1_2_88_parallel_perf = []
random2wl1_2_108_parallel_perf = []
random2wl1_2_128_parallel_perf = []

random2wl1_2_error_serial_perf = []
random2wl1_2_error_parallel_perf = []

random2wl1_8_serial_perf = []
random2wl1_28_serial_perf = []
random2wl1_48_serial_perf = []
random2wl1_68_serial_perf = []
random2wl1_88_serial_perf = []
random2wl1_108_serial_perf = []
random2wl1_128_serial_perf = []
random2wl1_8_parallel_perf = []
random2wl1_28_parallel_perf = []
random2wl1_48_parallel_perf = []
random2wl1_68_parallel_perf = []
random2wl1_88_parallel_perf = []
random2wl1_108_parallel_perf = []
random2wl1_128_parallel_perf = []

random2wl1_error_serial_perf = []
random2wl1_error_parallel_perf = []

# random28
with open('random2_32_8_wl2.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl2_8_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl2_8_parallel_perf.append(int(float(val))/1000) 

random2wl2_8_max_serial = max(random2wl2_8_serial_perf)
random2wl2_8_min_serial = min(random2wl2_8_serial_perf)
random2wl2_8_max_parallel = max(random2wl2_8_parallel_perf)
random2wl2_8_min_parallel = min(random2wl2_8_parallel_perf)
random2wl2_8_avg_serial = sum(random2wl2_8_serial_perf)/len(random2wl2_8_serial_perf)
random2wl2_8_avg_parallel = sum(random2wl2_8_parallel_perf)/len(random2wl2_8_parallel_perf)

# random228
with open('random2_32_28_wl2.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl2_28_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl2_28_parallel_perf.append(int(float(val))/1000) 

random2wl2_28_max_serial = max(random2wl2_28_serial_perf)
random2wl2_28_min_serial = min(random2wl2_28_serial_perf)
random2wl2_28_max_parallel = max(random2wl2_28_parallel_perf)
random2wl2_28_min_parallel = min(random2wl2_28_parallel_perf)
random2wl2_28_avg_serial = sum(random2wl2_28_serial_perf)/len(random2wl2_28_serial_perf)
random2wl2_28_avg_parallel = sum(random2wl2_28_parallel_perf)/len(random2wl2_28_parallel_perf)

# random2wl1_6
with open('random2_32_48_wl2.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl2_48_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl2_48_parallel_perf.append(int(float(val))/1000) 

random2wl2_48_max_serial = max(random2wl2_48_serial_perf)
random2wl2_48_min_serial = min(random2wl2_48_serial_perf)
random2wl2_48_max_parallel = max(random2wl2_48_parallel_perf)
random2wl2_48_min_parallel = min(random2wl2_48_parallel_perf)
random2wl2_48_avg_serial = sum(random2wl2_48_serial_perf)/len(random2wl2_48_serial_perf)
random2wl2_48_avg_parallel = sum(random2wl2_48_parallel_perf)/len(random2wl2_48_parallel_perf)

# random268
with open('random2_32_68_wl2.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl2_68_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl2_68_parallel_perf.append(int(float(val))/1000) 

random2wl2_68_max_serial = max(random2wl2_68_serial_perf)
random2wl2_68_min_serial = min(random2wl2_68_serial_perf)
random2wl2_68_max_parallel = max(random2wl2_68_parallel_perf)
random2wl2_68_min_parallel = min(random2wl2_68_parallel_perf)
random2wl2_68_avg_serial = sum(random2wl2_68_serial_perf)/len(random2wl2_68_serial_perf)
random2wl2_68_avg_parallel = sum(random2wl2_68_parallel_perf)/len(random2wl2_68_parallel_perf)

# random288
with open('random2_32_88_wl2.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl2_88_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl2_88_parallel_perf.append(int(float(val))/1000) 

random2wl2_88_max_serial = max(random2wl2_88_serial_perf)
random2wl2_88_min_serial = min(random2wl2_88_serial_perf)
random2wl2_88_max_parallel = max(random2wl2_88_parallel_perf)
random2wl2_88_min_parallel = min(random2wl2_88_parallel_perf)
random2wl2_88_avg_serial = sum(random2wl2_88_serial_perf)/len(random2wl2_88_serial_perf)
random2wl2_88_avg_parallel = sum(random2wl2_88_parallel_perf)/len(random2wl2_88_parallel_perf)

# random2108
with open('random2_32_108_wl2.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl2_108_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl2_108_parallel_perf.append(int(float(val))/1000) 

random2wl2_108_max_serial = max(random2wl2_108_serial_perf)
random2wl2_108_min_serial = min(random2wl2_108_serial_perf)
random2wl2_108_max_parallel = max(random2wl2_108_parallel_perf)
random2wl2_108_min_parallel = min(random2wl2_108_parallel_perf)
random2wl2_108_avg_serial = sum(random2wl2_108_serial_perf)/len(random2wl2_108_serial_perf)
random2wl2_108_avg_parallel = sum(random2wl2_108_parallel_perf)/len(random2wl2_108_parallel_perf)

# random2128
with open('random2_32_128_wl2.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl2_128_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl2_128_parallel_perf.append(int(float(val))/1000) 

random2wl2_128_max_serial = max(random2wl2_128_serial_perf)
random2wl2_128_min_serial = min(random2wl2_128_serial_perf)
random2wl2_128_max_parallel = max(random2wl2_128_parallel_perf)
random2wl2_128_min_parallel = min(random2wl2_128_parallel_perf)
random2wl2_128_avg_serial = sum(random2wl2_128_serial_perf)/len(random2wl2_128_serial_perf)
random2wl2_128_avg_parallel = sum(random2wl2_128_parallel_perf)/len(random2wl2_128_parallel_perf)


# random28
with open('random2_32_8_wl1.8.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_8_8_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_8_8_parallel_perf.append(int(float(val))/1000) 

random2wl1_8_8_max_serial = max(random2wl1_8_8_serial_perf)
random2wl1_8_8_min_serial = min(random2wl1_8_8_serial_perf)
random2wl1_8_8_max_parallel = max(random2wl1_8_8_parallel_perf)
random2wl1_8_8_min_parallel = min(random2wl1_8_8_parallel_perf)
random2wl1_8_8_avg_serial = sum(random2wl1_8_8_serial_perf)/len(random2wl1_8_8_serial_perf)
random2wl1_8_8_avg_parallel = sum(random2wl1_8_8_parallel_perf)/len(random2wl1_8_8_parallel_perf)

# random228
with open('random2_32_28_wl1.8.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_8_28_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_8_28_parallel_perf.append(int(float(val))/1000) 

random2wl1_8_28_max_serial = max(random2wl1_8_28_serial_perf)
random2wl1_8_28_min_serial = min(random2wl1_8_28_serial_perf)
random2wl1_8_28_max_parallel = max(random2wl1_8_28_parallel_perf)
random2wl1_8_28_min_parallel = min(random2wl1_8_28_parallel_perf)
random2wl1_8_28_avg_serial = sum(random2wl1_8_28_serial_perf)/len(random2wl1_8_28_serial_perf)
random2wl1_8_28_avg_parallel = sum(random2wl1_8_28_parallel_perf)/len(random2wl1_8_28_parallel_perf)

# random2wl1_6
with open('random2_32_48_wl1.8.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_8_48_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_8_48_parallel_perf.append(int(float(val))/1000) 

random2wl1_8_48_max_serial = max(random2wl1_8_48_serial_perf)
random2wl1_8_48_min_serial = min(random2wl1_8_48_serial_perf)
random2wl1_8_48_max_parallel = max(random2wl1_8_48_parallel_perf)
random2wl1_8_48_min_parallel = min(random2wl1_8_48_parallel_perf)
random2wl1_8_48_avg_serial = sum(random2wl1_8_48_serial_perf)/len(random2wl1_8_48_serial_perf)
random2wl1_8_48_avg_parallel = sum(random2wl1_8_48_parallel_perf)/len(random2wl1_8_48_parallel_perf)

# random268
with open('random2_32_68_wl1.8.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_8_68_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_8_68_parallel_perf.append(int(float(val))/1000) 

random2wl1_8_68_max_serial = max(random2wl1_8_68_serial_perf)
random2wl1_8_68_min_serial = min(random2wl1_8_68_serial_perf)
random2wl1_8_68_max_parallel = max(random2wl1_8_68_parallel_perf)
random2wl1_8_68_min_parallel = min(random2wl1_8_68_parallel_perf)
random2wl1_8_68_avg_serial = sum(random2wl1_8_68_serial_perf)/len(random2wl1_8_68_serial_perf)
random2wl1_8_68_avg_parallel = sum(random2wl1_8_68_parallel_perf)/len(random2wl1_8_68_parallel_perf)

# random288
with open('random2_32_88_wl1.8.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_8_88_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_8_88_parallel_perf.append(int(float(val))/1000) 

random2wl1_8_88_max_serial = max(random2wl1_8_88_serial_perf)
random2wl1_8_88_min_serial = min(random2wl1_8_88_serial_perf)
random2wl1_8_88_max_parallel = max(random2wl1_8_88_parallel_perf)
random2wl1_8_88_min_parallel = min(random2wl1_8_88_parallel_perf)
random2wl1_8_88_avg_serial = sum(random2wl1_8_88_serial_perf)/len(random2wl1_8_88_serial_perf)
random2wl1_8_88_avg_parallel = sum(random2wl1_8_88_parallel_perf)/len(random2wl1_8_88_parallel_perf)

# random2108
with open('random2_32_108_wl1.8.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_8_108_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_8_108_parallel_perf.append(int(float(val))/1000) 

random2wl1_8_108_max_serial = max(random2wl1_8_108_serial_perf)
random2wl1_8_108_min_serial = min(random2wl1_8_108_serial_perf)
random2wl1_8_108_max_parallel = max(random2wl1_8_108_parallel_perf)
random2wl1_8_108_min_parallel = min(random2wl1_8_108_parallel_perf)
random2wl1_8_108_avg_serial = sum(random2wl1_8_108_serial_perf)/len(random2wl1_8_108_serial_perf)
random2wl1_8_108_avg_parallel = sum(random2wl1_8_108_parallel_perf)/len(random2wl1_8_108_parallel_perf)

# random2128
with open('random2_32_128_wl1.8.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_8_128_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_8_128_parallel_perf.append(int(float(val))/1000) 

random2wl1_8_128_max_serial = max(random2wl1_8_128_serial_perf)
random2wl1_8_128_min_serial = min(random2wl1_8_128_serial_perf)
random2wl1_8_128_max_parallel = max(random2wl1_8_128_parallel_perf)
random2wl1_8_128_min_parallel = min(random2wl1_8_128_parallel_perf)
random2wl1_8_128_avg_serial = sum(random2wl1_8_128_serial_perf)/len(random2wl1_8_128_serial_perf)
random2wl1_8_128_avg_parallel = sum(random2wl1_8_128_parallel_perf)/len(random2wl1_8_128_parallel_perf)


# random28
with open('random2_32_8_wl1.6.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_6_8_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_6_8_parallel_perf.append(int(float(val))/1000) 

random2wl1_6_8_max_serial = max(random2wl1_6_8_serial_perf)
random2wl1_6_8_min_serial = min(random2wl1_6_8_serial_perf)
random2wl1_6_8_max_parallel = max(random2wl1_6_8_parallel_perf)
random2wl1_6_8_min_parallel = min(random2wl1_6_8_parallel_perf)
random2wl1_6_8_avg_serial = sum(random2wl1_6_8_serial_perf)/len(random2wl1_6_8_serial_perf)
random2wl1_6_8_avg_parallel = sum(random2wl1_6_8_parallel_perf)/len(random2wl1_6_8_parallel_perf)

# random228
with open('random2_32_28_wl1.6.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_6_28_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_6_28_parallel_perf.append(int(float(val))/1000) 

random2wl1_6_28_max_serial = max(random2wl1_6_28_serial_perf)
random2wl1_6_28_min_serial = min(random2wl1_6_28_serial_perf)
random2wl1_6_28_max_parallel = max(random2wl1_6_28_parallel_perf)
random2wl1_6_28_min_parallel = min(random2wl1_6_28_parallel_perf)
random2wl1_6_28_avg_serial = sum(random2wl1_6_28_serial_perf)/len(random2wl1_6_28_serial_perf)
random2wl1_6_28_avg_parallel = sum(random2wl1_6_28_parallel_perf)/len(random2wl1_6_28_parallel_perf)

# random2wl1_6
with open('random2_32_48_wl1.6.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_6_48_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_6_48_parallel_perf.append(int(float(val))/1000) 

random2wl1_6_48_max_serial = max(random2wl1_6_48_serial_perf)
random2wl1_6_48_min_serial = min(random2wl1_6_48_serial_perf)
random2wl1_6_48_max_parallel = max(random2wl1_6_48_parallel_perf)
random2wl1_6_48_min_parallel = min(random2wl1_6_48_parallel_perf)
random2wl1_6_48_avg_serial = sum(random2wl1_6_48_serial_perf)/len(random2wl1_6_48_serial_perf)
random2wl1_6_48_avg_parallel = sum(random2wl1_6_48_parallel_perf)/len(random2wl1_6_48_parallel_perf)

# random268
with open('random2_32_68_wl1.6.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_6_68_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_6_68_parallel_perf.append(int(float(val))/1000) 

random2wl1_6_68_max_serial = max(random2wl1_6_68_serial_perf)
random2wl1_6_68_min_serial = min(random2wl1_6_68_serial_perf)
random2wl1_6_68_max_parallel = max(random2wl1_6_68_parallel_perf)
random2wl1_6_68_min_parallel = min(random2wl1_6_68_parallel_perf)
random2wl1_6_68_avg_serial = sum(random2wl1_6_68_serial_perf)/len(random2wl1_6_68_serial_perf)
random2wl1_6_68_avg_parallel = sum(random2wl1_6_68_parallel_perf)/len(random2wl1_6_68_parallel_perf)

# random288
with open('random2_32_88_wl1.6.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_6_88_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_6_88_parallel_perf.append(int(float(val))/1000) 

random2wl1_6_88_max_serial = max(random2wl1_6_88_serial_perf)
random2wl1_6_88_min_serial = min(random2wl1_6_88_serial_perf)
random2wl1_6_88_max_parallel = max(random2wl1_6_88_parallel_perf)
random2wl1_6_88_min_parallel = min(random2wl1_6_88_parallel_perf)
random2wl1_6_88_avg_serial = sum(random2wl1_6_88_serial_perf)/len(random2wl1_6_88_serial_perf)
random2wl1_6_88_avg_parallel = sum(random2wl1_6_88_parallel_perf)/len(random2wl1_6_88_parallel_perf)

# random2108
with open('random2_32_108_wl1.6.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_6_108_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_6_108_parallel_perf.append(int(float(val))/1000) 

random2wl1_6_108_max_serial = max(random2wl1_6_108_serial_perf)
random2wl1_6_108_min_serial = min(random2wl1_6_108_serial_perf)
random2wl1_6_108_max_parallel = max(random2wl1_6_108_parallel_perf)
random2wl1_6_108_min_parallel = min(random2wl1_6_108_parallel_perf)
random2wl1_6_108_avg_serial = sum(random2wl1_6_108_serial_perf)/len(random2wl1_6_108_serial_perf)
random2wl1_6_108_avg_parallel = sum(random2wl1_6_108_parallel_perf)/len(random2wl1_6_108_parallel_perf)

# random2128
with open('random2_32_128_wl1.6.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_6_128_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_6_128_parallel_perf.append(int(float(val))/1000) 

random2wl1_6_128_max_serial = max(random2wl1_6_128_serial_perf)
random2wl1_6_128_min_serial = min(random2wl1_6_128_serial_perf)
random2wl1_6_128_max_parallel = max(random2wl1_6_128_parallel_perf)
random2wl1_6_128_min_parallel = min(random2wl1_6_128_parallel_perf)
random2wl1_6_128_avg_serial = sum(random2wl1_6_128_serial_perf)/len(random2wl1_6_128_serial_perf)
random2wl1_6_128_avg_parallel = sum(random2wl1_6_128_parallel_perf)/len(random2wl1_6_128_parallel_perf)


# random28
with open('random2_32_8_wl1.4.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_4_8_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_4_8_parallel_perf.append(int(float(val))/1000) 

random2wl1_4_8_max_serial = max(random2wl1_4_8_serial_perf)
random2wl1_4_8_min_serial = min(random2wl1_4_8_serial_perf)
random2wl1_4_8_max_parallel = max(random2wl1_4_8_parallel_perf)
random2wl1_4_8_min_parallel = min(random2wl1_4_8_parallel_perf)
random2wl1_4_8_avg_serial = sum(random2wl1_4_8_serial_perf)/len(random2wl1_4_8_serial_perf)
random2wl1_4_8_avg_parallel = sum(random2wl1_4_8_parallel_perf)/len(random2wl1_4_8_parallel_perf)

# random228
with open('random2_32_28_wl1.4.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_4_28_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_4_28_parallel_perf.append(int(float(val))/1000) 

random2wl1_4_28_max_serial = max(random2wl1_4_28_serial_perf)
random2wl1_4_28_min_serial = min(random2wl1_4_28_serial_perf)
random2wl1_4_28_max_parallel = max(random2wl1_4_28_parallel_perf)
random2wl1_4_28_min_parallel = min(random2wl1_4_28_parallel_perf)
random2wl1_4_28_avg_serial = sum(random2wl1_4_28_serial_perf)/len(random2wl1_4_28_serial_perf)
random2wl1_4_28_avg_parallel = sum(random2wl1_4_28_parallel_perf)/len(random2wl1_4_28_parallel_perf)

# random2wl1_6
with open('random2_32_48_wl1.4.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_4_48_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_4_48_parallel_perf.append(int(float(val))/1000) 

random2wl1_4_48_max_serial = max(random2wl1_4_48_serial_perf)
random2wl1_4_48_min_serial = min(random2wl1_4_48_serial_perf)
random2wl1_4_48_max_parallel = max(random2wl1_4_48_parallel_perf)
random2wl1_4_48_min_parallel = min(random2wl1_4_48_parallel_perf)
random2wl1_4_48_avg_serial = sum(random2wl1_4_48_serial_perf)/len(random2wl1_4_48_serial_perf)
random2wl1_4_48_avg_parallel = sum(random2wl1_4_48_parallel_perf)/len(random2wl1_4_48_parallel_perf)

# random268
with open('random2_32_68_wl1.4.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_4_68_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_4_68_parallel_perf.append(int(float(val))/1000) 

random2wl1_4_68_max_serial = max(random2wl1_4_68_serial_perf)
random2wl1_4_68_min_serial = min(random2wl1_4_68_serial_perf)
random2wl1_4_68_max_parallel = max(random2wl1_4_68_parallel_perf)
random2wl1_4_68_min_parallel = min(random2wl1_4_68_parallel_perf)
random2wl1_4_68_avg_serial = sum(random2wl1_4_68_serial_perf)/len(random2wl1_4_68_serial_perf)
random2wl1_4_68_avg_parallel = sum(random2wl1_4_68_parallel_perf)/len(random2wl1_4_68_parallel_perf)

# random288
with open('random2_32_88_wl1.4.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_4_88_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_4_88_parallel_perf.append(int(float(val))/1000) 

random2wl1_4_88_max_serial = max(random2wl1_4_88_serial_perf)
random2wl1_4_88_min_serial = min(random2wl1_4_88_serial_perf)
random2wl1_4_88_max_parallel = max(random2wl1_4_88_parallel_perf)
random2wl1_4_88_min_parallel = min(random2wl1_4_88_parallel_perf)
random2wl1_4_88_avg_serial = sum(random2wl1_4_88_serial_perf)/len(random2wl1_4_88_serial_perf)
random2wl1_4_88_avg_parallel = sum(random2wl1_4_88_parallel_perf)/len(random2wl1_4_88_parallel_perf)

# random2108
with open('random2_32_108_wl1.4.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_4_108_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_4_108_parallel_perf.append(int(float(val))/1000) 

random2wl1_4_108_max_serial = max(random2wl1_4_108_serial_perf)
random2wl1_4_108_min_serial = min(random2wl1_4_108_serial_perf)
random2wl1_4_108_max_parallel = max(random2wl1_4_108_parallel_perf)
random2wl1_4_108_min_parallel = min(random2wl1_4_108_parallel_perf)
random2wl1_4_108_avg_serial = sum(random2wl1_4_108_serial_perf)/len(random2wl1_4_108_serial_perf)
random2wl1_4_108_avg_parallel = sum(random2wl1_4_108_parallel_perf)/len(random2wl1_4_108_parallel_perf)

# random2128
with open('random2_32_128_wl1.4.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_4_128_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_4_128_parallel_perf.append(int(float(val))/1000) 

random2wl1_4_128_max_serial = max(random2wl1_4_128_serial_perf)
random2wl1_4_128_min_serial = min(random2wl1_4_128_serial_perf)
random2wl1_4_128_max_parallel = max(random2wl1_4_128_parallel_perf)
random2wl1_4_128_min_parallel = min(random2wl1_4_128_parallel_perf)
random2wl1_4_128_avg_serial = sum(random2wl1_4_128_serial_perf)/len(random2wl1_4_128_serial_perf)
random2wl1_4_128_avg_parallel = sum(random2wl1_4_128_parallel_perf)/len(random2wl1_4_128_parallel_perf)


# random28
with open('random2_32_8_wl1.2.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_2_8_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_2_8_parallel_perf.append(int(float(val))/1000) 

random2wl1_2_8_max_serial = max(random2wl1_2_8_serial_perf)
random2wl1_2_8_min_serial = min(random2wl1_2_8_serial_perf)
random2wl1_2_8_max_parallel = max(random2wl1_2_8_parallel_perf)
random2wl1_2_8_min_parallel = min(random2wl1_2_8_parallel_perf)
random2wl1_2_8_avg_serial = sum(random2wl1_2_8_serial_perf)/len(random2wl1_2_8_serial_perf)
random2wl1_2_8_avg_parallel = sum(random2wl1_2_8_parallel_perf)/len(random2wl1_2_8_parallel_perf)

# random228
with open('random2_32_28_wl1.2.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_2_28_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_2_28_parallel_perf.append(int(float(val))/1000) 

random2wl1_2_28_max_serial = max(random2wl1_2_28_serial_perf)
random2wl1_2_28_min_serial = min(random2wl1_2_28_serial_perf)
random2wl1_2_28_max_parallel = max(random2wl1_2_28_parallel_perf)
random2wl1_2_28_min_parallel = min(random2wl1_2_28_parallel_perf)
random2wl1_2_28_avg_serial = sum(random2wl1_2_28_serial_perf)/len(random2wl1_2_28_serial_perf)
random2wl1_2_28_avg_parallel = sum(random2wl1_2_28_parallel_perf)/len(random2wl1_2_28_parallel_perf)

# random2wl1_6
with open('random2_32_48_wl1.2.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_2_48_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_2_48_parallel_perf.append(int(float(val))/1000) 

random2wl1_2_48_max_serial = max(random2wl1_2_48_serial_perf)
random2wl1_2_48_min_serial = min(random2wl1_2_48_serial_perf)
random2wl1_2_48_max_parallel = max(random2wl1_2_48_parallel_perf)
random2wl1_2_48_min_parallel = min(random2wl1_2_48_parallel_perf)
random2wl1_2_48_avg_serial = sum(random2wl1_2_48_serial_perf)/len(random2wl1_2_48_serial_perf)
random2wl1_2_48_avg_parallel = sum(random2wl1_2_48_parallel_perf)/len(random2wl1_2_48_parallel_perf)

# random268
with open('random2_32_68_wl1.2.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_2_68_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_2_68_parallel_perf.append(int(float(val))/1000) 

random2wl1_2_68_max_serial = max(random2wl1_2_68_serial_perf)
random2wl1_2_68_min_serial = min(random2wl1_2_68_serial_perf)
random2wl1_2_68_max_parallel = max(random2wl1_2_68_parallel_perf)
random2wl1_2_68_min_parallel = min(random2wl1_2_68_parallel_perf)
random2wl1_2_68_avg_serial = sum(random2wl1_2_68_serial_perf)/len(random2wl1_2_68_serial_perf)
random2wl1_2_68_avg_parallel = sum(random2wl1_2_68_parallel_perf)/len(random2wl1_2_68_parallel_perf)

# random288
with open('random2_32_88_wl1.2.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_2_88_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_2_88_parallel_perf.append(int(float(val))/1000) 

random2wl1_2_88_max_serial = max(random2wl1_2_88_serial_perf)
random2wl1_2_88_min_serial = min(random2wl1_2_88_serial_perf)
random2wl1_2_88_max_parallel = max(random2wl1_2_88_parallel_perf)
random2wl1_2_88_min_parallel = min(random2wl1_2_88_parallel_perf)
random2wl1_2_88_avg_serial = sum(random2wl1_2_88_serial_perf)/len(random2wl1_2_88_serial_perf)
random2wl1_2_88_avg_parallel = sum(random2wl1_2_88_parallel_perf)/len(random2wl1_2_88_parallel_perf)

# random2108
with open('random2_32_108_wl1.2.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_2_108_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_2_108_parallel_perf.append(int(float(val))/1000) 

random2wl1_2_108_max_serial = max(random2wl1_2_108_serial_perf)
random2wl1_2_108_min_serial = min(random2wl1_2_108_serial_perf)
random2wl1_2_108_max_parallel = max(random2wl1_2_108_parallel_perf)
random2wl1_2_108_min_parallel = min(random2wl1_2_108_parallel_perf)
random2wl1_2_108_avg_serial = sum(random2wl1_2_108_serial_perf)/len(random2wl1_2_108_serial_perf)
random2wl1_2_108_avg_parallel = sum(random2wl1_2_108_parallel_perf)/len(random2wl1_2_108_parallel_perf)

# random2128
with open('random2_32_128_wl1.2.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_2_128_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_2_128_parallel_perf.append(int(float(val))/1000) 

random2wl1_2_128_max_serial = max(random2wl1_2_128_serial_perf)
random2wl1_2_128_min_serial = min(random2wl1_2_128_serial_perf)
random2wl1_2_128_max_parallel = max(random2wl1_2_128_parallel_perf)
random2wl1_2_128_min_parallel = min(random2wl1_2_128_parallel_perf)
random2wl1_2_128_avg_serial = sum(random2wl1_2_128_serial_perf)/len(random2wl1_2_128_serial_perf)
random2wl1_2_128_avg_parallel = sum(random2wl1_2_128_parallel_perf)/len(random2wl1_2_128_parallel_perf)


# random28
with open('random2_32_8_wl1.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_8_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_8_parallel_perf.append(int(float(val))/1000) 

random2wl1_8_max_serial = max(random2wl1_8_serial_perf)
random2wl1_8_min_serial = min(random2wl1_8_serial_perf)
random2wl1_8_max_parallel = max(random2wl1_8_parallel_perf)
random2wl1_8_min_parallel = min(random2wl1_8_parallel_perf)
random2wl1_8_avg_serial = sum(random2wl1_8_serial_perf)/len(random2wl1_8_serial_perf)
random2wl1_8_avg_parallel = sum(random2wl1_8_parallel_perf)/len(random2wl1_8_parallel_perf)

# random228
with open('random2_32_28_wl1.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_28_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_28_parallel_perf.append(int(float(val))/1000) 

random2wl1_28_max_serial = max(random2wl1_28_serial_perf)
random2wl1_28_min_serial = min(random2wl1_28_serial_perf)
random2wl1_28_max_parallel = max(random2wl1_28_parallel_perf)
random2wl1_28_min_parallel = min(random2wl1_28_parallel_perf)
random2wl1_28_avg_serial = sum(random2wl1_28_serial_perf)/len(random2wl1_28_serial_perf)
random2wl1_28_avg_parallel = sum(random2wl1_28_parallel_perf)/len(random2wl1_28_parallel_perf)

# random2wl1_6
with open('random2_32_48_wl1.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_48_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_48_parallel_perf.append(int(float(val))/1000) 

random2wl1_48_max_serial = max(random2wl1_48_serial_perf)
random2wl1_48_min_serial = min(random2wl1_48_serial_perf)
random2wl1_48_max_parallel = max(random2wl1_48_parallel_perf)
random2wl1_48_min_parallel = min(random2wl1_48_parallel_perf)
random2wl1_48_avg_serial = sum(random2wl1_48_serial_perf)/len(random2wl1_48_serial_perf)
random2wl1_48_avg_parallel = sum(random2wl1_48_parallel_perf)/len(random2wl1_48_parallel_perf)

# random268
with open('random2_32_68_wl1.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_68_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_68_parallel_perf.append(int(float(val))/1000) 

random2wl1_68_max_serial = max(random2wl1_68_serial_perf)
random2wl1_68_min_serial = min(random2wl1_68_serial_perf)
random2wl1_68_max_parallel = max(random2wl1_68_parallel_perf)
random2wl1_68_min_parallel = min(random2wl1_68_parallel_perf)
random2wl1_68_avg_serial = sum(random2wl1_68_serial_perf)/len(random2wl1_68_serial_perf)
random2wl1_68_avg_parallel = sum(random2wl1_68_parallel_perf)/len(random2wl1_68_parallel_perf)

# random288
with open('random2_32_88_wl1.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_88_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_88_parallel_perf.append(int(float(val))/1000) 

random2wl1_88_max_serial = max(random2wl1_88_serial_perf)
random2wl1_88_min_serial = min(random2wl1_88_serial_perf)
random2wl1_88_max_parallel = max(random2wl1_88_parallel_perf)
random2wl1_88_min_parallel = min(random2wl1_88_parallel_perf)
random2wl1_88_avg_serial = sum(random2wl1_88_serial_perf)/len(random2wl1_88_serial_perf)
random2wl1_88_avg_parallel = sum(random2wl1_88_parallel_perf)/len(random2wl1_88_parallel_perf)

# random2108
with open('random2_32_108_wl1.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_108_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_108_parallel_perf.append(int(float(val))/1000) 

random2wl1_108_max_serial = max(random2wl1_108_serial_perf)
random2wl1_108_min_serial = min(random2wl1_108_serial_perf)
random2wl1_108_max_parallel = max(random2wl1_108_parallel_perf)
random2wl1_108_min_parallel = min(random2wl1_108_parallel_perf)
random2wl1_108_avg_serial = sum(random2wl1_108_serial_perf)/len(random2wl1_108_serial_perf)
random2wl1_108_avg_parallel = sum(random2wl1_108_parallel_perf)/len(random2wl1_108_parallel_perf)

# random2128
with open('random2_32_128_wl1.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_128_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random2wl1_128_parallel_perf.append(int(float(val))/1000) 

random2wl1_128_max_serial = max(random2wl1_128_serial_perf)
random2wl1_128_min_serial = min(random2wl1_128_serial_perf)
random2wl1_128_max_parallel = max(random2wl1_128_parallel_perf)
random2wl1_128_min_parallel = min(random2wl1_128_parallel_perf)
random2wl1_128_avg_serial = sum(random2wl1_128_serial_perf)/len(random2wl1_128_serial_perf)
random2wl1_128_avg_parallel = sum(random2wl1_128_parallel_perf)/len(random2wl1_128_parallel_perf)


# setup the dataframe
Num_qubits = ['8', '28', '48', '68', '88', '108', '128', '8', '28', '48', '68', '88', '108', '128', '8', '28', '48', '68', '88', '108', '128', '8', '28', '48', '68', '88', '108', '128', '8', '28', '48', '68', '88', '108', '128', '8', '28', '48', '68', '88', '108', '128']

Performance = [random2wl2_8_avg_parallel, random2wl2_28_avg_parallel, random2wl2_48_avg_parallel, random2wl2_68_avg_parallel, random2wl2_88_avg_parallel, random2wl2_108_avg_parallel, random2wl2_128_avg_parallel, random2wl1_8_8_avg_parallel, random2wl1_8_28_avg_parallel, random2wl1_8_48_avg_parallel, random2wl1_8_68_avg_parallel, random2wl1_8_88_avg_parallel, random2wl1_8_108_avg_parallel, random2wl1_8_128_avg_parallel, random2wl1_6_8_avg_parallel, random2wl1_6_28_avg_parallel, random2wl1_6_48_avg_parallel, random2wl1_6_68_avg_parallel, random2wl1_6_88_avg_parallel, random2wl1_6_108_avg_parallel, random2wl1_6_128_avg_parallel, random2wl1_4_8_avg_parallel, random2wl1_4_28_avg_parallel, random2wl1_4_48_avg_parallel, random2wl1_4_68_avg_parallel, random2wl1_4_88_avg_parallel, random2wl1_4_108_avg_parallel, random2wl1_4_128_avg_parallel, random2wl1_2_8_avg_parallel, random2wl1_2_28_avg_parallel, random2wl1_2_48_avg_parallel, random2wl1_2_68_avg_parallel, random2wl1_2_88_avg_parallel, random2wl1_2_108_avg_parallel, random2wl1_2_128_avg_parallel, random2wl1_8_avg_parallel, random2wl1_28_avg_parallel, random2wl1_48_avg_parallel, random2wl1_68_avg_parallel, random2wl1_88_avg_parallel, random2wl1_108_avg_parallel, random2wl1_128_avg_parallel]

Weak_link_penalty = ['2', '2', '2', '2', '2', '2', '2', '1.8', '1.8', '1.8', '1.8', '1.8', '1.8', '1.8', '1.6', '1.6', '1.6', '1.6', '1.6', '1.6', '1.6', '1.4', '1.4', '1.4', '1.4', '1.4', '1.4', '1.4', '1.2', '1.2', '1.2', '1.2', '1.2', '1.2', '1.2', '1', '1', '1', '1', '1', '1', '1'] 

Model = ['Parallel', 'Parallel', 'Parallel', 'Parallel', 'Parallel', 'Parallel', 'Parallel', 'Parallel', 'Parallel']

df = pd.DataFrame({'Qubits':Num_qubits,'Execution Time [ms]':Performance, 'alpha':Weak_link_penalty})

print(df)

error = {random2wl2_8_avg_parallel: {'max': random2wl2_8_max_parallel,'min': random2wl2_8_min_parallel}, random2wl2_28_avg_parallel: {'max': random2wl2_28_max_parallel,'min': random2wl2_28_min_parallel}, random2wl2_48_avg_parallel: {'max': random2wl2_48_max_parallel,'min': random2wl2_48_min_parallel}, random2wl2_68_avg_parallel: {'max': random2wl2_68_max_parallel,'min': random2wl2_68_min_parallel}, random2wl2_88_avg_parallel: {'max': random2wl2_88_max_parallel,'min': random2wl2_88_min_parallel}, random2wl2_108_avg_parallel: {'max': random2wl2_108_max_parallel,'min': random2wl2_108_min_parallel}, random2wl2_128_avg_parallel: {'max': random2wl2_128_max_parallel,'min': random2wl2_128_min_parallel}, random2wl1_8_8_avg_parallel: {'max': random2wl1_8_8_max_parallel,'min': random2wl1_8_8_min_parallel}, random2wl1_8_28_avg_parallel: {'max': random2wl1_8_28_max_parallel,'min': random2wl1_8_28_min_parallel}, random2wl1_8_48_avg_parallel: {'max': random2wl1_8_48_max_parallel,'min': random2wl1_8_48_min_parallel}, random2wl1_8_68_avg_parallel: {'max': random2wl1_8_68_max_parallel,'min': random2wl1_8_68_min_parallel}, random2wl1_8_88_avg_parallel: {'max': random2wl1_8_88_max_parallel,'min': random2wl1_8_88_min_parallel}, random2wl1_8_108_avg_parallel: {'max': random2wl1_8_108_max_parallel,'min': random2wl1_8_108_min_parallel}, random2wl1_8_128_avg_parallel: {'max': random2wl1_8_128_max_parallel,'min': random2wl1_8_128_min_parallel}, random2wl1_6_8_avg_parallel: {'max': random2wl1_6_8_max_parallel,'min': random2wl1_6_8_min_parallel}, random2wl1_6_28_avg_parallel: {'max': random2wl1_6_28_max_parallel,'min': random2wl1_6_28_min_parallel}, random2wl1_6_48_avg_parallel: {'max': random2wl1_6_48_max_parallel,'min': random2wl1_6_48_min_parallel}, random2wl1_6_68_avg_parallel: {'max': random2wl1_6_68_max_parallel,'min': random2wl1_6_68_min_parallel}, random2wl1_6_88_avg_parallel: {'max': random2wl1_6_88_max_parallel,'min': random2wl1_6_88_min_parallel}, random2wl1_6_108_avg_parallel: {'max': random2wl1_6_108_max_parallel,'min': random2wl1_6_108_min_parallel}, random2wl1_6_128_avg_parallel: {'max': random2wl1_6_128_max_parallel,'min': random2wl1_6_128_min_parallel}, random2wl1_4_8_avg_parallel: {'max': random2wl1_4_8_max_parallel,'min': random2wl1_4_8_min_parallel}, random2wl1_4_28_avg_parallel: {'max': random2wl1_4_28_max_parallel,'min': random2wl1_4_28_min_parallel}, random2wl1_4_48_avg_parallel: {'max': random2wl1_4_48_max_parallel,'min': random2wl1_4_48_min_parallel}, random2wl1_4_68_avg_parallel: {'max': random2wl1_4_68_max_parallel,'min': random2wl1_4_68_min_parallel}, random2wl1_4_88_avg_parallel: {'max': random2wl1_4_88_max_parallel,'min': random2wl1_4_88_min_parallel}, random2wl1_4_108_avg_parallel: {'max': random2wl1_4_108_max_parallel,'min': random2wl1_4_108_min_parallel}, random2wl1_4_128_avg_parallel: {'max': random2wl1_4_128_max_parallel,'min': random2wl1_4_128_min_parallel}, random2wl1_2_8_avg_parallel: {'max': random2wl1_2_8_max_parallel, 'min': random2wl1_2_8_min_parallel}, random2wl1_2_28_avg_parallel: {'max': random2wl1_2_28_max_parallel,'min': random2wl1_2_28_min_parallel}, random2wl1_2_48_avg_parallel: {'max': random2wl1_2_48_max_parallel,'min': random2wl1_2_48_min_parallel}, random2wl1_2_68_avg_parallel: {'max': random2wl1_2_68_max_parallel,'min': random2wl1_2_68_min_parallel}, random2wl1_2_88_avg_parallel: {'max': random2wl1_2_88_max_parallel,'min': random2wl1_2_88_min_parallel}, random2wl1_2_108_avg_parallel: {'max': random2wl1_2_108_max_parallel,'min': random2wl1_2_108_min_parallel}, random2wl1_2_128_avg_parallel: {'max': random2wl1_2_128_max_parallel,'min': random2wl1_2_128_min_parallel}, random2wl1_8_avg_parallel: {'max': random2wl1_8_max_parallel, 'min': random2wl1_8_min_parallel}, random2wl1_28_avg_parallel: {'max': random2wl1_28_max_parallel,'min': random2wl1_28_min_parallel}, random2wl1_48_avg_parallel: {'max': random2wl1_48_max_parallel,'min': random2wl1_48_min_parallel}, random2wl1_68_avg_parallel: {'max': random2wl1_68_max_parallel,'min': random2wl1_68_min_parallel}, random2wl1_88_avg_parallel: {'max': random2wl1_88_max_parallel,'min': random2wl1_88_min_parallel}, random2wl1_108_avg_parallel: {'max': random2wl1_108_max_parallel,'min': random2wl1_108_min_parallel}, random2wl1_128_avg_parallel: {'max': random2wl1_128_max_parallel,'min': random2wl1_128_min_parallel}}

# plot the figure
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x='Qubits', y='Execution Time [ms]', hue='alpha', data=df, ax=ax)

#plt.title('32-ion chain')
#plt.ylim(0, 1.2)

# add the lines for the errors 
for p in ax.patches:
    x = p.get_x()  # get the bottom left x corner of the bar
    w = p.get_width()  # get width of bar
    h = p.get_height()  # get height of bar
    min_y = error[h]['min']  # use h to get min from dict z
    max_y = error[h]['max']  # use h to get max from dict z
    plt.vlines(x+w/2, min_y, max_y, color='k')  # draw a vertical line

#plt.show()
fig.savefig('scalability_random_weak_link_penalty.png', bbox_inches='tight')
