import pygame
import logging, logging.handlers

class Game:
    def __init__(self, args):
        self.args = args

        self.size = self.width, self.height = args.screen_width, args.screen_height

        # Initialize Game Engine
        pygame.init()

        # Initialize Game Fonts
        pygame.font.init()

        if args.probe:
            # Try to run directly on a framebuffer (PI)
            self.screen = pyscope.probe()
        else:
            # Initialize the game engine in windowed mode (Windows)
            pygame.init()
            self.screen = pygame.display.set_mode(self.size)
            pygame.display.set_caption(args.caption)

        self.running = True
 
    def event(self, event):

        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.scoreboard.Reset()
            elif event.key == pygame.K_LEFT:
                self.scoreboard.AddLeftScore()
            elif event.key == pygame.K_RIGHT:
                self.scoreboard.AddRightScore()
            elif event.key == pygame.K_q:
                self.running = False
        
    def loop(self):
        # Allow pygame to do internal events and processing with the OS
        pygame.event.pump()

    def render(self):
        self.scoreboard.Draw()

    def cleanup(self):
        pygame.quit()
 
    def execute(self, scoreboard):
 
        self.scoreboard = scoreboard

        while( self.running ):
            for event in pygame.event.get():
                self.event(event)
            self.loop()
            self.render()
        self.cleanup()

def parse_arguments(_args):
    import argparse, util

    debugChoices = util.UpperCaseList(["INFO","WARNING","ERROR","CRITICAL","DEBUG"])
    
    parser = argparse.ArgumentParser(description="PWA Ping Pong Scoreboard")
    # parser.add_argument("--fps", help="Override the default game FPS: 30", type=int, default=30)
    parser.add_argument("-l", "--loglevel", help="Logging level", choices=debugChoices, default="INFO")
    parser.add_argument("-f", "--logpath", help="The path to store the log file.")
    parser.add_argument("--probe", help="For use on Raspberry PI, probes system for GPU.", action="store_true")
    parser.add_argument("--http-server", help="Enable use of http server.", action="store_true", default=False)
    parser.add_argument("--http-port", help="Override the default http port: 1337", type=int, default=1337)

    args = parser.parse_args(_args)
    args.caption = "PWA Ping Pong Scoreboard"
    args.target_score = 15
    args.screen_width = 1024
    args.screen_height = 768 
    args.logscreen = True

    return args   

def init_logging(args):
    rootLogger = logging.getLogger()
    rootLogger.setLevel(getattr(logging, args.loglevel.upper(), None))

    if not args.logscreen:
        lhStdout = rootLogger.handlers[0]       # screen is only hanlder by default
        rootLogger.removeHandler(lhStdout)      # this will turn off screen logging

    if args.logpath != None:
        fileHandler = logging.FileHandler(args.logpath)
        fileHandler.setLevel(getattr(logging, args.loglevel.upper(), None))
        rootLogger.addHandler(fileHandler)

    logging.debug("Logging Initialized")

def main(_args):
    import scoreboard as sb
    import server, _thread

    # Parse Command Arguments
    args = parse_arguments(_args)

    # Intitialize Logging
    init_logging(args)

    # Create the scoreboard object.
    scoreboard = sb.Scoreboard(args)

    # Stand up a small HTTP server for remote control
    _thread.start_new_thread(server.run, (scoreboard,args))

    # Start up game loop
    game = Game(args)
    game.execute(scoreboard)

if __name__ == "__main__":
    import sys    
    sys.exit(main(sys.argv[1:]))