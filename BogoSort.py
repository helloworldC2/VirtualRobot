import Jobs
import random
def createJobs(alist,worker):
    jobs = []
    sortedList = sorted(alist)
    while True:
        random.shuffle(alist,random.random)
        for i,t in enumerate(alist):
            jobs.append(Jobs.JobGoTo(i))
            jobs.append(Jobs.JobPlaceTreasure(i,treasure=t))
        if alist==sortedList:
            break
        for i,t in enumerate(alist):
            jobs.append(Jobs.JobGoTo(i))
            jobs.append(Jobs.JobPickUpTreasure(i))

    jobs.append(Jobs.JobIdle())
    return jobs
