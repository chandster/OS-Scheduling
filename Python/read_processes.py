import csv

def read_processes():
    filename = "Python/processes.csv"
    processes = []
    with open(filename, "r") as csvFile:
        csv_reader = csv.reader(csvFile)

        for row in csv_reader:
            name = row[0]
            arrival_time = int(row[1])
            burst_time = int(row[2])
            processes.append([name, arrival_time, burst_time])
    
    return processes

def read_processes_priority():
    filename = "priority_processes.csv"
    processes = []
    with open(filename, "r") as csvFile:
        csv_reader = csv.reader(csvFile)

        for row in csv_reader:
            name = row[0]
            arrival_time = int(row[1])
            burst_time = int(row[2])
            priority = int(row[3])
            processes.append([name, arrival_time, burst_time, priority])
    
    return processes