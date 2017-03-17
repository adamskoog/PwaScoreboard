import pygame, shapes

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
        
    def Draw(self, screen):
        GREY = (64,64,64)
        WHITE = (255,255,255)    
        BLACK = (0,0,0) 
        
        screenWidth, screenHeight = screen.get_size()
    
        outerBorderWidth = screenWidth * 0.022
        innerBorderWidth = screenWidth * 0.038
        
        # Draw rounded rectange for border
        shapes.AAfilledRoundedRect(screen,(outerBorderWidth,outerBorderWidth,screenWidth-(outerBorderWidth*2),screenHeight-(outerBorderWidth*2)),WHITE,0.1)

        # Draw inside rounded rectange background color to create border
        shapes.AAfilledRoundedRect(screen,(innerBorderWidth,innerBorderWidth,screenWidth-(innerBorderWidth*2),screenHeight-(innerBorderWidth*2)),GREY,0.08)
        
        screenOffset = innerBorderWidth / 2
        screenWidth -= innerBorderWidth
        screenHeight -= innerBorderWidth
        
        topBuffer = (screenHeight * 0.3) / 2
        sideBuffer = (screenWidth * 0.08) / 2
        height = screenHeight * 0.45
        width = screenWidth * 0.4
        
        # draw left background
        pygame.draw.rect(screen, BLACK, (sideBuffer + screenOffset, topBuffer + screenOffset, width, height))
    
        # draw right background
        pygame.draw.rect(screen, BLACK, (screenWidth + screenOffset - sideBuffer - width, topBuffer + screenOffset, width, height))