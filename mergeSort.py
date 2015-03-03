import Jobs

def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        jobs = []

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
                jobs.append(Jobs.JobGoTo(i))
                jobs.append(Jobs.JobPickUpTreasure(i))
                jobs.append(Jobs.JobStoreTreasure())
            
                jobs.append(Jobs.JobGoTo(i))
                jobs.append(Jobs.JobPickUpTreasure(i+1))
                jobs.append(Jobs.JobGoTo(i))
                jobs.append(Jobs.JobPlaceTreasure(root))
            
                jobs.append(Jobs.JobGoTo(i+1))
                jobs.append(Jobs.JobSwapHandWithContainer())
                jobs.append(Jobs.JobPlaceTreasure(i+1))
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)
return jobs
