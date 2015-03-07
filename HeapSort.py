import random
import Jobs

def siftDown(l,start, end,jobs):
    root = start
    while root*2+1<=end:
        child = root*2+1
        swap = root
        if l[swap] < l[child]:#swap left child to top
            swap = child
        if child+1 <= end and l[swap] < l[child+1]:
            swap = child + 1#swap right child to top
        if swap == root:
            return#larest element is at the top
        else:
            jobs.append(Jobs.JobGoTo(root))
            jobs.append(Jobs.JobPickUpTreasure(root))
            jobs.append(Jobs.JobStoreTreasure())
            
            jobs.append(Jobs.JobGoTo(swap))
            jobs.append(Jobs.JobPickUpTreasure(swap))
            jobs.append(Jobs.JobGoTo(root))
            jobs.append(Jobs.JobPlaceTreasure(root))
            
            jobs.append(Jobs.JobGoTo(swap))
            jobs.append(Jobs.JobSwapHandWithContainer())
            jobs.append(Jobs.JobPlaceTreasure(swap))
            
            l[root],l[swap] = l[swap],l[root]
            root = swap

                
def heapify(l,length,jobs):
    
    start = (length-2)//2
    while start >=0:
        siftDown(l,start, length -1,jobs)
        start -=1
   

def heapSort(l,length):
    jobs = []
    for i,t in enumerate(l):
        jobs.append(Jobs.JobGoTo(i))
        jobs.append(Jobs.JobPlaceTreasure(i,treasure=t))
    heapify(l,length,jobs)
    end = length-1
    while end > 0:
        jobs.append(Jobs.JobGoTo(end))
        jobs.append(Jobs.JobPickUpTreasure(end))
        jobs.append(Jobs.JobStoreTreasure())
            
        jobs.append(Jobs.JobGoTo(0))
        jobs.append(Jobs.JobPickUpTreasure(0))
        jobs.append(Jobs.JobGoTo(end))
        jobs.append(Jobs.JobPlaceTreasure(end))
            
        jobs.append(Jobs.JobGoTo(0))
        jobs.append(Jobs.JobSwapHandWithContainer())
        jobs.append(Jobs.JobPlaceTreasure(0))
        l[end],l[0] = l[0],l[end]
        end -=1
        siftDown(l,0,end,jobs)
    jobs.append(Jobs.JobIdle())
    return jobs

    
##li = []
##for i in range(10000):
##    li.append(random.randint(0,100000))
##    
##print "Made list, now sorting"
##heapSort(li, len(li))
##print "Done..printing..."
##print li
##print "Sorted"
        

    
