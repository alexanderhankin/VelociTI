import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import gmean

# set edgecolor param (this is a global setting, so only set it once)
plt.rcParams["patch.force_edgecolor"] = True
plt.rcParams['errorbar.capsize'] = 10
plt.rcParams.update({'font.size': 14})


sim_time_25_25 = []
sim_time_25_50 = []
sim_time_25_75 = []
sim_time_25_100 = []

sim_time_50_50 = []
sim_time_50_100 = []
sim_time_50_150 = []
sim_time_50_200 = []

sim_time_75_75 = []
sim_time_75_150 = []
sim_time_75_225 = []
sim_time_75_300 = []

sim_time_100_100 = []
sim_time_100_200 = []
sim_time_100_300 = []
sim_time_100_400 = []


# sim_time_25_25 
with open('sim_time_25_25.out') as file:
    for line in file:
        if 'Simulation time [s]:' in line:
            val = line.rstrip().split(":")[-1]
            sim_time_25_25.append(int(float(val))) 

sim_time_25_25_max = max(sim_time_25_25)
sim_time_25_25_min = min(sim_time_25_25)
sim_time_25_25_avg = sum(sim_time_25_25)/len(sim_time_25_25)

# sim_time_25_50 
with open('sim_time_25_50.out') as file:
    for line in file:
        if 'Simulation time [s]:' in line:
            val = line.rstrip().split(":")[-1]
            sim_time_25_50.append(int(float(val))) 

sim_time_25_50_max = max(sim_time_25_50)
sim_time_25_50_min = min(sim_time_25_50)
sim_time_25_50_avg = sum(sim_time_25_50)/len(sim_time_25_50)

# sim_time_25_75 
with open('sim_time_25_75.out') as file:
    for line in file:
        if 'Simulation time [s]:' in line:
            val = line.rstrip().split(":")[-1]
            sim_time_25_75.append(int(float(val))) 

sim_time_25_75_max = max(sim_time_25_75)
sim_time_25_75_min = min(sim_time_25_75)
sim_time_25_75_avg = sum(sim_time_25_75)/len(sim_time_25_75)

# sim_time_25_100 
with open('sim_time_25_100.out') as file:
    for line in file:
        if 'Simulation time [s]:' in line:
            val = line.rstrip().split(":")[-1]
            sim_time_25_100.append(int(float(val))) 

sim_time_25_100_max = max(sim_time_25_100)
sim_time_25_100_min = min(sim_time_25_100)
sim_time_25_100_avg = sum(sim_time_25_100)/len(sim_time_25_100)

# sim_time_50_50 
with open('sim_time_50_50.out') as file:
    for line in file:
        if 'Simulation time [s]:' in line:
            val = line.rstrip().split(":")[-1]
            sim_time_50_50.append(int(float(val))) 

sim_time_50_50_max = max(sim_time_50_50)
sim_time_50_50_min = min(sim_time_50_50)
sim_time_50_50_avg = sum(sim_time_50_50)/len(sim_time_50_50)

# sim_time_50_100 
with open('sim_time_50_100.out') as file:
    for line in file:
        if 'Simulation time [s]:' in line:
            val = line.rstrip().split(":")[-1]
            sim_time_50_100.append(int(float(val))) 

sim_time_50_100_max = max(sim_time_50_100)
sim_time_50_100_min = min(sim_time_50_100)
sim_time_50_100_avg = sum(sim_time_50_100)/len(sim_time_50_100)

# sim_time_50_150 
with open('sim_time_50_150.out') as file:
    for line in file:
        if 'Simulation time [s]:' in line:
            val = line.rstrip().split(":")[-1]
            sim_time_50_150.append(int(float(val))) 

sim_time_50_150_max = max(sim_time_50_150)
sim_time_50_150_min = min(sim_time_50_150)
sim_time_50_150_avg = sum(sim_time_50_150)/len(sim_time_50_150)

# sim_time_50_200 
with open('sim_time_50_200.out') as file:
    for line in file:
        if 'Simulation time [s]:' in line:
            val = line.rstrip().split(":")[-1]
            sim_time_50_200.append(int(float(val))) 

sim_time_50_200_max = max(sim_time_50_200)
sim_time_50_200_min = min(sim_time_50_200)
sim_time_50_200_avg = sum(sim_time_50_200)/len(sim_time_50_200)

# sim_time_75_75 
with open('sim_time_75_75.out') as file:
    for line in file:
        if 'Simulation time [s]:' in line:
            val = line.rstrip().split(":")[-1]
            sim_time_75_75.append(int(float(val))) 

sim_time_75_75_max = max(sim_time_75_75)
sim_time_75_75_min = min(sim_time_75_75)
sim_time_75_75_avg = sum(sim_time_75_75)/len(sim_time_75_75)

# sim_time_75_150 
with open('sim_time_75_150.out') as file:
    for line in file:
        if 'Simulation time [s]:' in line:
            val = line.rstrip().split(":")[-1]
            sim_time_75_150.append(int(float(val))) 

sim_time_75_150_max = max(sim_time_75_150)
sim_time_75_150_min = min(sim_time_75_150)
sim_time_75_150_avg = sum(sim_time_75_150)/len(sim_time_75_150)

# sim_time_75_225 
with open('sim_time_75_225.out') as file:
    for line in file:
        if 'Simulation time [s]:' in line:
            val = line.rstrip().split(":")[-1]
            sim_time_75_225.append(int(float(val))) 

sim_time_75_225_max = max(sim_time_75_225)
sim_time_75_225_min = min(sim_time_75_225)
sim_time_75_225_avg = sum(sim_time_75_225)/len(sim_time_75_225)

# sim_time_75_300 
with open('sim_time_75_300.out') as file:
    for line in file:
        if 'Simulation time [s]:' in line:
            val = line.rstrip().split(":")[-1]
            sim_time_75_300.append(int(float(val))) 

sim_time_75_300_max = max(sim_time_75_300)
sim_time_75_300_min = min(sim_time_75_300)
sim_time_75_300_avg = sum(sim_time_75_300)/len(sim_time_75_300)

# sim_time_100_100 
with open('sim_time_100_100.out') as file:
    for line in file:
        if 'Simulation time [s]:' in line:
            val = line.rstrip().split(":")[-1]
            sim_time_100_100.append(int(float(val))) 

sim_time_100_100_max = max(sim_time_100_100)
sim_time_100_100_min = min(sim_time_100_100)
sim_time_100_100_avg = sum(sim_time_100_100)/len(sim_time_100_100)

# sim_time_100_200 
with open('sim_time_100_200.out') as file:
    for line in file:
        if 'Simulation time [s]:' in line:
            val = line.rstrip().split(":")[-1]
            sim_time_100_200.append(int(float(val))) 

sim_time_100_200_max = max(sim_time_100_200)
sim_time_100_200_min = min(sim_time_100_200)
sim_time_100_200_avg = sum(sim_time_100_200)/len(sim_time_100_200)

# sim_time_100_300 
with open('sim_time_100_300.out') as file:
    for line in file:
        if 'Simulation time [s]:' in line:
            val = line.rstrip().split(":")[-1]
            sim_time_100_300.append(int(float(val))) 

sim_time_100_300_max = max(sim_time_100_300)
sim_time_100_300_min = min(sim_time_100_300)
sim_time_100_300_avg = sum(sim_time_100_300)/len(sim_time_100_300)

# sim_time_100_400 
with open('sim_time_100_400.out') as file:
    for line in file:
        if 'Simulation time [s]:' in line:
            val = line.rstrip().split(":")[-1]
            sim_time_100_400.append(int(float(val))) 

sim_time_100_400_max = max(sim_time_100_400)
sim_time_100_400_min = min(sim_time_100_400)
sim_time_100_400_avg = sum(sim_time_100_400)/len(sim_time_100_400)

# setup the dataframe
Random_circuits = ['25:25', '25:50', '25:75', '25:100', '50:50', '50:100', '50:150', '50:200', '75:75', '75:150', '75:225', '75:300', '100:100', '100:200', '100:300', '100:400']

#Serial_Performance = [supremacy_avg_serial, qaoa_avg_serial, squareroot_avg_serial, qft_avg_serial, adder_avg_serial, bv_avg_serial]
#Parallel_Performance = [supremacy_avg_parallel, qaoa_avg_parallel, squareroot_avg_parallel, qft_avg_parallel, adder_avg_parallel, bv_avg_parallel]

Sim_time = [sim_time_25_25_avg, sim_time_25_50_avg, sim_time_25_75_avg, sim_time_25_100_avg, sim_time_50_50_avg, sim_time_50_100_avg, sim_time_50_150_avg, sim_time_50_200_avg, sim_time_75_75_avg, sim_time_75_150_avg, sim_time_75_225_avg, sim_time_75_300_avg, sim_time_100_100_avg, sim_time_100_200_avg, sim_time_100_300_avg, sim_time_100_400_avg]


df = pd.DataFrame({'Qubits:2-qubit Gates':Random_circuits,'Simulation Time [s]':Sim_time})
#df = pd.DataFrame({'':Benchmarks,'Execution Time [ms]':Performance, 'Model':Model})

print(df)

#error = {supremacy_avg_serial: {'max': supremacy_max_serial,'min': supremacy_min_serial}, qaoa_avg_serial: {'max': qaoa_max_serial,'min': qaoa_min_serial}, squareroot_avg_serial: {'max': squareroot_max_serial,'min': squareroot_min_serial}, qft_avg_serial: {'max': qft_max_serial,'min': qft_min_serial}, adder_avg_serial: {'max': adder_max_serial,'min': adder_min_serial}, bv_avg_serial: {'max': bv_max_serial,'min': bv_min_serial}, geomean_serial: {'max': 0,'min': 0}, supremacy_avg_parallel: {'max': supremacy_max_parallel,'min': supremacy_min_parallel}, qaoa_avg_parallel: {'max': qaoa_max_parallel,'min': qaoa_min_parallel}, squareroot_avg_parallel: {'max': squareroot_max_parallel,'min': squareroot_min_parallel}, qft_avg_parallel: {'max': qft_max_parallel,'min': qft_min_parallel}, adder_avg_parallel: {'max': adder_max_parallel,'min': adder_min_parallel}, bv_avg_parallel: {'max': bv_max_parallel,'min': bv_min_parallel}, geomean_parallel: {'max': 0,'min': 0}}

# plot the figure
fig, ax = plt.subplots(figsize=(6, 3))
sns.barplot(x='Qubits:2-qubit Gates', y='Simulation Time [s]', data=df, ax=ax)
#sns.barplot(x='', y='Execution Time [ms]', hue='Model', data=df, ax=ax)

#plt.title('Comparison of Serial and Parallel Performance Models')
plt.xticks(rotation = 60)
#plt.ylim(0, 85)

# add the lines for the errors 
#for p in ax.patches:
#    x = p.get_x()  # get the bottom left x corner of the bar
#    w = p.get_width()  # get width of bar
#    h = p.get_height()  # get height of bar
#    min_y = error[h]['min']  # use h to get min from dict z
#    max_y = error[h]['max']  # use h to get max from dict z
#    plt.vlines(x+w/2, min_y, max_y, color='k')  # draw a vertical line

#plt.show()
fig.savefig('sim_time_study.png', bbox_inches='tight')
