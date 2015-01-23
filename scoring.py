import LeaderboardClient


class Score(object):
    """Initialises the Class "Score"
    
    @Params:
            score: the player's score
            
    """
    def __init__(self):
        self.score =  0

    """Uses incrementScore from LeaderboardClient
    Increases score by 25 points
    
    @Params: 
            None
            
    """
    def incrementScore(self):
        self.score = self.score + 25
    
    """happyDucks is a function which posts the scores to the Leaderboard Client
    
    @Params:
            None
    
    """
    def happyDucks(self,name):
        LeaderboardClient.postScore(name, self.score)
