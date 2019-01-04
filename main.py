import pygame

def run(scoreboard, args):

    # get clock to manage screen update speed
    clock = pygame.time.Clock()

    while True:
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    scoreboard.Reset()
                elif event.key == pygame.K_LEFT:
                    scoreboard.AddLeftScore()
                elif event.key == pygame.K_RIGHT:
                    scoreboard.AddRightScore()
                elif event.key == pygame.K_q:
                    return None

        # Draw Screen
        scoreboard.Draw()

        # Set Speed (fps)
        clock.tick(args.fps)

def main(_args):
    import argparse, _thread, server, pyscope
    import scoreboard as sb

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

    if args.probe:
        # Try to run directly on a framebuffer (PI)
        screen = pyscope.probe()
    else:
        # Initialize the game engine in windowed mode (Windows)
        pygame.init()
        screen = pygame.display.set_mode((args.screen_width, args.screen_height))
        pygame.display.set_caption(args.caption)

    # Initialize Game Fonts
    pygame.font.init()

    # Create the scoreboard object.
    scoreboard = sb.Scoreboard(args)

    # Stand up a small HTTP server for remote control
    _thread.start_new_thread(server.run, (scoreboard,args))

    run(scoreboard, args)

    pygame.quit()

if __name__ == "__main__":
    import sys    
    sys.exit(main(sys.argv[1:]))