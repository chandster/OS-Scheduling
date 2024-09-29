# OS Scheduling
Simulates a Process Scheduler that assigns processes to the CPU based on a particular scheduling algorithm. You can run each algorithm from their respective Python files and compare the average wait times that are output.

## fcfs.py
Performs First Come First Served scheduling. Tasks that arrive first are executed first.

## sjf.py
Performs Shortest Job First scheduling. Tasks with shorter burst times are executed first.

## priority.py
Performs Priority Based scheduling. Tasks with higher priority (lower numbers) are executed first.

## read_processes.py
Contains functions to read in processes from the .csv files. Imported by the scheduling algorithm files.
