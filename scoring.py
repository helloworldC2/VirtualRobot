import LeaderboardClient


class Score(object):
    def __init__(self):
        self.score =  0

    def incrementScore(self):
        self.score = self.score + 25

    def happyDucks(self,name):
        LeaderboardClient.postScore(name, self.score)
