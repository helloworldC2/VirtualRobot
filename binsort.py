from random import randint

def findMax(arr): # for finding the biggest element in the list
    m = 0
    for i in range (0,len(arr)):
        if m < arr[i]:
            m = arr[i]
    return m

def binsort(array):
    n = len(array) # the length of the lsit
    tmp = []
    m = findMax(array)

    for j in range(0,m+1): # filling up the auxiliary array with zeros
        tmp.append(0)

    for i in range(0,n): # counting each element in the input array
        tmp[array[i]] += 1

    q = 0
    for i in range(0,m+1): # rewriting the input array 
        for j in range(0,tmp[i]):
            array[q] = i
            q += 1
            
    return array # returning the sorted array



a = []
for i in range(0,100):
    a.append(randint(0,1000000))
print a
print binsort(a)
