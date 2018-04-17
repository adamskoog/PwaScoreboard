import pygame
import scoreboard as sb
import pyscope as ps
import server
import sys
import thread

# Try to run directly on a framebuffer
if "--probe" in sys.argv:
    screen = ps.probe()
else:
    # Initialize the game engine
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

# Define static variables
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
GAME_FPS = 5
CAPTION = "PWA Ping Pong Scoreboard"
TARGET_SCORE = 15

BACKGROUND = (64,64,64)

# Create the game window
size = (SCREEN_WIDTH, SCREEN_HEIGHT)   #test with 4:3 aspect ratio
pygame.display.set_caption(CAPTION)

# Create the scoreboard object.
scoreboard = sb.Scoreboard(TARGET_SCORE)
quitGame = False

# get clock to manage screen update speed
clock = pygame.time.Clock()

# Stand up a small HTTP server for remote control
thread.start_new_thread(server.run, (scoreboard,))

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

    # Update the screen
    scoreboard.Draw()

    # Game Logic
    gameOver = scoreboard.CheckScore()

    # set speed fps
    clock.tick(GAME_FPS)
    
pygame.quit()
