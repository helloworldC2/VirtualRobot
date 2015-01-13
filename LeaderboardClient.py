from porc import Client
import random

"""Unscrammbles the fake key
    just means the real one isn't on github so we are protected
    a bit from scanning bots
@Params:
        key (string): the key
@Return:
        key (string): unscrammbled key
"""
def slightlyUnscrammbleKey(key):
    keyy =""
    for i in range(len(key)):
        try:
            n = int(key[i])
            n-=1
            if n ==-1:
                n=9
            keyy+=str(n)
        except ValueError:
            keyy+=key[i]
            pass
    return keyy


key = "03609008-99c1-51cf-9cd8-878fe78581c9"
client = Client(slightlyUnscrammbleKey(key))
client.ping().raise_for_status()




"""Call to add score to database
@Params:
        name (string): name of player
        score (int): score player achieved
@Return:
        None
"""
def postScore(name, score):
    response = client.post('Leaderboard',{
      "name": name,
      "score": score
    })
    # make sure the request succeeded
    response.raise_for_status()


"""Used to sort scores recursively,from high to low, works well for a
small number of scores.
@Params:
        l (list[int]): list of scores
        s (list[string]): list of players names, remains fixed to scores
        n (int): end point of the unsorted section of the list
"""
def bubbleSort(l,s,n):

    for i in range(0,n):
        if l[i]<l[i+1]:
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

"""Fetches list of scores from database
@Params:
        None
@Return:
        scoresAndNames[names(list),scores(list)](list)
"""
def getHighScores():
    res = client.list('Leaderboard')
    pages = res.all()
    scores = []
    names = []
    for page in pages:
      scores.append(page["value"]['score'])
      names.append(page["value"]['name'])


    bubbleSort(scores,names,len(scores)-1)
    return [names,scores]
