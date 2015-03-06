import Jobs
def insertionSort(alist):
    jobs = []
    for index in range(1,len(alist)):
       jobs.append(Jobs.JobGoTo(index))
       jobs.append(Jobs.JobPlaceTreasure(index))

    currentvalue = alist[index]
    position = index

    while position > 0 and alist[position-1]>currentvalue:
       jobs.append(Jobs.JobGoTo(index))
       jobs.append(Jobs.JobPickUpTreasure(index))
       jobs.append(Jobs.JobStoreTreasure())
       alist[position]=alist[position-1]
       jobs.append(Jobs.JobGoTo(index+1))
       jobs.append(Jobs.JobPickUpTreasure(index+1))
       jobs.append(Jobs.JobGoTo(index))
       jobs.append(Jobs.JobPlaceTreasure(index))
       alist[position] = currentvalue
       jobs.append(Jobs.JobGoTo(index+1))
       jobs.append(Jobs.JobSwapHandWithContainer())
       jobs.append(Jobs.JobPlaceTreasure(index+1))

       position = position-1
       jobs.append(Jobs.JobIdle())
       
    return Jobs
