import Jobs
def createJobs(alist,worker):
    jobs = []
    for i,t in enumerate(alist):
        jobs.append(Jobs.JobGoTo(i))
        jobs.append(Jobs.JobPlaceTreasure(i,treasure=t))
        
    exchanges = True
    passnum = len(alist)-2
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(len(jobs)-2):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               jobs.append(Jobs.JobGoTo(i))
               jobs.append(Jobs.JobPickUpTreasure(i))
               jobs.append(Jobs.JobStoreTreasure())
               alist[i] = alist[i+1]
               jobs.append(Jobs.JobGoTo(i+1))
               jobs.append(Jobs.JobPickUpTreasure(i+1))
               jobs.append(Jobs.JobGoTo(i))
               jobs.append(Jobs.JobPlaceTreasure(i))
               alist[i+1] = temp
               jobs.append(Jobs.JobGoTo(i+1))
               jobs.append(Jobs.JobSwapHandWithContainer())
               jobs.append(Jobs.JobPlaceTreasure(i+1))
               exchanges = True
       if exchanges == False:break
       for i in range(len(jobs)-2,0,-1):
           if alist[i]>alist[i+1]:
               jobs.append(Jobs.JobGoTo(i))
               jobs.append(Jobs.JobPickUpTreasure(i))
               jobs.append(Jobs.JobStoreTreasure())
               alist[i] = alist[i+1]
               jobs.append(Jobs.JobGoTo(i+1))
               jobs.append(Jobs.JobPickUpTreasure(i+1))
               jobs.append(Jobs.JobGoTo(i))
               jobs.append(Jobs.JobPlaceTreasure(i))
               alist[i+1] = temp
               jobs.append(Jobs.JobGoTo(i+1))
               jobs.append(Jobs.JobSwapHandWithContainer())
               jobs.append(Jobs.JobPlaceTreasure(i+1))
               exchanges == True

                               
       passnum = passnum-1
    jobs.append(Jobs.JobIdle())
    return jobs

