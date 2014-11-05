class Node(object):

    def __init__(self,pos,parent,costSoFar,distanceToEnd):
        self.pos = pos
        self.parent = parent
        self.costSoFar = costSoFar
        self.distanceToEnd = distanceToEnd
        self.totalCost = distanceToEnd +costSoFar
