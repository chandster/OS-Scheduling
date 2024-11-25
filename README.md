# OS Scheduling
Simulates a Process Scheduler that assigns processes to the CPU based on a particular scheduling algorithm. You can run each algorithm from their respective Python files and observe the average wait times that are output or run `scheduler.py` to compare algorithms.

## scheduler.py
Each of the algorithms for FCFS, Round Robin and SJF returns a 2D array of arrival times, service times, wait times and burst times for each process. Run `scheduler.py` to compute and compare averages for these times across the scheduling algorithms.

## processes.csv
Each line in `processes.csv` has format `processName,arrivalTime,burstTime`. Try changing the values and adding more processes, then running `sheduler.py` again.

## priority_processes.csv
Similar to `processes.csv` but each process also has a priority (fourth value of each line). Used by `priority.py`.

## fcfs.py
Performs First Come First Served scheduling. Tasks that arrive first are executed first.

## sjf.py
Performs Shortest Job First scheduling. Tasks with shorter burst times are executed first.

## round_robin.py
Performs Round Robin scheduling. Tasks are executed in order cyclically for a time quantum.

## priority.py
Performs Priority Based scheduling. Tasks with higher priority (lower numbers) are executed first.

## read_processes.py
Contains functions to read in processes from the .csv files. Imported by the scheduling algorithm files.