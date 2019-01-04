import pygame

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
    import argparse

    parser = argparse.ArgumentParser(description="PWA Ping Pong Scoreboard")
    parser.add_argument("--fps", help="Override the default game FPS: 30", type=int, default=30)
    parser.add_argument("-p", "--probe", help="For use on Raspberry PI, probes system for GPU.", action="store_true")
    parser.add_argument("-s", "--http-server", help="Enable use of http server.", action="store_true", default=False)
    parser.add_argument("--http-port", help="Override the default http port: 1337", type=int, default=1337)

    args = parser.parse_args(_args)
    args.caption = "PWA Ping Pong Scoreboard"
    args.target_score = 15
    args.screen_width = 1024
    args.screen_height = 768 

    return args   

def main(_args):
    import scoreboard as sb
    import server, _thread

    args = parse_arguments(_args)

    # Create the scoreboard object.
    scoreboard = sb.Scoreboard(args)

    game = Game(args)
    game.execute(scoreboard)

    # Stand up a small HTTP server for remote control
    _thread.start_new_thread(server.run, (scoreboard,args))

if __name__ == "__main__":
    import sys    
    sys.exit(main(sys.argv[1:]))