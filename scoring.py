import LeaderboardClient

score = 0

def implementScore():
    score += 1

def happyDucks(name):
    LeaderboardClient.postScore(name, score)
