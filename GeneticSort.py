import random
import Jobs

class Chromosome(object):

    def __init__(self,genes):
        self.genes = genes
        self.fitness = 0


def inList(i,l):
    for j in l:
        if j==i:return True
    return False

def combine(a,b):
    new = []
    for i in range(len(a)):
        if not inList(min(a[i],b[i]),new):
            new.append(min(a[i],b[i]))
        else:
            new.append(max(a[i],b[i]))
    return new
    
    
def geneticSort(l,worker):
    chromosomes = []
    jobs = []
    for i in range(10):
        random.shuffle(l,random.random)
        chromosomes.append(Chromosome(list(l)))
        
    generations = 0
    while True:
        generations +=1
        for c in chromosomes:
            c.fitness = 0
            for i in range(len(c.genes)-1):
                if c.genes[i]<=c.genes[i+1]:c.fitness+=1
                if c.fitness > len(c.genes)-2:
                    print "Done in",generations,"generations with",len(chromosomes),"individuals"
                    for i,t in enumerate(c.genes):
                        jobs.append(Jobs.JobGoTo(i))
                        jobs.append(Jobs.JobPlaceTreasure(i,treasure=t))
                    jobs.append(Jobs.JobIdle())
                    return jobs

        chromosomes.sort(key=lambda x: x.fitness, reverse=True)
        for i in range(len(chromosomes)/2):
           chromosomes[i*2].genes = combine(chromosomes[i*2].genes,chromosomes[i*2+1].genes)
            
        for i in range(5):
            random.shuffle(l,random.random)
            chromosomes.append(Chromosome(list(l)))
        for i,t in enumerate(chromosomes[0].genes):
            jobs.append(Jobs.JobGoTo(i))
            jobs.append(Jobs.JobPlaceTreasure(i,treasure=t))
        for i,t in enumerate(chromosomes[0].genes):
            jobs.append(Jobs.JobGoTo(i))
            jobs.append(Jobs.JobPickUpTreasure(i))
        
   
            

