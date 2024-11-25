#first come first served scheduling
import read_processes as readIn
import numpy as np

def fcfs(tasks):
    currentTime = 0
    tasksExecuted = []
    taskWaitTimes = []
    info = []

    while len(tasks) > 0:
        arrivedNow = []
        for task in tasks:
            if task[1]<=currentTime: #tasks that have already arrived or arrived just now
                arrivedNow.append(task)
        
        if len(arrivedNow)>=1:
            #sort according to arrival time
            arrivedNow.sort(key=lambda x:x[1])
        if len(arrivedNow)>0:
            currentTask = arrivedNow[0]
            serviceTime=currentTime
            waitTime=serviceTime-currentTask[1] #wait time = service time - arrival time
            task.append(serviceTime)
            task.append(waitTime)
            taskWaitTimes.append(waitTime)
            tasksExecuted.append(currentTask)

            currentTime += currentTask[2]
            tasks.remove(currentTask)

            print(f"{currentTask[0]}\t\t{currentTask[1]}\t\t{serviceTime}\t\t{waitTime}\t\t{currentTask[2]}")
            info.append([currentTask[0],currentTask[1],serviceTime, waitTime, currentTask[2]])
        else:
            currentTime+=1
    
    avgWait = sum(taskWaitTimes) / len(taskWaitTimes)
    print(f"Average wait time: {avgWait}")
    info = np.transpose(info)
    info = np.array(info[1:], dtype=int)
    return info

processes = readIn.read_processes()
print("\tArrival Time\tService Time\tWait Time\tBurst Time")
data = fcfs(processes)