import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import gmean

# set edgecolor param (this is a global setting, so only set it once)
plt.rcParams["patch.force_edgecolor"] = True
plt.rcParams['errorbar.capsize'] = 10
plt.rcParams.update({'font.size': 16})

supremacy_num_weak_links = []
qaoa_num_weak_links = []
squareroot_num_weak_links = []
qft_num_weak_links = []
adder_num_weak_links = []
bv_num_weak_links = []

supremacy_serial_perf = []
supremacy_parallel_perf = []

qaoa_serial_perf = []
qaoa_parallel_perf = []

squareroot_serial_perf = []
squareroot_parallel_perf = []

qft_serial_perf = []
qft_parallel_perf = []

adder_serial_perf = []
adder_parallel_perf = []

bv_serial_perf = []
bv_parallel_perf = []

error_serial_perf = []
error_parallel_perf = []

# supremacy
with open('supremacy.out') as file:
    for line in file:
        if 'Number of weak links:' in line:
            val = line.rstrip().split(":")[-1]
            supremacy_num_weak_links.append(int(val)) 
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            supremacy_serial_perf.append(int(val)/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            supremacy_parallel_perf.append(int(val)/1000) 

supremacy_max_serial = max(supremacy_serial_perf)
supremacy_min_serial = min(supremacy_serial_perf)
supremacy_max_parallel = max(supremacy_parallel_perf)
supremacy_min_parallel = min(supremacy_parallel_perf)
supremacy_avg_serial = sum(supremacy_serial_perf)/len(supremacy_serial_perf)
supremacy_avg_parallel = sum(supremacy_parallel_perf)/len(supremacy_parallel_perf)
print(supremacy_num_weak_links)


# qaoa
with open('qaoa.out') as file:
    for line in file:
        if 'Number of weak links:' in line:
            val = line.rstrip().split(":")[-1]
            qaoa_num_weak_links.append(int(val)) 
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qaoa_serial_perf.append(int(val)/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qaoa_parallel_perf.append(int(val)/1000) 

qaoa_max_serial = max(qaoa_serial_perf)
qaoa_min_serial = min(qaoa_serial_perf)
qaoa_max_parallel = max(qaoa_parallel_perf)
qaoa_min_parallel = min(qaoa_parallel_perf)
qaoa_avg_serial = sum(qaoa_serial_perf)/len(qaoa_serial_perf)
qaoa_avg_parallel = sum(qaoa_parallel_perf)/len(qaoa_parallel_perf)
print(qaoa_num_weak_links)


# squareroot
with open('squareroot.out') as file:
    for line in file:
        if 'Number of weak links:' in line:
            val = line.rstrip().split(":")[-1]
            squareroot_num_weak_links.append(int(val)) 
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            squareroot_serial_perf.append(int(val)/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            squareroot_parallel_perf.append(int(val)/1000) 

squareroot_max_serial = max(squareroot_serial_perf)
squareroot_min_serial = min(squareroot_serial_perf)
squareroot_max_parallel = max(squareroot_parallel_perf)
squareroot_min_parallel = min(squareroot_parallel_perf)
squareroot_avg_serial = sum(squareroot_serial_perf)/len(squareroot_serial_perf)
squareroot_avg_parallel = sum(squareroot_parallel_perf)/len(squareroot_parallel_perf)
print(squareroot_num_weak_links)


# qft
with open('qft.out') as file:
    for line in file:
        if 'Number of weak links:' in line:
            val = line.rstrip().split(":")[-1]
            qft_num_weak_links.append(int(val)) 
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qft_serial_perf.append(int(val)/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            qft_parallel_perf.append(int(val)/1000) 

qft_max_serial = max(qft_serial_perf)
qft_min_serial = min(qft_serial_perf)
qft_max_parallel = max(qft_parallel_perf)
qft_min_parallel = min(qft_parallel_perf)
qft_avg_serial = sum(qft_serial_perf)/len(qft_serial_perf)
qft_avg_parallel = sum(qft_parallel_perf)/len(qft_parallel_perf)
print(qft_num_weak_links)


# adder
with open('adder.out') as file:
    for line in file:
        if 'Number of weak links:' in line:
            val = line.rstrip().split(":")[-1]
            adder_num_weak_links.append(int(val)) 
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            adder_serial_perf.append(int(val)/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            adder_parallel_perf.append(int(val)/1000) 

adder_max_serial = max(adder_serial_perf)
adder_min_serial = min(adder_serial_perf)
adder_max_parallel = max(adder_parallel_perf)
adder_min_parallel = min(adder_parallel_perf)
adder_avg_serial = sum(adder_serial_perf)/len(adder_serial_perf)
adder_avg_parallel = sum(adder_parallel_perf)/len(adder_parallel_perf)
print(adder_num_weak_links)


# bv
with open('bv.out') as file:
    for line in file:
        if 'Number of weak links:' in line:
            val = line.rstrip().split(":")[-1]
            bv_num_weak_links.append(int(val)) 
        if 'Serial performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            bv_serial_perf.append(int(val)/1000) 
        if 'Parallel performance [us]:' in line:
            val = line.rstrip().split(":")[-1]
            bv_parallel_perf.append(int(val)/1000) 

bv_max_serial = max(bv_serial_perf)
bv_min_serial = min(bv_serial_perf)
bv_max_parallel = max(bv_parallel_perf)
bv_min_parallel = min(bv_parallel_perf)
bv_avg_serial = sum(bv_serial_perf)/len(bv_serial_perf)
bv_avg_parallel = sum(bv_parallel_perf)/len(bv_parallel_perf)
print(bv_num_weak_links)


# setup the dataframe
Benchmarks = ['Supremacy', 'QAOA', 'SquareRoot', 'QFT', 'Adder', 'BV', 'geomean', 'Supremacy', 'QAOA', 'SquareRoot', 'QFT', 'Adder', 'BV', 'geomean']

#Serial_Performance = [supremacy_avg_serial, qaoa_avg_serial, squareroot_avg_serial, qft_avg_serial, adder_avg_serial, bv_avg_serial]
#Parallel_Performance = [supremacy_avg_parallel, qaoa_avg_parallel, squareroot_avg_parallel, qft_avg_parallel, adder_avg_parallel, bv_avg_parallel]

geomean_serial = gmean([supremacy_avg_serial, qaoa_avg_serial, squareroot_avg_serial, qft_avg_serial, adder_avg_serial, bv_avg_serial])
geomean_parallel = gmean([supremacy_avg_parallel, qaoa_avg_parallel, squareroot_avg_parallel, qft_avg_parallel, adder_avg_parallel, bv_avg_parallel])

Performance = [supremacy_avg_serial, qaoa_avg_serial, squareroot_avg_serial, qft_avg_serial, adder_avg_serial, bv_avg_serial, geomean_serial, supremacy_avg_parallel, qaoa_avg_parallel, squareroot_avg_parallel, qft_avg_parallel, adder_avg_parallel, bv_avg_parallel, geomean_parallel]

Model = ['Serial', 'Serial', 'Serial', 'Serial', 'Serial', 'Serial', 'Serial', 'Parallel', 'Parallel', 'Parallel', 'Parallel', 'Parallel', 'Parallel', 'Parallel']

df = pd.DataFrame({'':Benchmarks,'Execution Time [ms]':Performance, 'Model':Model})

print(df)

error = {supremacy_avg_serial: {'max': supremacy_max_serial,'min': supremacy_min_serial}, qaoa_avg_serial: {'max': qaoa_max_serial,'min': qaoa_min_serial}, squareroot_avg_serial: {'max': squareroot_max_serial,'min': squareroot_min_serial}, qft_avg_serial: {'max': qft_max_serial,'min': qft_min_serial}, adder_avg_serial: {'max': adder_max_serial,'min': adder_min_serial}, bv_avg_serial: {'max': bv_max_serial,'min': bv_min_serial}, geomean_serial: {'max': 0,'min': 0}, supremacy_avg_parallel: {'max': supremacy_max_parallel,'min': supremacy_min_parallel}, qaoa_avg_parallel: {'max': qaoa_max_parallel,'min': qaoa_min_parallel}, squareroot_avg_parallel: {'max': squareroot_max_parallel,'min': squareroot_min_parallel}, qft_avg_parallel: {'max': qft_max_parallel,'min': qft_min_parallel}, adder_avg_parallel: {'max': adder_max_parallel,'min': adder_min_parallel}, bv_avg_parallel: {'max': bv_max_parallel,'min': bv_min_parallel}, geomean_parallel: {'max': 0,'min': 0}}

# plot the figure
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x='', y='Execution Time [ms]', hue='Model', data=df, ax=ax)

#plt.title('Comparison of Serial and Parallel Performance Models')
plt.xticks(rotation = 45)
plt.ylim(0, 85)

# add the lines for the errors 
for p in ax.patches:
    x = p.get_x()  # get the bottom left x corner of the bar
    w = p.get_width()  # get width of bar
    h = p.get_height()  # get height of bar
    min_y = error[h]['min']  # use h to get min from dict z
    max_y = error[h]['max']  # use h to get max from dict z
    plt.vlines(x+w/2, min_y, max_y, color='k')  # draw a vertical line

#plt.show()
fig.savefig('model_comparison.png', bbox_inches='tight')
