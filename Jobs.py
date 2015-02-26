import SorterRobot
import EntityTreasure

class Job(object):

    def __init__(self):
        self.jobDone = False

    def doneJob(self):
        self.jobDone = True

    def checkHasDone(self,worker):
        return False

    def doJob(self,worker):
        worker.currentJob = self
        print "doing job"

class JobIdle(Job):

    def __init__(self):
        super(JobIdle,self).__init__()

    def checkHasDone(self,worker):
        if len(worker.jobs) > 1:
            self.jobDone = True
    
    def doJob(self,worker):
        super(JobIdle,self).doJob(worker)

class JobGoTo(Job):

    def __init__(self,index):
        super(JobGoTo,self).__init__()
        self.index = index
    
    def doJob(self,worker):
        super(JobGoTo,self).doJob(worker)
        self.goTo(worker,self.index)

    def goTo(self,worker,index):
        x = (index * 2 + 2)
        if x>10:x=x-10
        y = ((index / 5)+1) * 3
        worker.dest = (x,y)
        print "Gone to",x,y

class JobPlaceTreasure(Job):

    def __init__(self,index,treasure=None):
        super(JobPlaceTreasure,self).__init__()
        self.treasure = treasure
        self.index = index
    
    def doJob(self,worker):
        super(JobPlaceTreasure,self).doJob(worker)
        if self.treasure == None:self.treasure=worker.inHand
        self.place(worker,self.treasure,self.index)

    def place(self,worker,treasureValue,index):
        x = (index * 2 + 2)
        y = ((index / 5)+1) * 3
        if x>10:
            x-=10
            y+=1
        else:
            y-=1
            
        worker.level.entities.append(EntityTreasure.EntityTreasure(worker.level,x<<5,y<<5,treasureValue))
        self.jobDone = True
        worker.inHand = None

class JobPickUpTreasure(Job):

    def __init__(self,index):
        super(JobPickUpTreasure,self).__init__()
        self.index = index
    
    def doJob(self,worker):
        super(JobPickUpTreasure,self).doJob(worker)
        self.pickUp(worker,self.index)

    def pickUp(self,worker,index):
        x = (index * 2 + 2)
        y = ((index / 5)+1) * 3
        if x>10:
            x-=10
            y+=1
        else:
            y-=1
        for e in worker.level.entities:
            if e==worker:continue
            if e.x >>5 == x and e.y >>5 == y:
                worker.inHand = e.value
                worker.level.entities.remove(e)
            
        self.jobDone = True


class JobSwapHandWithContainer(Job):

    def __init__(self):
        super(JobSwapHandWithContainer,self).__init__()
    
    def doJob(self,worker):
        super(JobSwapHandWithContainer,self).doJob(worker)
        self.swap(worker)

    def swap(self,worker):
        temp = worker.inHand
        worker.inHand = worker.inContainer
        worker.inContainer = temp
        self.jobDone = True
        print "Swapped"

class JobStoreTreasure(Job):

    def __init__(self):
        super(JobStoreTreasure,self).__init__()
    
    def doJob(self,worker):
        super(JobStoreTreasure,self).doJob(worker)
        self.store(worker)

    def store(self,worker):
        worker.inContainer = worker.inHand
        worker.inHand = None
        
        self.jobDone = True
        print "stored"
