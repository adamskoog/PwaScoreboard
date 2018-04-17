import pygame, shapes, scoring

class Scoreboard():
    def __init__(self, targetScore):
        self.LeftScore = 0
        self.RightScore = 0
        self.GameOver = False
        self.TargerScore = targetScore

    def AddLeftScore(self):
        if not self.GameOver:
            self.LeftScore += 1
        
    def AddRightScore(self):
        if not self.GameOver:
            self.RightScore += 1
        
    def SubtractLeftScore(self):
        if not self.GameOver and self.LeftScore > 0:
            self.LeftScore -= 1
            
    def SubtractRightScore(self):
        if not self.GameOver and self.RightScore > 0:
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
            self.GameOver = True
            return True
        elif (self.RightScore >= self.TargerScore) and (self.RightScore >= (self.LeftScore + 2)):
            print("SOUTH WINS")
            self.GameOver = True
            return True
        else:
            pass
            # print(str(self.LeftScore) + " - " + str(self.RightScore))
        
        # Game is not over.
        return False

    def Reset(self):
        self.LeftScore = 0
        self.RightScore = 0
        self.GameOver = False
        print("NEW GAME")
        
    def Draw(self):
        GREY = (64,64,64)
        WHITE = (255,255,255)    
        BLACK = (0,0,0)      

        screen = pygame.display.get_surface()  
        screenWidth, screenHeight = screen.get_size()
    
        outerBorderWidth = screenWidth * 0.022
        innerBorderWidth = screenWidth * 0.038

        # Fill the background
        screen.fill(GREY)
        
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
        
        # draw left side
        leftRectX = sideBuffer + screenOffset
        leftRectY = topBuffer + screenOffset
        pygame.draw.rect(screen, BLACK, (sideBuffer + screenOffset, topBuffer + screenOffset, width, height))

        scoring.drawNumber(self.LeftScore, screen, leftRectX, leftRectY, width, height)

        # draw right side
        rightRectX = screenWidth + screenOffset - sideBuffer - width
        rightRectY = topBuffer + screenOffset
        pygame.draw.rect(screen, BLACK, (rightRectX, rightRectY, width, height))
        
        scoring.drawNumber(self.RightScore, screen, rightRectX, rightRectY, width, height)

        pygame.display.flip()
