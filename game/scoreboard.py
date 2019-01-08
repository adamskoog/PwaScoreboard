import math, pygame
import game.shapes as shapes
import game.scoring as scoring
import raspi.gpio

class GameStates:
    NORMAL = 0
    ADV_LEFT = 1
    ADV_RIGHT = 2
    DEUCE = 3
    GAME_OVER = 4
    GAME_OVER_NORTH = 5
    GAME_OVER_SOUTH = 6

class Scoreboard():
    def __init__(self, args):
        # Initialize raspberry pi functions if available.
        self.pi = raspi.gpio.RaspPi()

        self.LeftScore = 0
        self.RightScore = 0
        self.GameState = GameStates.NORMAL
        self.TargetScore = args.target_score
        self.PlayedWinnerSound = False

    def AddLeftScore(self):
        if self.GameState < GameStates.GAME_OVER:
            self.LeftScore += 1
            self.pi.sound.LeftScore()
        
    def AddRightScore(self):
        if self.GameState < GameStates.GAME_OVER:
            self.RightScore += 1
            self.pi.sound.RightScore()
        
    def SubtractLeftScore(self):
        if self.GameState < GameStates.GAME_OVER and self.LeftScore > 0:
            self.LeftScore -= 1
            self.pi.sound.LeftScore()
            
    def SubtractRightScore(self):
        if self.GameState < GameStates.GAME_OVER and self.RightScore > 0:
            self.RightScore -= 1
            self.pi.sound.RightScore()
             
    def CheckScore(self):
        if (self.LeftScore == self.RightScore) and (self.RightScore >= self.TargetScore - 1):
            self.GameState = GameStates.DEUCE
        elif (self.RightScore == self.LeftScore + 1) and (self.LeftScore >= self.TargetScore - 1):
            self.GameState = GameStates.ADV_RIGHT
        elif (self.LeftScore == self.RightScore + 1) and (self.RightScore >= self.TargetScore - 1):
            self.GameState = GameStates.ADV_LEFT
        elif (self.LeftScore >= self.TargetScore) and (self.LeftScore >= (self.RightScore + 2)):
            self.GameState = GameStates.GAME_OVER_NORTH

            # Play winner sound if game is over
            if not self.PlayedWinnerSound:
                self.pi.sound.Winner()
                self.playedWinnerSound = True

        elif (self.RightScore >= self.TargetScore) and (self.RightScore >= (self.LeftScore + 2)):
            self.GameState = GameStates.GAME_OVER_SOUTH

            # Play winner sound if game is over
            if not self.PlayedWinnerSound:
                self.pi.sound.Winner()
                self.playedWinnerSound = True

    def Reset(self):
        self.LeftScore = 0
        self.RightScore = 0
        self.GameState = GameStates.NORMAL

        self.PlayedWinnerSound = False
        self.pi.sound.Reset()
        
    def Draw(self):

        self.CheckScore()

        GREY = (64,64,64)
        LT_GRAY = (110,110,110)
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
        
        topBuffer = (screenHeight * 0.5) / 2
        sideBuffer = (screenWidth * 0.08) / 2
        height = screenHeight * 0.45
        width = screenWidth * 0.4
        
        # draw left side score
        leftRectX = sideBuffer + screenOffset
        leftRectY = topBuffer + screenOffset
        pygame.draw.rect(screen, BLACK, (sideBuffer + screenOffset, topBuffer + screenOffset, width, height))

        scoring.drawNumber(self.LeftScore, screen, leftRectX, leftRectY, width, height)

        # draw right side score
        rightRectX = screenWidth + screenOffset - sideBuffer - width
        rightRectY = topBuffer + screenOffset
        pygame.draw.rect(screen, BLACK, (rightRectX, rightRectY, width, height))
        
        scoring.drawNumber(self.RightScore, screen, rightRectX, rightRectY, width, height)

        # Determine shared calculations for coordinates
        advHBuffer = screenHeight * 0.015
        advHeight = screenHeight * 0.14
        advWidth = screenWidth * 0.245
        advY = leftRectY - advHeight - advHBuffer
        borderWidth = screenWidth * 0.0165

        # # Draw DEUCE
        deuceWidth = screenWidth * 0.325
        deuceX = (screenWidth / 2) - (deuceWidth / 2) + (borderWidth)

        shapes.AAfilledRoundedRect(screen,(deuceX,advY,deuceWidth,advHeight),WHITE,0.1)
        shapes.AAfilledRoundedRect(screen,(deuceX+(borderWidth/2),advY+(borderWidth/2),deuceWidth-borderWidth,advHeight-borderWidth),GREY,0.1)

        deuceColor = LT_GRAY
        if self.GameState == GameStates.DEUCE:
            deuceColor = WHITE

        textY = screenHeight * 0.145
        fontSize = int(screenWidth * 0.05)

        deuceTextX = screenWidth * 0.43
        shapes.Text(screen, "DEUCE", (deuceTextX,textY), deuceColor, fontSize)          

        # Draw < ADV
        advLeftX = leftRectX

        shapes.AAfilledRoundedRect(screen,(advLeftX,advY,advWidth,advHeight),WHITE,0.1)
        shapes.AAfilledRoundedRect(screen,(advLeftX+(borderWidth/2),advY+(borderWidth/2),advWidth-borderWidth,advHeight-borderWidth),GREY,0.1)

        leftAdvColor = LT_GRAY
        if self.GameState == GameStates.ADV_LEFT:
            leftAdvColor = WHITE

        advLeftTextX = screenWidth * 0.11
        shapes.Text(screen, "< ADV", (advLeftTextX,textY), leftAdvColor, fontSize)

        # # Draw ADV >
        advRightX = screenWidth + screenOffset - sideBuffer - advWidth

        shapes.AAfilledRoundedRect(screen,(advRightX,advY,advWidth,advHeight),WHITE,0.1)
        shapes.AAfilledRoundedRect(screen,(advRightX+(borderWidth/2),advY+(borderWidth/2),advWidth-borderWidth,advHeight-borderWidth),GREY,0.1)

        rightAdvColor = LT_GRAY
        if self.GameState == GameStates.ADV_RIGHT:
            rightAdvColor = WHITE

        advRightTextX = screenWidth * 0.8
        shapes.Text(screen, "ADV >", (advRightTextX,textY), rightAdvColor, fontSize)

        # Draw Win State
        winTextX = screenWidth * 0.165
        winTextY = screenHeight * 0.77
        winFontSize = int(screenWidth * 0.1)
        if self.GameState > GameStates.GAME_OVER:
            if self.GameState == GameStates.GAME_OVER_NORTH:
                shapes.Text(screen, "NORTH WINS!", (winTextX,winTextY), WHITE, winFontSize)
            elif self.GameState == GameStates.GAME_OVER_SOUTH:
                shapes.Text(screen, "SOUTH WINS!", (winTextX,winTextY), WHITE, winFontSize)

        pygame.display.flip()