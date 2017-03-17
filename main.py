import pygame
import scoreboard as sb

# Initialize the game engine
pygame.init()

# Define static variables
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
GAME_FPS = 60
CAPTION = "PWA Ping Pong Scoreboard"
TARGET_SCORE = 15

BACKGROUND = (64,64,64)

# Create the game window
size = (SCREEN_WIDTH, SCREEN_HEIGHT)   #test with 4:3 aspect ratio
screen = pygame.display.set_mode(size)
pygame.display.set_caption(CAPTION)

# Create the scoreboard object.
scoreboard = sb.Scoreboard(TARGET_SCORE)
quitGame = False

# get clock to manage screen update speed
clock = pygame.time.Clock()

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
    screen.fill(BACKGROUND)

    scoreboard.Draw(screen)
    
    pygame.display.flip()
    
    # set speed fps
    clock.tick(GAME_FPS)
    
pygame.quit()
