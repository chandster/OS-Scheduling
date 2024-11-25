from read_processes import read_processes
import numpy as np

def round_robin(tasks, quantum=2):
    currentTime = 0
    tasksCompleted = 0
    remainingTime = [None for t in tasks]
    taskWaitTimes = [None for t in tasks]
    taskServiceTimes = [None for t in tasks]
    info = []

    for i in range(len(tasks)):
        remainingTime[i] = tasks[i][2]

    finished = False
    index=0
    while not finished:
        index = index % len(tasks) # cycles through tasks
        taskTimeToCompletion = remainingTime[index]
        if taskTimeToCompletion > 0: # current task not yet completed
            taskServiceTimes[index] = currentTime
            taskTimeToCompletion -= quantum # task runs for some time
            if taskTimeToCompletion <= 0:
                tasksCompleted += 1
            remainingTime[index] = taskTimeToCompletion
        currentTime += quantum
        index +=1
        if tasksCompleted == len(tasks):
            finished = True

    for i, task in enumerate(tasks):
        taskWaitTimes[i] = taskServiceTimes[i] - task[1]
        print(f"{task[0]}\t\t{task[1]}\t\t{taskServiceTimes[i]}\t\t{taskWaitTimes[i]}\t\t{task[2]}")
        info.append([task[0],task[1],taskServiceTimes[i],taskWaitTimes[i],task[2]])

    avgWait = sum(taskWaitTimes) / len(taskWaitTimes)
    print(f"Average wait time: {avgWait}")
    info = np.transpose(info)
    info = np.array(info[1:], dtype=int)
    return info

#each process has format [name, arrivalTime, burstTime]
processes = read_processes()
print("\tArrival Time\tService Time\tWait Time\tBurst Time")
round_robin(processes)