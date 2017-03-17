class Scoreboard():
    def __init__(self, targetScore):
        self.LeftScore = 0
        self.RightScore = 0
        self.TargerScore = targetScore
        
    def AddLeftScore(self):
        self.LeftScore += 1
        
    def AddRightScore(self):
        self.RightScore += 1
        
    def SubtractLeftScore(self):
        if self.LeftScore > 0:
            self.LeftScore -= 1
            
    def SubtractRightScore(self):
        if self.RightScore > 0:
            self.RightScore -= 1
           
    def CheckScore(self):
        if (self.LeftScore == self.RightScore) and (self.RightScore >= self.TargerScore - 1):
            print("DEUCE")
        elif (self.RightScore == self.LeftScore + 1) and (self.LeftScore >= self.TargerScore - 1):
            print("ADV >")
        elif (self.LeftScore == self.RightScore + 1) and (self.RightScore >= self.TargerScore - 1):
            print("< ADV")
        elif (self.LeftScore >= self.TargerScore) and (self.LeftScore >= (self.RightScore + 2)):
            print("NORTH WINS")
            return True
        elif (self.RightScore >= self.TargerScore) and (self.RightScore >= (self.LeftScore + 2)):
            print("SOUTH WINS")
            return True
        else:
            print(str(self.LeftScore) + " - " + str(self.RightScore))
        
        # Game is not over.
        return False

    def Reset(self):
        self.LeftScore = 0
        self.RightScore = 0
        print("NEW GAME")