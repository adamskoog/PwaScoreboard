import sys, pygame, argparse, _thread
import scoreboard as sb
import pyscope as ps
import server, rasppi

parser = argparse.ArgumentParser(description="PWA Ping Pong Scoreboard")
parser.add_argument("--fps", help="Override the default game FPS: 5", type=int, default=5)
parser.add_argument("-p", "--probe", help="For use on Raspberry PI, probes system for GPU.", action="store_true")
parser.add_argument("-s", "--http-server", help="Enable use of http server.", action="store_true", default=False)
parser.add_argument("--http-port", help="Override the default http port: 1337", type=int, default=1337)

args = parser.parse_args()
args.caption = "PWA Ping Pong Scoreboard"
args.target_score = 15
args.screen_width = 640
args.screen_height = 480

if args.probe:
    # Try to run directly on a framebuffer (PI)
    screen = ps.probe()
else:
    # Initialize the game engine in windowed mode (Windows)
    pygame.init()
    screen = pygame.display.set_mode((args.screen_width, args.screen_height))
    pygame.display.set_caption(args.caption)

# Initialize raspberry pi functions if available.
rasppi_gpio = rasppi.RaspPi(pygame)

# Create the scoreboard object.
scoreboard = sb.Scoreboard(args, rasppi_gpio)
quitGame = False

# get clock to manage screen update speed
clock = pygame.time.Clock()

# Stand up a small HTTP server for remote control
_thread.start_new_thread(server.run, (scoreboard,args))

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
            elif event.key == pygame.K_q:
                quitGame = True

    # Update the screen
    scoreboard.Draw()

    # Game Logic
    gameOver = scoreboard.CheckScore()

    # set speed fps
    clock.tick(args.fps)

pygame.quit()
