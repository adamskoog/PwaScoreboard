import pygame, logging
import game.pyscope as pyscope

class Runner:
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
        logging.info("Game Running")
 
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