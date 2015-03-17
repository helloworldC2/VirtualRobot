import random


class Chromosome(object):

    def __init__(self,genes):
        self.genes = genes
        self.fitness = 0


def inList(i,l):
    for j in l:
        #print j,i
        if j==i:
          #  print "yep"
            return True
    #print "Nope"
    return False
def combine(a,b):
    checkList = list(a)
    new = []
    print checkList
    addBoth = False
    for i in range(len(a)):
        if inList(a[i],checkList) and inList(b[i],checkList) and addBoth and i<len(a)-1 and b[i]!=a[i]:
            new.append(a[i])
            new.append(b[i])
            checkList.remove(a[i])
            checkList.remove(b[i])
            addBoth = False
##        elif inList(a[i],checkList) and addBoth and i>=len(a)-1:
##             new.append(a[i])
##             checkList.remove(a[i])
##        elif inList(b[i],checkList) and addBoth and i>=len(b)-1:
##             new.append(b[i])
##             checkList.remove(b[i])
        elif inList(min(a[i],b[i]),checkList):
            new.append(min(a[i],b[i]))
            checkList.remove(min(a[i],b[i]))
        elif a[i]!=b[i] and inList(max(a[i],b[i]),checkList):
            new.append(max(a[i],b[i]))
            checkList.remove(max(a[i],b[i]))
        else:
            addBoth = True
        #print addBoth
        #print "check",checkList
        #print "new",new
    return new
                        
    
def combine1(a,b):
    new = []
    cont = False
    
    for i in range(len(a)):
        if cont==True:
            cont = False
            continue
        #print i,len(a),len(b)
        if not inList(min(a[i],b[i]),new):
            new.append(min(a[i],b[i]))
        elif a[i]!=b[i]:
            new.append(max(a[i],b[i]))
        elif i<len(a)-1:
            new.append(a[i])
            new.append(min(a[i+1],b[i+1]))
            cont = True
        else:
            new.append(a[i])
            
            
    #print len(a),len(new)
    return new
    
    
def geneticSort(l):
    chromosomes = []
    jobs = []
    lastBest = None
    for i in range(20):
        random.shuffle(l,random.random)
        chromosomes.append(Chromosome(list(l)))
        #print chromosomes[i].genes
        
    generations = 0
    while True:
        generations +=1
        for c in chromosomes:
            c.fitness = 0
            for i in range(len(c.genes)-1):
                if c.genes[i]<=c.genes[i+1]:c.fitness+=1
                if c.fitness > len(c.genes)-2:
                    print "Done in",generations,"generations with",len(chromosomes),"individuals"
                    return c.genes

        chromosomes.sort(key=lambda x: x.fitness, reverse=True)
        for i in range(len(chromosomes)/2):
            #print i,i*2,i*2+1,len(chromosomes)
            chromosomes[i*2].genes = combine(chromosomes[i*2].genes,chromosomes[i*2+1].genes)
            
        for i in range(20):
            random.shuffle(l,random.random)
            chromosomes.append(Chromosome(list(l)))

       
    
        lastBest = chromosomes[0].genes
        #print lastBest

l = []
for i in range(5):
    l.append(random.randint(0,1000))
print "Unsorted list:",l
print geneticSort(l)
            

