# OS-Scheduling

This repository consists of scheduling algorithms: First Come First Served (`fcfs.py`), Priority (`priority.py`), Round Robin (`round_robin.py`), and Shortest Job First (`sjf.py`).

Each of the algorithms for FCFS, Round Robin and SJF returns a 2D array of arrival times, service times, wait times and burst times for each process. Run `scheduler.py` to compute and compare averages for these times across the scheduling algorithms.

Each line in `processes.csv` has format `processName,arrivalTime,burstTime`. Try changing the values and adding more processes, then running `sheduler.py` again.