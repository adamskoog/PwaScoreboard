import pygame
import scoreboard as sb
import pyscope as ps
import server
import sys
import _thread


IsPI = False
try:
    import RPi.GPIO as GPIO
    import sound
    IsPI = True
except:
    pass

# Define static variables
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
GAME_FPS = 5
CAPTION = "PWA Ping Pong Scoreboard"
TARGET_SCORE = 15
HTTP_PORT = 1337

# Try to run directly on a framebuffer (used on PI)
if "--probe" in sys.argv:
    screen = ps.probe()
else:
    # Initialize the game engine
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

if "--disableweb" in sys.argv:
    HTTP_PORT = None

def button_callback(channel):
    if channel == BUTTON_P1:
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT)
    if channel == BUTTON_P2:
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT)
    if channel == BUTTON_RESET:
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN)

    pygame.event.post(event)

if IsPI:
    # SETUP GPIO PORTS
    BUTTON_P1 = 12
    BUTTON_RESET = 20
    BUTTON_P2 = 16
    BUZZER = 21

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_RESET, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUTTON_P1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUTTON_P2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUZZER, GPIO.OUT)
    GPIO.add_event_detect(BUTTON_P1, GPIO.FALLING, callback=button_callback, bouncetime=1000)
    GPIO.add_event_detect(BUTTON_P2, GPIO.FALLING, callback=button_callback, bouncetime=1000)
    GPIO.add_event_detect(BUTTON_RESET, GPIO.FALLING, callback=button_callback, bouncetime=1000)

# Create the game window
size = (SCREEN_WIDTH, SCREEN_HEIGHT)   #test with 4:3 aspect ratio
pygame.display.set_caption(CAPTION)

# Create the sound object
if IsPI:
    sound = sound.Sound(BUZZER)

# Create the scoreboard object.
scoreboard = sb.Scoreboard(TARGET_SCORE)
quitGame = False

# get clock to manage screen update speed
clock = pygame.time.Clock()

# Stand up a small HTTP server for remote control
_thread.start_new_thread(server.run, (scoreboard,HTTP_PORT))

#--------- Main Loop ----------
playedWinnerSound = False
while not quitGame:
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitGame = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                scoreboard.Reset()
                if IsPI:
                    sound.Reset()
            elif event.key == pygame.K_LEFT:
                scoreboard.AddLeftScore()
                if IsPI:
                    sound.LeftScore()
            elif event.key == pygame.K_RIGHT:
                scoreboard.AddRightScore()
                if IsPI:
                    sound.RightScore()
            elif event.key == pygame.K_q:
                quitGame = True

    # Update the screen
    scoreboard.Draw()

    # Game Logic
    gameOver = scoreboard.CheckScore()

    # Play winner sound if game is over
    if gameOver and not playedWinnerSound:
        if IsPI:
            sound.Winner()
        playedWinnerSound = True

    # Reset check for playing winning sound only once
    if not gameOver and playedWinnerSound:
        playedWinnerSound = False

    # set speed fps
    clock.tick(GAME_FPS)

pygame.quit()
