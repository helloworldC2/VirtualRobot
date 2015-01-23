import LeaderboardClient


class Score(object):
    """initialises the class
    sets score variable to 0"""
    def __init__(self):
        self.score =  0

    """uses incrementScore from LeaderboardClient
    increases score by 25 points"""
    def incrementScore(self):
        self.score = self.score + 25
    
    """happyDucks is a function which posts the scores to the leaderboard client"""
    def happyDucks(self,name):
        LeaderboardClient.postScore(name, self.score)
