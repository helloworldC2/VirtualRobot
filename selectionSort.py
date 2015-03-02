import random

def selectionSort(treasureScores):
    for unsortedNums in range(len(treasureScores)-1,0,-1):
        posOfMaxNum=0
        for highestNum in range(1,unsortedNums+1):
            if treasureScores[highestNum]>treasureScores[posOfMaxNum]:
                posOfMaxNum = highestNum

        temp = treasureScores[unsortedNums]
        treasureScores[unsortedNums] = treasureScores[posOfMaxNum]
        treasureScores[posOfMaxNum] = temp

treasureScores = [54,26,93,17,77,31,44,55,20]
selectionSort(treasureScores)
print(treasureScores)

def testSort(TTS):
    sortedList = TTS.sort()
    print selectionSort(TTS) == sortedList

testSort(treasureScores)



    
