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

qv32_8_serial_perf = []
qv32_28_serial_perf = []
qv32_48_serial_perf = []
qv32_68_serial_perf = []
qv32_88_serial_perf = []
qv32_108_serial_perf = []
qv32_128_serial_perf = []
qv32_8_parallel_perf = []
qv32_28_parallel_perf = []
qv32_48_parallel_perf = []
qv32_68_parallel_perf = []
qv32_88_parallel_perf = []
qv32_108_parallel_perf = []
qv32_128_parallel_perf = []

qv32_error_serial_perf = []
qv32_error_parallel_perf = []

qv40_8_serial_perf = []
qv40_28_serial_perf = []
qv40_48_serial_perf = []
qv40_68_serial_perf = []
qv40_88_serial_perf = []
qv40_108_serial_perf = []
qv40_128_serial_perf = []
qv40_8_parallel_perf = []
qv40_28_parallel_perf = []
qv40_48_parallel_perf = []
qv40_68_parallel_perf = []
qv40_88_parallel_perf = []
qv40_108_parallel_perf = []
qv40_128_parallel_perf = []

qv40_error_serial_perf = []
qv40_error_parallel_perf = []

qv48_8_serial_perf = []
qv48_28_serial_perf = []
qv48_48_serial_perf = []
qv48_68_serial_perf = []
qv48_88_serial_perf = []
qv48_108_serial_perf = []
qv48_128_serial_perf = []
qv48_8_parallel_perf = []
qv48_28_parallel_perf = []
qv48_48_parallel_perf = []
qv48_68_parallel_perf = []
qv48_88_parallel_perf = []
qv48_108_parallel_perf = []
qv48_128_parallel_perf = []

qv48_error_serial_perf = []
qv48_error_parallel_perf = []

qv56_8_serial_perf = []
qv56_28_serial_perf = []
qv56_48_serial_perf = []
qv56_68_serial_perf = []
qv56_88_serial_perf = []
qv56_108_serial_perf = []
qv56_128_serial_perf = []
qv56_8_parallel_perf = []
qv56_28_parallel_perf = []
qv56_48_parallel_perf = []
qv56_68_parallel_perf = []
qv56_88_parallel_perf = []
qv56_108_parallel_perf = []
qv56_128_parallel_perf = []

qv56_error_serial_perf = []
qv56_error_parallel_perf = []

qv64_8_serial_perf = []
qv64_28_serial_perf = []
qv64_48_serial_perf = []
qv64_68_serial_perf = []
qv64_88_serial_perf = []
qv64_108_serial_perf = []
qv64_128_serial_perf = []
qv64_8_parallel_perf = []
qv64_28_parallel_perf = []
qv64_48_parallel_perf = []
qv64_68_parallel_perf = []
qv64_88_parallel_perf = []
qv64_108_parallel_perf = []
qv64_128_parallel_perf = []

qv64_error_serial_perf = []
qv64_error_parallel_perf = []

# qv8
with open('qv_32_8.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv32_8_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv32_8_parallel_perf.append(int(float(val))/1000) 

qv32_8_max_serial = max(qv32_8_serial_perf)
qv32_8_min_serial = min(qv32_8_serial_perf)
qv32_8_max_parallel = max(qv32_8_parallel_perf)
qv32_8_min_parallel = min(qv32_8_parallel_perf)
qv32_8_avg_serial = sum(qv32_8_serial_perf)/len(qv32_8_serial_perf)
qv32_8_avg_parallel = sum(qv32_8_parallel_perf)/len(qv32_8_parallel_perf)

# qv28
with open('qv_32_28.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv32_28_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv32_28_parallel_perf.append(int(float(val))/1000) 

qv32_28_max_serial = max(qv32_28_serial_perf)
qv32_28_min_serial = min(qv32_28_serial_perf)
qv32_28_max_parallel = max(qv32_28_parallel_perf)
qv32_28_min_parallel = min(qv32_28_parallel_perf)
qv32_28_avg_serial = sum(qv32_28_serial_perf)/len(qv32_28_serial_perf)
qv32_28_avg_parallel = sum(qv32_28_parallel_perf)/len(qv32_28_parallel_perf)

# qv48
with open('qv_32_48.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv32_48_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv32_48_parallel_perf.append(int(float(val))/1000) 

qv32_48_max_serial = max(qv32_48_serial_perf)
qv32_48_min_serial = min(qv32_48_serial_perf)
qv32_48_max_parallel = max(qv32_48_parallel_perf)
qv32_48_min_parallel = min(qv32_48_parallel_perf)
qv32_48_avg_serial = sum(qv32_48_serial_perf)/len(qv32_48_serial_perf)
qv32_48_avg_parallel = sum(qv32_48_parallel_perf)/len(qv32_48_parallel_perf)

# qv68
with open('qv_32_68.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv32_68_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv32_68_parallel_perf.append(int(float(val))/1000) 

qv32_68_max_serial = max(qv32_68_serial_perf)
qv32_68_min_serial = min(qv32_68_serial_perf)
qv32_68_max_parallel = max(qv32_68_parallel_perf)
qv32_68_min_parallel = min(qv32_68_parallel_perf)
qv32_68_avg_serial = sum(qv32_68_serial_perf)/len(qv32_68_serial_perf)
qv32_68_avg_parallel = sum(qv32_68_parallel_perf)/len(qv32_68_parallel_perf)

# qv88
with open('qv_32_88.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv32_88_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv32_88_parallel_perf.append(int(float(val))/1000) 

qv32_88_max_serial = max(qv32_88_serial_perf)
qv32_88_min_serial = min(qv32_88_serial_perf)
qv32_88_max_parallel = max(qv32_88_parallel_perf)
qv32_88_min_parallel = min(qv32_88_parallel_perf)
qv32_88_avg_serial = sum(qv32_88_serial_perf)/len(qv32_88_serial_perf)
qv32_88_avg_parallel = sum(qv32_88_parallel_perf)/len(qv32_88_parallel_perf)

# qv108
with open('qv_32_108.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv32_108_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv32_108_parallel_perf.append(int(float(val))/1000) 

qv32_108_max_serial = max(qv32_108_serial_perf)
qv32_108_min_serial = min(qv32_108_serial_perf)
qv32_108_max_parallel = max(qv32_108_parallel_perf)
qv32_108_min_parallel = min(qv32_108_parallel_perf)
qv32_108_avg_serial = sum(qv32_108_serial_perf)/len(qv32_108_serial_perf)
qv32_108_avg_parallel = sum(qv32_108_parallel_perf)/len(qv32_108_parallel_perf)

# qv128
with open('qv_32_128.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv32_128_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv32_128_parallel_perf.append(int(float(val))/1000) 

qv32_128_max_serial = max(qv32_128_serial_perf)
qv32_128_min_serial = min(qv32_128_serial_perf)
qv32_128_max_parallel = max(qv32_128_parallel_perf)
qv32_128_min_parallel = min(qv32_128_parallel_perf)
qv32_128_avg_serial = sum(qv32_128_serial_perf)/len(qv32_128_serial_perf)
qv32_128_avg_parallel = sum(qv32_128_parallel_perf)/len(qv32_128_parallel_perf)


# qv8
with open('qv_40_8.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv40_8_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv40_8_parallel_perf.append(int(float(val))/1000) 

qv40_8_max_serial = max(qv40_8_serial_perf)
qv40_8_min_serial = min(qv40_8_serial_perf)
qv40_8_max_parallel = max(qv40_8_parallel_perf)
qv40_8_min_parallel = min(qv40_8_parallel_perf)
qv40_8_avg_serial = sum(qv40_8_serial_perf)/len(qv40_8_serial_perf)
qv40_8_avg_parallel = sum(qv40_8_parallel_perf)/len(qv40_8_parallel_perf)

# qv28
with open('qv_40_28.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv40_28_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv40_28_parallel_perf.append(int(float(val))/1000) 

qv40_28_max_serial = max(qv40_28_serial_perf)
qv40_28_min_serial = min(qv40_28_serial_perf)
qv40_28_max_parallel = max(qv40_28_parallel_perf)
qv40_28_min_parallel = min(qv40_28_parallel_perf)
qv40_28_avg_serial = sum(qv40_28_serial_perf)/len(qv40_28_serial_perf)
qv40_28_avg_parallel = sum(qv40_28_parallel_perf)/len(qv40_28_parallel_perf)

# qv48
with open('qv_40_48.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv40_48_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv40_48_parallel_perf.append(int(float(val))/1000) 

qv40_48_max_serial = max(qv40_48_serial_perf)
qv40_48_min_serial = min(qv40_48_serial_perf)
qv40_48_max_parallel = max(qv40_48_parallel_perf)
qv40_48_min_parallel = min(qv40_48_parallel_perf)
qv40_48_avg_serial = sum(qv40_48_serial_perf)/len(qv40_48_serial_perf)
qv40_48_avg_parallel = sum(qv40_48_parallel_perf)/len(qv40_48_parallel_perf)

# qv68
with open('qv_40_68.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv40_68_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv40_68_parallel_perf.append(int(float(val))/1000) 

qv40_68_max_serial = max(qv40_68_serial_perf)
qv40_68_min_serial = min(qv40_68_serial_perf)
qv40_68_max_parallel = max(qv40_68_parallel_perf)
qv40_68_min_parallel = min(qv40_68_parallel_perf)
qv40_68_avg_serial = sum(qv40_68_serial_perf)/len(qv40_68_serial_perf)
qv40_68_avg_parallel = sum(qv40_68_parallel_perf)/len(qv40_68_parallel_perf)

# qv88
with open('qv_40_88.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv40_88_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv40_88_parallel_perf.append(int(float(val))/1000) 

qv40_88_max_serial = max(qv40_88_serial_perf)
qv40_88_min_serial = min(qv40_88_serial_perf)
qv40_88_max_parallel = max(qv40_88_parallel_perf)
qv40_88_min_parallel = min(qv40_88_parallel_perf)
qv40_88_avg_serial = sum(qv40_88_serial_perf)/len(qv40_88_serial_perf)
qv40_88_avg_parallel = sum(qv40_88_parallel_perf)/len(qv40_88_parallel_perf)

# qv108
with open('qv_40_108.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv40_108_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv40_108_parallel_perf.append(int(float(val))/1000) 

qv40_108_max_serial = max(qv40_108_serial_perf)
qv40_108_min_serial = min(qv40_108_serial_perf)
qv40_108_max_parallel = max(qv40_108_parallel_perf)
qv40_108_min_parallel = min(qv40_108_parallel_perf)
qv40_108_avg_serial = sum(qv40_108_serial_perf)/len(qv40_108_serial_perf)
qv40_108_avg_parallel = sum(qv40_108_parallel_perf)/len(qv40_108_parallel_perf)

# qv128
with open('qv_40_128.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv40_128_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv40_128_parallel_perf.append(int(float(val))/1000) 

qv40_128_max_serial = max(qv40_128_serial_perf)
qv40_128_min_serial = min(qv40_128_serial_perf)
qv40_128_max_parallel = max(qv40_128_parallel_perf)
qv40_128_min_parallel = min(qv40_128_parallel_perf)
qv40_128_avg_serial = sum(qv40_128_serial_perf)/len(qv40_128_serial_perf)
qv40_128_avg_parallel = sum(qv40_128_parallel_perf)/len(qv40_128_parallel_perf)


# qv8
with open('qv_48_8.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv48_8_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv48_8_parallel_perf.append(int(float(val))/1000) 

qv48_8_max_serial = max(qv48_8_serial_perf)
qv48_8_min_serial = min(qv48_8_serial_perf)
qv48_8_max_parallel = max(qv48_8_parallel_perf)
qv48_8_min_parallel = min(qv48_8_parallel_perf)
qv48_8_avg_serial = sum(qv48_8_serial_perf)/len(qv48_8_serial_perf)
qv48_8_avg_parallel = sum(qv48_8_parallel_perf)/len(qv48_8_parallel_perf)

# qv28
with open('qv_48_28.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv48_28_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv48_28_parallel_perf.append(int(float(val))/1000) 

qv48_28_max_serial = max(qv48_28_serial_perf)
qv48_28_min_serial = min(qv48_28_serial_perf)
qv48_28_max_parallel = max(qv48_28_parallel_perf)
qv48_28_min_parallel = min(qv48_28_parallel_perf)
qv48_28_avg_serial = sum(qv48_28_serial_perf)/len(qv48_28_serial_perf)
qv48_28_avg_parallel = sum(qv48_28_parallel_perf)/len(qv48_28_parallel_perf)

# qv48
with open('qv_48_48.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv48_48_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv48_48_parallel_perf.append(int(float(val))/1000) 

qv48_48_max_serial = max(qv48_48_serial_perf)
qv48_48_min_serial = min(qv48_48_serial_perf)
qv48_48_max_parallel = max(qv48_48_parallel_perf)
qv48_48_min_parallel = min(qv48_48_parallel_perf)
qv48_48_avg_serial = sum(qv48_48_serial_perf)/len(qv48_48_serial_perf)
qv48_48_avg_parallel = sum(qv48_48_parallel_perf)/len(qv48_48_parallel_perf)

# qv68
with open('qv_48_68.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv48_68_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv48_68_parallel_perf.append(int(float(val))/1000) 

qv48_68_max_serial = max(qv48_68_serial_perf)
qv48_68_min_serial = min(qv48_68_serial_perf)
qv48_68_max_parallel = max(qv48_68_parallel_perf)
qv48_68_min_parallel = min(qv48_68_parallel_perf)
qv48_68_avg_serial = sum(qv48_68_serial_perf)/len(qv48_68_serial_perf)
qv48_68_avg_parallel = sum(qv48_68_parallel_perf)/len(qv48_68_parallel_perf)

# qv88
with open('qv_48_88.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv48_88_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv48_88_parallel_perf.append(int(float(val))/1000) 

qv48_88_max_serial = max(qv48_88_serial_perf)
qv48_88_min_serial = min(qv48_88_serial_perf)
qv48_88_max_parallel = max(qv48_88_parallel_perf)
qv48_88_min_parallel = min(qv48_88_parallel_perf)
qv48_88_avg_serial = sum(qv48_88_serial_perf)/len(qv48_88_serial_perf)
qv48_88_avg_parallel = sum(qv48_88_parallel_perf)/len(qv48_88_parallel_perf)

# qv108
with open('qv_48_108.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv48_108_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv48_108_parallel_perf.append(int(float(val))/1000) 

qv48_108_max_serial = max(qv48_108_serial_perf)
qv48_108_min_serial = min(qv48_108_serial_perf)
qv48_108_max_parallel = max(qv48_108_parallel_perf)
qv48_108_min_parallel = min(qv48_108_parallel_perf)
qv48_108_avg_serial = sum(qv48_108_serial_perf)/len(qv48_108_serial_perf)
qv48_108_avg_parallel = sum(qv48_108_parallel_perf)/len(qv48_108_parallel_perf)

# qv128
with open('qv_48_128.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv48_128_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv48_128_parallel_perf.append(int(float(val))/1000) 

qv48_128_max_serial = max(qv48_128_serial_perf)
qv48_128_min_serial = min(qv48_128_serial_perf)
qv48_128_max_parallel = max(qv48_128_parallel_perf)
qv48_128_min_parallel = min(qv48_128_parallel_perf)
qv48_128_avg_serial = sum(qv48_128_serial_perf)/len(qv48_128_serial_perf)
qv48_128_avg_parallel = sum(qv48_128_parallel_perf)/len(qv48_128_parallel_perf)


# qv8
with open('qv_56_8.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv56_8_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv56_8_parallel_perf.append(int(float(val))/1000) 

qv56_8_max_serial = max(qv56_8_serial_perf)
qv56_8_min_serial = min(qv56_8_serial_perf)
qv56_8_max_parallel = max(qv56_8_parallel_perf)
qv56_8_min_parallel = min(qv56_8_parallel_perf)
qv56_8_avg_serial = sum(qv56_8_serial_perf)/len(qv56_8_serial_perf)
qv56_8_avg_parallel = sum(qv56_8_parallel_perf)/len(qv56_8_parallel_perf)

# qv28
with open('qv_56_28.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv56_28_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv56_28_parallel_perf.append(int(float(val))/1000) 

qv56_28_max_serial = max(qv56_28_serial_perf)
qv56_28_min_serial = min(qv56_28_serial_perf)
qv56_28_max_parallel = max(qv56_28_parallel_perf)
qv56_28_min_parallel = min(qv56_28_parallel_perf)
qv56_28_avg_serial = sum(qv56_28_serial_perf)/len(qv56_28_serial_perf)
qv56_28_avg_parallel = sum(qv56_28_parallel_perf)/len(qv56_28_parallel_perf)

# qv48
with open('qv_56_48.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv56_48_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv56_48_parallel_perf.append(int(float(val))/1000) 

qv56_48_max_serial = max(qv56_48_serial_perf)
qv56_48_min_serial = min(qv56_48_serial_perf)
qv56_48_max_parallel = max(qv56_48_parallel_perf)
qv56_48_min_parallel = min(qv56_48_parallel_perf)
qv56_48_avg_serial = sum(qv56_48_serial_perf)/len(qv56_48_serial_perf)
qv56_48_avg_parallel = sum(qv56_48_parallel_perf)/len(qv56_48_parallel_perf)

# qv68
with open('qv_56_68.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv56_68_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv56_68_parallel_perf.append(int(float(val))/1000) 

qv56_68_max_serial = max(qv56_68_serial_perf)
qv56_68_min_serial = min(qv56_68_serial_perf)
qv56_68_max_parallel = max(qv56_68_parallel_perf)
qv56_68_min_parallel = min(qv56_68_parallel_perf)
qv56_68_avg_serial = sum(qv56_68_serial_perf)/len(qv56_68_serial_perf)
qv56_68_avg_parallel = sum(qv56_68_parallel_perf)/len(qv56_68_parallel_perf)

# qv88
with open('qv_56_88.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv56_88_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv56_88_parallel_perf.append(int(float(val))/1000) 

qv56_88_max_serial = max(qv56_88_serial_perf)
qv56_88_min_serial = min(qv56_88_serial_perf)
qv56_88_max_parallel = max(qv56_88_parallel_perf)
qv56_88_min_parallel = min(qv56_88_parallel_perf)
qv56_88_avg_serial = sum(qv56_88_serial_perf)/len(qv56_88_serial_perf)
qv56_88_avg_parallel = sum(qv56_88_parallel_perf)/len(qv56_88_parallel_perf)

# qv108
with open('qv_56_108.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv56_108_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv56_108_parallel_perf.append(int(float(val))/1000) 

qv56_108_max_serial = max(qv56_108_serial_perf)
qv56_108_min_serial = min(qv56_108_serial_perf)
qv56_108_max_parallel = max(qv56_108_parallel_perf)
qv56_108_min_parallel = min(qv56_108_parallel_perf)
qv56_108_avg_serial = sum(qv56_108_serial_perf)/len(qv56_108_serial_perf)
qv56_108_avg_parallel = sum(qv56_108_parallel_perf)/len(qv56_108_parallel_perf)

# qv128
with open('qv_56_128.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv56_128_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv56_128_parallel_perf.append(int(float(val))/1000) 

qv56_128_max_serial = max(qv56_128_serial_perf)
qv56_128_min_serial = min(qv56_128_serial_perf)
qv56_128_max_parallel = max(qv56_128_parallel_perf)
qv56_128_min_parallel = min(qv56_128_parallel_perf)
qv56_128_avg_serial = sum(qv56_128_serial_perf)/len(qv56_128_serial_perf)
qv56_128_avg_parallel = sum(qv56_128_parallel_perf)/len(qv56_128_parallel_perf)


# qv8
with open('qv_64_8.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv64_8_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv64_8_parallel_perf.append(int(float(val))/1000) 

qv64_8_max_serial = max(qv64_8_serial_perf)
qv64_8_min_serial = min(qv64_8_serial_perf)
qv64_8_max_parallel = max(qv64_8_parallel_perf)
qv64_8_min_parallel = min(qv64_8_parallel_perf)
qv64_8_avg_serial = sum(qv64_8_serial_perf)/len(qv64_8_serial_perf)
qv64_8_avg_parallel = sum(qv64_8_parallel_perf)/len(qv64_8_parallel_perf)

# qv28
with open('qv_64_28.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv64_28_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv64_28_parallel_perf.append(int(float(val))/1000) 

qv64_28_max_serial = max(qv64_28_serial_perf)
qv64_28_min_serial = min(qv64_28_serial_perf)
qv64_28_max_parallel = max(qv64_28_parallel_perf)
qv64_28_min_parallel = min(qv64_28_parallel_perf)
qv64_28_avg_serial = sum(qv64_28_serial_perf)/len(qv64_28_serial_perf)
qv64_28_avg_parallel = sum(qv64_28_parallel_perf)/len(qv64_28_parallel_perf)

# qv48
with open('qv_64_48.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv64_48_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv64_48_parallel_perf.append(int(float(val))/1000) 

qv64_48_max_serial = max(qv64_48_serial_perf)
qv64_48_min_serial = min(qv64_48_serial_perf)
qv64_48_max_parallel = max(qv64_48_parallel_perf)
qv64_48_min_parallel = min(qv64_48_parallel_perf)
qv64_48_avg_serial = sum(qv64_48_serial_perf)/len(qv64_48_serial_perf)
qv64_48_avg_parallel = sum(qv64_48_parallel_perf)/len(qv64_48_parallel_perf)

# qv68
with open('qv_64_68.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv64_68_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv64_68_parallel_perf.append(int(float(val))/1000) 

qv64_68_max_serial = max(qv64_68_serial_perf)
qv64_68_min_serial = min(qv64_68_serial_perf)
qv64_68_max_parallel = max(qv64_68_parallel_perf)
qv64_68_min_parallel = min(qv64_68_parallel_perf)
qv64_68_avg_serial = sum(qv64_68_serial_perf)/len(qv64_68_serial_perf)
qv64_68_avg_parallel = sum(qv64_68_parallel_perf)/len(qv64_68_parallel_perf)

# qv88
with open('qv_64_88.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv64_88_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv64_88_parallel_perf.append(int(float(val))/1000) 

qv64_88_max_serial = max(qv64_88_serial_perf)
qv64_88_min_serial = min(qv64_88_serial_perf)
qv64_88_max_parallel = max(qv64_88_parallel_perf)
qv64_88_min_parallel = min(qv64_88_parallel_perf)
qv64_88_avg_serial = sum(qv64_88_serial_perf)/len(qv64_88_serial_perf)
qv64_88_avg_parallel = sum(qv64_88_parallel_perf)/len(qv64_88_parallel_perf)

# qv108
with open('qv_64_108.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv64_108_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv64_108_parallel_perf.append(int(float(val))/1000) 

qv64_108_max_serial = max(qv64_108_serial_perf)
qv64_108_min_serial = min(qv64_108_serial_perf)
qv64_108_max_parallel = max(qv64_108_parallel_perf)
qv64_108_min_parallel = min(qv64_108_parallel_perf)
qv64_108_avg_serial = sum(qv64_108_serial_perf)/len(qv64_108_serial_perf)
qv64_108_avg_parallel = sum(qv64_108_parallel_perf)/len(qv64_108_parallel_perf)

# qv128
with open('qv_64_128.out') as file:
    for line in file:
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv64_128_serial_perf.append(int(float(val))/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qv64_128_parallel_perf.append(int(float(val))/1000) 

qv64_128_max_serial = max(qv64_128_serial_perf)
qv64_128_min_serial = min(qv64_128_serial_perf)
qv64_128_max_parallel = max(qv64_128_parallel_perf)
qv64_128_min_parallel = min(qv64_128_parallel_perf)
qv64_128_avg_serial = sum(qv64_128_serial_perf)/len(qv64_128_serial_perf)
qv64_128_avg_parallel = sum(qv64_128_parallel_perf)/len(qv64_128_parallel_perf)


# setup the dataframe
Num_qubits = ['8', '28', '48', '68', '88', '108', '128', '8', '28', '48', '68', '88', '108', '128', '8', '28', '48', '68', '88', '108', '128', '8', '28', '48', '68', '88', '108', '128', '8', '28', '48', '68', '88', '108', '128']

Performance = [qv32_8_avg_parallel, qv32_28_avg_parallel, qv32_48_avg_parallel, qv32_68_avg_parallel, qv32_88_avg_parallel, qv32_108_avg_parallel, qv32_128_avg_parallel, qv40_8_avg_parallel, qv40_28_avg_parallel, qv40_48_avg_parallel, qv40_68_avg_parallel, qv40_88_avg_parallel, qv40_108_avg_parallel, qv40_128_avg_parallel, qv48_8_avg_parallel, qv48_28_avg_parallel, qv48_48_avg_parallel, qv48_68_avg_parallel, qv48_88_avg_parallel, qv48_108_avg_parallel, qv48_128_avg_parallel, qv56_8_avg_parallel, qv56_28_avg_parallel, qv56_48_avg_parallel, qv56_68_avg_parallel, qv56_88_avg_parallel, qv56_108_avg_parallel, qv56_128_avg_parallel, qv64_8_avg_parallel, qv64_28_avg_parallel, qv64_48_avg_parallel, qv64_68_avg_parallel, qv64_88_avg_parallel, qv64_108_avg_parallel, qv64_128_avg_parallel]

Chain_length = ['32', '32', '32', '32', '32', '32', '32', '40', '40', '40', '40', '40', '40', '40', '48', '48', '48', '48', '48', '48', '48', '56', '56', '56', '56', '56', '56', '56', '64', '64', '64', '64', '64', '64', '64']

Model = ['Parallel', 'Parallel', 'Parallel', 'Parallel', 'Parallel', 'Parallel', 'Parallel', 'Parallel', 'Parallel']

df = pd.DataFrame({'Qubits':Num_qubits,'Execution Time [ms]':Performance, 'Chain length':Chain_length})

print(df)

error = {qv32_8_avg_parallel: {'max': qv32_8_max_parallel,'min': qv32_8_min_parallel}, qv32_28_avg_parallel: {'max': qv32_28_max_parallel,'min': qv32_28_min_parallel}, qv32_48_avg_parallel: {'max': qv32_48_max_parallel,'min': qv32_48_min_parallel}, qv32_68_avg_parallel: {'max': qv32_68_max_parallel,'min': qv32_68_min_parallel}, qv32_88_avg_parallel: {'max': qv32_88_max_parallel,'min': qv32_88_min_parallel}, qv32_108_avg_parallel: {'max': qv32_108_max_parallel,'min': qv32_108_min_parallel}, qv32_128_avg_parallel: {'max': qv32_128_max_parallel,'min': qv32_128_min_parallel}, qv40_8_avg_parallel: {'max': qv40_8_max_parallel,'min': qv40_8_min_parallel}, qv40_28_avg_parallel: {'max': qv40_28_max_parallel,'min': qv40_28_min_parallel}, qv40_48_avg_parallel: {'max': qv40_48_max_parallel,'min': qv40_48_min_parallel}, qv40_68_avg_parallel: {'max': qv40_68_max_parallel,'min': qv40_68_min_parallel}, qv40_88_avg_parallel: {'max': qv40_88_max_parallel,'min': qv40_88_min_parallel}, qv40_108_avg_parallel: {'max': qv40_108_max_parallel,'min': qv40_108_min_parallel}, qv40_128_avg_parallel: {'max': qv40_128_max_parallel,'min': qv40_128_min_parallel}, qv48_8_avg_parallel: {'max': qv48_8_max_parallel,'min': qv48_8_min_parallel}, qv48_28_avg_parallel: {'max': qv48_28_max_parallel,'min': qv48_28_min_parallel}, qv48_48_avg_parallel: {'max': qv48_48_max_parallel,'min': qv48_48_min_parallel}, qv48_68_avg_parallel: {'max': qv48_68_max_parallel,'min': qv48_68_min_parallel}, qv48_88_avg_parallel: {'max': qv48_88_max_parallel,'min': qv48_88_min_parallel}, qv48_108_avg_parallel: {'max': qv48_108_max_parallel,'min': qv48_108_min_parallel}, qv48_128_avg_parallel: {'max': qv48_128_max_parallel,'min': qv48_128_min_parallel}, qv56_8_avg_parallel: {'max': qv56_8_max_parallel,'min': qv56_8_min_parallel}, qv56_28_avg_parallel: {'max': qv56_28_max_parallel,'min': qv56_28_min_parallel}, qv56_48_avg_parallel: {'max': qv56_48_max_parallel,'min': qv56_48_min_parallel}, qv56_68_avg_parallel: {'max': qv56_68_max_parallel,'min': qv56_68_min_parallel}, qv56_88_avg_parallel: {'max': qv56_88_max_parallel,'min': qv56_88_min_parallel}, qv56_108_avg_parallel: {'max': qv56_108_max_parallel,'min': qv56_108_min_parallel}, qv56_128_avg_parallel: {'max': qv56_128_max_parallel,'min': qv56_128_min_parallel}, qv64_8_avg_parallel: {'max': qv64_8_max_parallel, 'min': qv64_8_min_parallel}, qv64_28_avg_parallel: {'max': qv64_28_max_parallel,'min': qv64_28_min_parallel}, qv64_48_avg_parallel: {'max': qv64_48_max_parallel,'min': qv64_48_min_parallel}, qv64_68_avg_parallel: {'max': qv64_68_max_parallel,'min': qv64_68_min_parallel}, qv64_88_avg_parallel: {'max': qv64_88_max_parallel,'min': qv64_88_min_parallel}, qv64_108_avg_parallel: {'max': qv64_108_max_parallel,'min': qv64_108_min_parallel}, qv64_128_avg_parallel: {'max': qv64_128_max_parallel,'min': qv64_128_min_parallel}}

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
fig.savefig('scalability_chain_length.png', bbox_inches='tight')
