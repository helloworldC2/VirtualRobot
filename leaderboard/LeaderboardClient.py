from porc import Client
import random


client = Client("92598997-88c0-40cf-8cd7-767fe67470c8")

client.ping().raise_for_status()

def bubbleSort(l,s,n):

    for i in range(0,n):
        if l[i]>l[i+1]:
            temp = l[i]
            l[i] = l[i+1]
            l[i+1] = temp
            temp = s[i]
            s[i] = s[i+1]
            s[i+1] = temp
            del temp
    if n<=1:
        return l
    return bubbleSort(l,s,n-1)

def postScore(name, score):
    response = client.post('Leaderboard',{
      "name": name,
      "score": score
    })
    # make sure the request succeeded
    response.raise_for_status()
    # prints the item's key
    #print response.key
    # prints the item version's ref
    #print response.ref




def getHighScores():
    res = client.list('Leaderboard')


    pages = res.all()

    scores = []
    names = []
    for page in pages:
      # ensure getting the page succeeded
      #page.raise_for_response()
      scores.append(page["value"]['score'])
      names.append(page["value"]['name'])

      print page["value"]['name'],page["value"]['score']

    bubbleSort(scores,names,len(scores)-1)
    return [names,scores]
