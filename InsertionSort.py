import Jobs
def createJobs(alist,worker):
    jobs = []
    for index in range(1,len(alist)):
       jobs.append(Jobs.JobGoTo(i))
       jobs.append(Jobs.JobPlaceTreasure(i,treasure=t))

    currentvalue = alist[index]
    position = index

    while position > 0 and alist[postion-1]>currentvalue:
       jobs.append(Jobs.JobGoTo(i))
       jobs.append(Jobs.JobPickUpTreasure(i))
       jobs.append(Jobs.JobStoreTreasure())
       alist[position]=alist[position-1]
       jobs.append(Jobs.JobGoTo(i+1))
       jobs.append(Jobs.JobPickUpTreasure(i+1))
       jobs.append(Jobs.JobGoTo(i))
       jobs.append(Jobs.JobPlaceTreasure(i))
       alist[postion] = currentvalue
       jobs.append(Jobs.JobGoTo(i+1))
       jobs.append(Jobs.JobSwapHandWithContainer())
       jobs.append(Jobs.JobPlaceTreasure(i+1))

       position = position-1
       jobs.append(Jobs.JobIdle())
       insertionSort (alist)
    return Jobs

