import numpy as np
from matplotlib import pyplot as plt

from fcfs import fcfs
from round_robin import round_robin
from sjf import sjf
from read_processes import read_processes

def get_avg(process_fn):
    processes = read_processes()
    times = process_fn(processes)
    return np.mean(times,axis=1)

mean_fcfs = get_avg(fcfs)
mean_rr = get_avg(round_robin)
mean_sjf = get_avg(sjf)
mean_times = np.array([mean_fcfs,mean_rr,mean_sjf]).transpose()
arrival_time = mean_times[0]
service_time = mean_times[1]
wait_time = mean_times[2]
burst_time = mean_times[3]

# labels for x axis correspond to algorithm names
x_labels = ["FCFS", "Round Robin", "SJF"]
x = np.arange(3)
width = 0.2

plt.bar(x-0.3, arrival_time, width, color='purple') 
plt.bar(x-0.1, service_time, width, color='orange') 
plt.bar(x+0.1, wait_time, width, color='red') 
plt.bar(x+0.3, burst_time, width, color='green') 
plt.xticks(x, x_labels) 
plt.xlabel("Scheduling Algorithms") 
plt.ylabel("Average Times") 
plt.legend(["Arrival Time", "Service Time", "Wait Time", "Burst Time"]) 
plt.title("Scheduling Algorithms Compared")
plt.show()