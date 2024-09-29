#non-preemptive priority scheduling
import read_processes as readIn

def priority(tasks):
    currentTime = 0
    tasksExecuted = []
    taskWaitTimes = []

    while len(tasks) > 0:
        arrivedNow = []
        for task in tasks:
            if task[1]<=currentTime: #tasks that have already arrived or arrived just now
                arrivedNow.append(task)
        
        if len(arrivedNow)>=1:
            #sort according to priority
            arrivedNow.sort(key=lambda x:x[3])
        if len(arrivedNow)>0:
            currentTask = arrivedNow[0]
            serviceTime=currentTime
            waitTime=currentTime-currentTask[1]
            task.append(serviceTime)
            task.append(waitTime)
            taskWaitTimes.append(waitTime)
            tasksExecuted.append(currentTask)

            currentTime += currentTask[2]
            tasks.remove(currentTask)

            print(f"{currentTask[0]}\t\t{currentTask[1]}\t\t{serviceTime}\t\t{waitTime}\t\t{currentTask[2]}\t\t{currentTask[3]}")
        else:
            currentTime+=1
    
    avgWait = sum(taskWaitTimes) / len(taskWaitTimes)
    print(f"Average wait time: {avgWait}")

#each process has format [name, arrivalTime, burstTime, priority]
processes = readIn.read_processes_priority()
print("\tArrival Time\tService Time\tWait Time\tBurst Time\tPriority")
priority(processes)