import pygame, pygame.gfxdraw
import scoreboard as sb

# Initialize the game engine
pygame.init()

# Define static variables
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 225
GAME_FPS = 60
CAPTION = "PWA Ping Pong Scoreboard"
TARGET_SCORE = 15

WHITE = (255,255,255)    
BLACK = (0,0,0) 

# Create the game window
size = (SCREEN_WIDTH, SCREEN_HEIGHT)   #test with 4:3 aspect ratio
screen = pygame.display.set_mode(size)
pygame.display.set_caption(CAPTION)

# Create the scoreboard object.
scoreboard = sb.Scoreboard(TARGET_SCORE)
quitGame = False

# get clock to manage screen update speed
clock = pygame.time.Clock()

# Testing Graphics
def drawScoreboard(screen):
    global BLACK

    screenWidth, screenHeight = screen.get_size()

    topBuffer = (screenHeight * 0.3) / 2
    sideBuffer = (screenWidth * 0.1) / 2
    height = screenHeight * 0.45
    width = screenWidth * 0.4

    # draw left background
    pygame.draw.rect(screen, BLACK, (sideBuffer, topBuffer, width, height))

    # draw right background
    pygame.draw.rect(screen, BLACK, (300 - sideBuffer - width, topBuffer, width, height))

#--------- Main Loop ----------
while not quitGame:
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitGame = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                scoreboard.Reset()
            elif event.key == pygame.K_LEFT:
                scoreboard.AddLeftScore()
            elif event.key == pygame.K_RIGHT:
                scoreboard.AddRightScore()

    # Game Logic        
    gameOver = scoreboard.CheckScore()

    # Repaint Screen
    screen.fill(WHITE)

    drawScoreboard(screen)
    
    pygame.display.flip()
    
    # set speed fps
    clock.tick(GAME_FPS)
    
pygame.quit()
