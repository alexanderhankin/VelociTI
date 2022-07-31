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

random232_8_serial_perf = []
random232_28_serial_perf = []
random232_48_serial_perf = []
random232_68_serial_perf = []
random232_88_serial_perf = []
random232_108_serial_perf = []
random232_128_serial_perf = []
random232_8_parallel_perf = []
random232_28_parallel_perf = []
random232_48_parallel_perf = []
random232_68_parallel_perf = []
random232_88_parallel_perf = []
random232_108_parallel_perf = []
random232_128_parallel_perf = []

random232_error_serial_perf = []
random232_error_parallel_perf = []

random240_8_serial_perf = []
random240_28_serial_perf = []
random240_48_serial_perf = []
random240_68_serial_perf = []
random240_88_serial_perf = []
random240_108_serial_perf = []
random240_128_serial_perf = []
random240_8_parallel_perf = []
random240_28_parallel_perf = []
random240_48_parallel_perf = []
random240_68_parallel_perf = []
random240_88_parallel_perf = []
random240_108_parallel_perf = []
random240_128_parallel_perf = []

random240_error_serial_perf = []
random240_error_parallel_perf = []

random248_8_serial_perf = []
random248_28_serial_perf = []
random248_48_serial_perf = []
random248_68_serial_perf = []
random248_88_serial_perf = []
random248_108_serial_perf = []
random248_128_serial_perf = []
random248_8_parallel_perf = []
random248_28_parallel_perf = []
random248_48_parallel_perf = []
random248_68_parallel_perf = []
random248_88_parallel_perf = []
random248_108_parallel_perf = []
random248_128_parallel_perf = []

random248_error_serial_perf = []
random248_error_parallel_perf = []

random256_8_serial_perf = []
random256_28_serial_perf = []
random256_48_serial_perf = []
random256_68_serial_perf = []
random256_88_serial_perf = []
random256_108_serial_perf = []
random256_128_serial_perf = []
random256_8_parallel_perf = []
random256_28_parallel_perf = []
random256_48_parallel_perf = []
random256_68_parallel_perf = []
random256_88_parallel_perf = []
random256_108_parallel_perf = []
random256_128_parallel_perf = []

random256_error_serial_perf = []
random256_error_parallel_perf = []

random264_8_serial_perf = []
random264_28_serial_perf = []
random264_48_serial_perf = []
random264_68_serial_perf = []
random264_88_serial_perf = []
random264_108_serial_perf = []
random264_128_serial_perf = []
random264_8_parallel_perf = []
random264_28_parallel_perf = []
random264_48_parallel_perf = []
random264_68_parallel_perf = []
random264_88_parallel_perf = []
random264_108_parallel_perf = []
random264_128_parallel_perf = []

random264_error_serial_perf = []
random264_error_parallel_perf = []

# random28
with open('random2_32_8.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random232_8_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random232_8_parallel_perf.append(int(float(val))/1000) 

random232_8_max_serial = max(random232_8_serial_perf)
random232_8_min_serial = min(random232_8_serial_perf)
random232_8_max_parallel = max(random232_8_parallel_perf)
random232_8_min_parallel = min(random232_8_parallel_perf)
random232_8_avg_serial = sum(random232_8_serial_perf)/len(random232_8_serial_perf)
random232_8_avg_parallel = sum(random232_8_parallel_perf)/len(random232_8_parallel_perf)

# random228
with open('random2_32_28.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random232_28_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random232_28_parallel_perf.append(int(float(val))/1000) 

random232_28_max_serial = max(random232_28_serial_perf)
random232_28_min_serial = min(random232_28_serial_perf)
random232_28_max_parallel = max(random232_28_parallel_perf)
random232_28_min_parallel = min(random232_28_parallel_perf)
random232_28_avg_serial = sum(random232_28_serial_perf)/len(random232_28_serial_perf)
random232_28_avg_parallel = sum(random232_28_parallel_perf)/len(random232_28_parallel_perf)

# random248
with open('random2_32_48.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random232_48_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random232_48_parallel_perf.append(int(float(val))/1000) 

random232_48_max_serial = max(random232_48_serial_perf)
random232_48_min_serial = min(random232_48_serial_perf)
random232_48_max_parallel = max(random232_48_parallel_perf)
random232_48_min_parallel = min(random232_48_parallel_perf)
random232_48_avg_serial = sum(random232_48_serial_perf)/len(random232_48_serial_perf)
random232_48_avg_parallel = sum(random232_48_parallel_perf)/len(random232_48_parallel_perf)

# random268
with open('random2_32_68.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random232_68_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random232_68_parallel_perf.append(int(float(val))/1000) 

random232_68_max_serial = max(random232_68_serial_perf)
random232_68_min_serial = min(random232_68_serial_perf)
random232_68_max_parallel = max(random232_68_parallel_perf)
random232_68_min_parallel = min(random232_68_parallel_perf)
random232_68_avg_serial = sum(random232_68_serial_perf)/len(random232_68_serial_perf)
random232_68_avg_parallel = sum(random232_68_parallel_perf)/len(random232_68_parallel_perf)

# random288
with open('random2_32_88.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random232_88_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random232_88_parallel_perf.append(int(float(val))/1000) 

random232_88_max_serial = max(random232_88_serial_perf)
random232_88_min_serial = min(random232_88_serial_perf)
random232_88_max_parallel = max(random232_88_parallel_perf)
random232_88_min_parallel = min(random232_88_parallel_perf)
random232_88_avg_serial = sum(random232_88_serial_perf)/len(random232_88_serial_perf)
random232_88_avg_parallel = sum(random232_88_parallel_perf)/len(random232_88_parallel_perf)

# random2108
with open('random2_32_108.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random232_108_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random232_108_parallel_perf.append(int(float(val))/1000) 

random232_108_max_serial = max(random232_108_serial_perf)
random232_108_min_serial = min(random232_108_serial_perf)
random232_108_max_parallel = max(random232_108_parallel_perf)
random232_108_min_parallel = min(random232_108_parallel_perf)
random232_108_avg_serial = sum(random232_108_serial_perf)/len(random232_108_serial_perf)
random232_108_avg_parallel = sum(random232_108_parallel_perf)/len(random232_108_parallel_perf)

# random2128
with open('random2_32_128.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random232_128_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random232_128_parallel_perf.append(int(float(val))/1000) 

random232_128_max_serial = max(random232_128_serial_perf)
random232_128_min_serial = min(random232_128_serial_perf)
random232_128_max_parallel = max(random232_128_parallel_perf)
random232_128_min_parallel = min(random232_128_parallel_perf)
random232_128_avg_serial = sum(random232_128_serial_perf)/len(random232_128_serial_perf)
random232_128_avg_parallel = sum(random232_128_parallel_perf)/len(random232_128_parallel_perf)


# random28
with open('random2_40_8.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random240_8_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random240_8_parallel_perf.append(int(float(val))/1000) 

random240_8_max_serial = max(random240_8_serial_perf)
random240_8_min_serial = min(random240_8_serial_perf)
random240_8_max_parallel = max(random240_8_parallel_perf)
random240_8_min_parallel = min(random240_8_parallel_perf)
random240_8_avg_serial = sum(random240_8_serial_perf)/len(random240_8_serial_perf)
random240_8_avg_parallel = sum(random240_8_parallel_perf)/len(random240_8_parallel_perf)

# random228
with open('random2_40_28.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random240_28_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random240_28_parallel_perf.append(int(float(val))/1000) 

random240_28_max_serial = max(random240_28_serial_perf)
random240_28_min_serial = min(random240_28_serial_perf)
random240_28_max_parallel = max(random240_28_parallel_perf)
random240_28_min_parallel = min(random240_28_parallel_perf)
random240_28_avg_serial = sum(random240_28_serial_perf)/len(random240_28_serial_perf)
random240_28_avg_parallel = sum(random240_28_parallel_perf)/len(random240_28_parallel_perf)

# random248
with open('random2_40_48.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random240_48_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random240_48_parallel_perf.append(int(float(val))/1000) 

random240_48_max_serial = max(random240_48_serial_perf)
random240_48_min_serial = min(random240_48_serial_perf)
random240_48_max_parallel = max(random240_48_parallel_perf)
random240_48_min_parallel = min(random240_48_parallel_perf)
random240_48_avg_serial = sum(random240_48_serial_perf)/len(random240_48_serial_perf)
random240_48_avg_parallel = sum(random240_48_parallel_perf)/len(random240_48_parallel_perf)

# random268
with open('random2_40_68.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random240_68_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random240_68_parallel_perf.append(int(float(val))/1000) 

random240_68_max_serial = max(random240_68_serial_perf)
random240_68_min_serial = min(random240_68_serial_perf)
random240_68_max_parallel = max(random240_68_parallel_perf)
random240_68_min_parallel = min(random240_68_parallel_perf)
random240_68_avg_serial = sum(random240_68_serial_perf)/len(random240_68_serial_perf)
random240_68_avg_parallel = sum(random240_68_parallel_perf)/len(random240_68_parallel_perf)

# random288
with open('random2_40_88.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random240_88_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random240_88_parallel_perf.append(int(float(val))/1000) 

random240_88_max_serial = max(random240_88_serial_perf)
random240_88_min_serial = min(random240_88_serial_perf)
random240_88_max_parallel = max(random240_88_parallel_perf)
random240_88_min_parallel = min(random240_88_parallel_perf)
random240_88_avg_serial = sum(random240_88_serial_perf)/len(random240_88_serial_perf)
random240_88_avg_parallel = sum(random240_88_parallel_perf)/len(random240_88_parallel_perf)

# random2108
with open('random2_40_108.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random240_108_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random240_108_parallel_perf.append(int(float(val))/1000) 

random240_108_max_serial = max(random240_108_serial_perf)
random240_108_min_serial = min(random240_108_serial_perf)
random240_108_max_parallel = max(random240_108_parallel_perf)
random240_108_min_parallel = min(random240_108_parallel_perf)
random240_108_avg_serial = sum(random240_108_serial_perf)/len(random240_108_serial_perf)
random240_108_avg_parallel = sum(random240_108_parallel_perf)/len(random240_108_parallel_perf)

# random2128
with open('random2_40_128.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random240_128_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random240_128_parallel_perf.append(int(float(val))/1000) 

random240_128_max_serial = max(random240_128_serial_perf)
random240_128_min_serial = min(random240_128_serial_perf)
random240_128_max_parallel = max(random240_128_parallel_perf)
random240_128_min_parallel = min(random240_128_parallel_perf)
random240_128_avg_serial = sum(random240_128_serial_perf)/len(random240_128_serial_perf)
random240_128_avg_parallel = sum(random240_128_parallel_perf)/len(random240_128_parallel_perf)


# random28
with open('random2_48_8.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random248_8_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random248_8_parallel_perf.append(int(float(val))/1000) 

random248_8_max_serial = max(random248_8_serial_perf)
random248_8_min_serial = min(random248_8_serial_perf)
random248_8_max_parallel = max(random248_8_parallel_perf)
random248_8_min_parallel = min(random248_8_parallel_perf)
random248_8_avg_serial = sum(random248_8_serial_perf)/len(random248_8_serial_perf)
random248_8_avg_parallel = sum(random248_8_parallel_perf)/len(random248_8_parallel_perf)

# random228
with open('random2_48_28.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random248_28_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random248_28_parallel_perf.append(int(float(val))/1000) 

random248_28_max_serial = max(random248_28_serial_perf)
random248_28_min_serial = min(random248_28_serial_perf)
random248_28_max_parallel = max(random248_28_parallel_perf)
random248_28_min_parallel = min(random248_28_parallel_perf)
random248_28_avg_serial = sum(random248_28_serial_perf)/len(random248_28_serial_perf)
random248_28_avg_parallel = sum(random248_28_parallel_perf)/len(random248_28_parallel_perf)

# random248
with open('random2_48_48.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random248_48_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random248_48_parallel_perf.append(int(float(val))/1000) 

random248_48_max_serial = max(random248_48_serial_perf)
random248_48_min_serial = min(random248_48_serial_perf)
random248_48_max_parallel = max(random248_48_parallel_perf)
random248_48_min_parallel = min(random248_48_parallel_perf)
random248_48_avg_serial = sum(random248_48_serial_perf)/len(random248_48_serial_perf)
random248_48_avg_parallel = sum(random248_48_parallel_perf)/len(random248_48_parallel_perf)

# random268
with open('random2_48_68.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random248_68_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random248_68_parallel_perf.append(int(float(val))/1000) 

random248_68_max_serial = max(random248_68_serial_perf)
random248_68_min_serial = min(random248_68_serial_perf)
random248_68_max_parallel = max(random248_68_parallel_perf)
random248_68_min_parallel = min(random248_68_parallel_perf)
random248_68_avg_serial = sum(random248_68_serial_perf)/len(random248_68_serial_perf)
random248_68_avg_parallel = sum(random248_68_parallel_perf)/len(random248_68_parallel_perf)

# random288
with open('random2_48_88.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random248_88_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random248_88_parallel_perf.append(int(float(val))/1000) 

random248_88_max_serial = max(random248_88_serial_perf)
random248_88_min_serial = min(random248_88_serial_perf)
random248_88_max_parallel = max(random248_88_parallel_perf)
random248_88_min_parallel = min(random248_88_parallel_perf)
random248_88_avg_serial = sum(random248_88_serial_perf)/len(random248_88_serial_perf)
random248_88_avg_parallel = sum(random248_88_parallel_perf)/len(random248_88_parallel_perf)

# random2108
with open('random2_48_108.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random248_108_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random248_108_parallel_perf.append(int(float(val))/1000) 

random248_108_max_serial = max(random248_108_serial_perf)
random248_108_min_serial = min(random248_108_serial_perf)
random248_108_max_parallel = max(random248_108_parallel_perf)
random248_108_min_parallel = min(random248_108_parallel_perf)
random248_108_avg_serial = sum(random248_108_serial_perf)/len(random248_108_serial_perf)
random248_108_avg_parallel = sum(random248_108_parallel_perf)/len(random248_108_parallel_perf)

# random2128
with open('random2_48_128.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random248_128_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random248_128_parallel_perf.append(int(float(val))/1000) 

random248_128_max_serial = max(random248_128_serial_perf)
random248_128_min_serial = min(random248_128_serial_perf)
random248_128_max_parallel = max(random248_128_parallel_perf)
random248_128_min_parallel = min(random248_128_parallel_perf)
random248_128_avg_serial = sum(random248_128_serial_perf)/len(random248_128_serial_perf)
random248_128_avg_parallel = sum(random248_128_parallel_perf)/len(random248_128_parallel_perf)


# random28
with open('random2_56_8.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random256_8_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random256_8_parallel_perf.append(int(float(val))/1000) 

random256_8_max_serial = max(random256_8_serial_perf)
random256_8_min_serial = min(random256_8_serial_perf)
random256_8_max_parallel = max(random256_8_parallel_perf)
random256_8_min_parallel = min(random256_8_parallel_perf)
random256_8_avg_serial = sum(random256_8_serial_perf)/len(random256_8_serial_perf)
random256_8_avg_parallel = sum(random256_8_parallel_perf)/len(random256_8_parallel_perf)

# random228
with open('random2_56_28.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random256_28_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random256_28_parallel_perf.append(int(float(val))/1000) 

random256_28_max_serial = max(random256_28_serial_perf)
random256_28_min_serial = min(random256_28_serial_perf)
random256_28_max_parallel = max(random256_28_parallel_perf)
random256_28_min_parallel = min(random256_28_parallel_perf)
random256_28_avg_serial = sum(random256_28_serial_perf)/len(random256_28_serial_perf)
random256_28_avg_parallel = sum(random256_28_parallel_perf)/len(random256_28_parallel_perf)

# random248
with open('random2_56_48.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random256_48_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random256_48_parallel_perf.append(int(float(val))/1000) 

random256_48_max_serial = max(random256_48_serial_perf)
random256_48_min_serial = min(random256_48_serial_perf)
random256_48_max_parallel = max(random256_48_parallel_perf)
random256_48_min_parallel = min(random256_48_parallel_perf)
random256_48_avg_serial = sum(random256_48_serial_perf)/len(random256_48_serial_perf)
random256_48_avg_parallel = sum(random256_48_parallel_perf)/len(random256_48_parallel_perf)

# random268
with open('random2_56_68.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random256_68_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random256_68_parallel_perf.append(int(float(val))/1000) 

random256_68_max_serial = max(random256_68_serial_perf)
random256_68_min_serial = min(random256_68_serial_perf)
random256_68_max_parallel = max(random256_68_parallel_perf)
random256_68_min_parallel = min(random256_68_parallel_perf)
random256_68_avg_serial = sum(random256_68_serial_perf)/len(random256_68_serial_perf)
random256_68_avg_parallel = sum(random256_68_parallel_perf)/len(random256_68_parallel_perf)

# random288
with open('random2_56_88.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random256_88_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random256_88_parallel_perf.append(int(float(val))/1000) 

random256_88_max_serial = max(random256_88_serial_perf)
random256_88_min_serial = min(random256_88_serial_perf)
random256_88_max_parallel = max(random256_88_parallel_perf)
random256_88_min_parallel = min(random256_88_parallel_perf)
random256_88_avg_serial = sum(random256_88_serial_perf)/len(random256_88_serial_perf)
random256_88_avg_parallel = sum(random256_88_parallel_perf)/len(random256_88_parallel_perf)

# random2108
with open('random2_56_108.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random256_108_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random256_108_parallel_perf.append(int(float(val))/1000) 

random256_108_max_serial = max(random256_108_serial_perf)
random256_108_min_serial = min(random256_108_serial_perf)
random256_108_max_parallel = max(random256_108_parallel_perf)
random256_108_min_parallel = min(random256_108_parallel_perf)
random256_108_avg_serial = sum(random256_108_serial_perf)/len(random256_108_serial_perf)
random256_108_avg_parallel = sum(random256_108_parallel_perf)/len(random256_108_parallel_perf)

# random2128
with open('random2_56_128.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random256_128_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random256_128_parallel_perf.append(int(float(val))/1000) 

random256_128_max_serial = max(random256_128_serial_perf)
random256_128_min_serial = min(random256_128_serial_perf)
random256_128_max_parallel = max(random256_128_parallel_perf)
random256_128_min_parallel = min(random256_128_parallel_perf)
random256_128_avg_serial = sum(random256_128_serial_perf)/len(random256_128_serial_perf)
random256_128_avg_parallel = sum(random256_128_parallel_perf)/len(random256_128_parallel_perf)


# random28
with open('random2_64_8.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random264_8_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random264_8_parallel_perf.append(int(float(val))/1000) 

random264_8_max_serial = max(random264_8_serial_perf)
random264_8_min_serial = min(random264_8_serial_perf)
random264_8_max_parallel = max(random264_8_parallel_perf)
random264_8_min_parallel = min(random264_8_parallel_perf)
random264_8_avg_serial = sum(random264_8_serial_perf)/len(random264_8_serial_perf)
random264_8_avg_parallel = sum(random264_8_parallel_perf)/len(random264_8_parallel_perf)

# random228
with open('random2_64_28.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random264_28_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random264_28_parallel_perf.append(int(float(val))/1000) 

random264_28_max_serial = max(random264_28_serial_perf)
random264_28_min_serial = min(random264_28_serial_perf)
random264_28_max_parallel = max(random264_28_parallel_perf)
random264_28_min_parallel = min(random264_28_parallel_perf)
random264_28_avg_serial = sum(random264_28_serial_perf)/len(random264_28_serial_perf)
random264_28_avg_parallel = sum(random264_28_parallel_perf)/len(random264_28_parallel_perf)

# random248
with open('random2_64_48.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random264_48_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random264_48_parallel_perf.append(int(float(val))/1000) 

random264_48_max_serial = max(random264_48_serial_perf)
random264_48_min_serial = min(random264_48_serial_perf)
random264_48_max_parallel = max(random264_48_parallel_perf)
random264_48_min_parallel = min(random264_48_parallel_perf)
random264_48_avg_serial = sum(random264_48_serial_perf)/len(random264_48_serial_perf)
random264_48_avg_parallel = sum(random264_48_parallel_perf)/len(random264_48_parallel_perf)

# random268
with open('random2_64_68.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random264_68_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random264_68_parallel_perf.append(int(float(val))/1000) 

random264_68_max_serial = max(random264_68_serial_perf)
random264_68_min_serial = min(random264_68_serial_perf)
random264_68_max_parallel = max(random264_68_parallel_perf)
random264_68_min_parallel = min(random264_68_parallel_perf)
random264_68_avg_serial = sum(random264_68_serial_perf)/len(random264_68_serial_perf)
random264_68_avg_parallel = sum(random264_68_parallel_perf)/len(random264_68_parallel_perf)

# random288
with open('random2_64_88.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random264_88_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random264_88_parallel_perf.append(int(float(val))/1000) 

random264_88_max_serial = max(random264_88_serial_perf)
random264_88_min_serial = min(random264_88_serial_perf)
random264_88_max_parallel = max(random264_88_parallel_perf)
random264_88_min_parallel = min(random264_88_parallel_perf)
random264_88_avg_serial = sum(random264_88_serial_perf)/len(random264_88_serial_perf)
random264_88_avg_parallel = sum(random264_88_parallel_perf)/len(random264_88_parallel_perf)

# random2108
with open('random2_64_108.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random264_108_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random264_108_parallel_perf.append(int(float(val))/1000) 

random264_108_max_serial = max(random264_108_serial_perf)
random264_108_min_serial = min(random264_108_serial_perf)
random264_108_max_parallel = max(random264_108_parallel_perf)
random264_108_min_parallel = min(random264_108_parallel_perf)
random264_108_avg_serial = sum(random264_108_serial_perf)/len(random264_108_serial_perf)
random264_108_avg_parallel = sum(random264_108_parallel_perf)/len(random264_108_parallel_perf)

# random2128
with open('random2_64_128.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random264_128_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            random264_128_parallel_perf.append(int(float(val))/1000) 

random264_128_max_serial = max(random264_128_serial_perf)
random264_128_min_serial = min(random264_128_serial_perf)
random264_128_max_parallel = max(random264_128_parallel_perf)
random264_128_min_parallel = min(random264_128_parallel_perf)
random264_128_avg_serial = sum(random264_128_serial_perf)/len(random264_128_serial_perf)
random264_128_avg_parallel = sum(random264_128_parallel_perf)/len(random264_128_parallel_perf)


# setup the dataframe
Num_qubits = ['8', '28', '48', '68', '88', '108', '128', '8', '28', '48', '68', '88', '108', '128', '8', '28', '48', '68', '88', '108', '128', '8', '28', '48', '68', '88', '108', '128', '8', '28', '48', '68', '88', '108', '128']

Performance = [random232_8_avg_parallel, random232_28_avg_parallel, random232_48_avg_parallel, random232_68_avg_parallel, random232_88_avg_parallel, random232_108_avg_parallel, random232_128_avg_parallel, random240_8_avg_parallel, random240_28_avg_parallel, random240_48_avg_parallel, random240_68_avg_parallel, random240_88_avg_parallel, random240_108_avg_parallel, random240_128_avg_parallel, random248_8_avg_parallel, random248_28_avg_parallel, random248_48_avg_parallel, random248_68_avg_parallel, random248_88_avg_parallel, random248_108_avg_parallel, random248_128_avg_parallel, random256_8_avg_parallel, random256_28_avg_parallel, random256_48_avg_parallel, random256_68_avg_parallel, random256_88_avg_parallel, random256_108_avg_parallel, random256_128_avg_parallel, random264_8_avg_parallel, random264_28_avg_parallel, random264_48_avg_parallel, random264_68_avg_parallel, random264_88_avg_parallel, random264_108_avg_parallel, random264_128_avg_parallel]

Chain_length = ['32', '32', '32', '32', '32', '32', '32', '40', '40', '40', '40', '40', '40', '40', '48', '48', '48', '48', '48', '48', '48', '56', '56', '56', '56', '56', '56', '56', '64', '64', '64', '64', '64', '64', '64']

Model = ['Parallel', 'Parallel', 'Parallel', 'Parallel', 'Parallel', 'Parallel', 'Parallel', 'Parallel', 'Parallel']

df = pd.DataFrame({'Qubits':Num_qubits,'Execution Time [ms]':Performance, 'Chain length':Chain_length})

print(df)

error = {random232_8_avg_parallel: {'max': random232_8_max_parallel,'min': random232_8_min_parallel}, random232_28_avg_parallel: {'max': random232_28_max_parallel,'min': random232_28_min_parallel}, random232_48_avg_parallel: {'max': random232_48_max_parallel,'min': random232_48_min_parallel}, random232_68_avg_parallel: {'max': random232_68_max_parallel,'min': random232_68_min_parallel}, random232_88_avg_parallel: {'max': random232_88_max_parallel,'min': random232_88_min_parallel}, random232_108_avg_parallel: {'max': random232_108_max_parallel,'min': random232_108_min_parallel}, random232_128_avg_parallel: {'max': random232_128_max_parallel,'min': random232_128_min_parallel}, random240_8_avg_parallel: {'max': random240_8_max_parallel,'min': random240_8_min_parallel}, random240_28_avg_parallel: {'max': random240_28_max_parallel,'min': random240_28_min_parallel}, random240_48_avg_parallel: {'max': random240_48_max_parallel,'min': random240_48_min_parallel}, random240_68_avg_parallel: {'max': random240_68_max_parallel,'min': random240_68_min_parallel}, random240_88_avg_parallel: {'max': random240_88_max_parallel,'min': random240_88_min_parallel}, random240_108_avg_parallel: {'max': random240_108_max_parallel,'min': random240_108_min_parallel}, random240_128_avg_parallel: {'max': random240_128_max_parallel,'min': random240_128_min_parallel}, random248_8_avg_parallel: {'max': random248_8_max_parallel,'min': random248_8_min_parallel}, random248_28_avg_parallel: {'max': random248_28_max_parallel,'min': random248_28_min_parallel}, random248_48_avg_parallel: {'max': random248_48_max_parallel,'min': random248_48_min_parallel}, random248_68_avg_parallel: {'max': random248_68_max_parallel,'min': random248_68_min_parallel}, random248_88_avg_parallel: {'max': random248_88_max_parallel,'min': random248_88_min_parallel}, random248_108_avg_parallel: {'max': random248_108_max_parallel,'min': random248_108_min_parallel}, random248_128_avg_parallel: {'max': random248_128_max_parallel,'min': random248_128_min_parallel}, random256_8_avg_parallel: {'max': random256_8_max_parallel,'min': random256_8_min_parallel}, random256_28_avg_parallel: {'max': random256_28_max_parallel,'min': random256_28_min_parallel}, random256_48_avg_parallel: {'max': random256_48_max_parallel,'min': random256_48_min_parallel}, random256_68_avg_parallel: {'max': random256_68_max_parallel,'min': random256_68_min_parallel}, random256_88_avg_parallel: {'max': random256_88_max_parallel,'min': random256_88_min_parallel}, random256_108_avg_parallel: {'max': random256_108_max_parallel,'min': random256_108_min_parallel}, random256_128_avg_parallel: {'max': random256_128_max_parallel,'min': random256_128_min_parallel}, random264_8_avg_parallel: {'max': random264_8_max_parallel, 'min': random264_8_min_parallel}, random264_28_avg_parallel: {'max': random264_28_max_parallel,'min': random264_28_min_parallel}, random264_48_avg_parallel: {'max': random264_48_max_parallel,'min': random264_48_min_parallel}, random264_68_avg_parallel: {'max': random264_68_max_parallel,'min': random264_68_min_parallel}, random264_88_avg_parallel: {'max': random264_88_max_parallel,'min': random264_88_min_parallel}, random264_108_avg_parallel: {'max': random264_108_max_parallel,'min': random264_108_min_parallel}, random264_128_avg_parallel: {'max': random264_128_max_parallel,'min': random264_128_min_parallel}}

# plot the figure
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x='Qubits', y='Execution Time [ms]', hue='Chain length', data=df, ax=ax)

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
fig.savefig('scalability_random_chain_length.png', bbox_inches='tight')
