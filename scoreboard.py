)import pygame

# Initialize the game engine
pygame.init()

# Define static variables
GAME_FPS = 60
CAPTION = "PWA Ping Pong Scoreboard"
TARGET_SCORE = 15

# Create the game window
size = (300, 300)

screen = pygame.display.set_mode(size)
pygame.display.set_caption(CAPTION)

quitGame = False

scoreTeamOne = 0
scoreTeamTwo = 0

# get clock to manage screen update speed
clock = pygame.time.Clock()

def gameReset():
	global scoreTeamOne
	global scoreTeamTwo 
	scoreTeamOne = 0
	scoreTeamTwo = 0
	print("NEW GAME")

#--------- Main Loop ----------
while not quitGame:
	# Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitGame = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                gameReset()
            elif event.key == pygame.K_LEFT:
                scoreTeamOne += 1
            elif event.key == pygame.K_RIGHT:
                scoreTeamTwo += 1
            
    # Add Game Logic
    if (scoreTeamOne == scoreTeamTwo) and (scoreTeamTwo >= TARGET_SCORE - 1):
        print("DEUCE")
    elif (scoreTeamTwo == scoreTeamOne + 1) and (scoreTeamOne >= TARGET_SCORE - 1):
        print("ADV >")
    elif (scoreTeamOne == scoreTeamTwo + 1) and (scoreTeamTwo >= TARGET_SCORE - 1):
        print("< ADV")
    elif (scoreTeamOne >= TARGET_SCORE) and (scoreTeamOne >= (scoreTeamTwo + 2)):
        print("NORTH WINS")
    elif (scoreTeamTwo >= TARGET_SCORE) and (scoreTeamTwo >= (scoreTeamOne + 2)):
        print("SOUTH WINS")
    else:
        print(str(scoreTeamOne) + " - " + str(scoreTeamTwo))
    
    # Repaint Screen
    white = (255,255,255)    
    screen.fill(white)
    
    pygame.display.flip()
    
    # set speed fps
    clock.tick(GAME_FPS)
    
pygame.quit()
