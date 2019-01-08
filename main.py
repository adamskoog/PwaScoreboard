import pygame, logging

def parse_arguments(_args):
    import argparse, util

    debugChoices = util.UpperCaseList(["INFO","WARNING","ERROR","CRITICAL","DEBUG"])
    
    parser = argparse.ArgumentParser(description="PWA Ping Pong Scoreboard")
    # parser.add_argument("--fps", help="Override the default game FPS: 30", type=int, default=30)
    parser.add_argument("-l", "--loglevel", help="Logging level", choices=debugChoices, default="INFO")
    parser.add_argument("-f", "--logpath", help="The path to store the log file.")
    parser.add_argument("--probe", help="For use on Raspberry PI, probes system for GPU.", action="store_true")
    parser.add_argument("--http-server", help="Enable use of http server.", action="store_true", default=False)
    parser.add_argument("--http-host", help="Override the default http host: localhost", default="localhost")
    parser.add_argument("--http-port", help="Override the default http port: 1337", type=int, default=1337)

    args = parser.parse_args(_args)
    args.caption = "PWA Ping Pong Scoreboard"
    args.target_score = 15
    args.screen_width = 1024
    args.screen_height = 768 
    args.logscreen = True

    return args   

def init_logging(args):
    import logging.handlers

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
    logging.debug("Command Arguments: {}".format(args))

def main(_args):
    from game.runner import Runner
    from game.scoreboard import Scoreboard
    from web.server import Server

    # Parse Command Arguments
    args = parse_arguments(_args)

    # Intitialize Logging
    init_logging(args)

    # Create the scoreboard object.
    scoreboard = Scoreboard(args)

    # Stand up a small HTTP server for remote control (if enabled)
    webserver = Server(scoreboard, args)
    webserver.start()

    # Start up game loop
    runner = Runner(args)
    runner.execute(scoreboard)

if __name__ == "__main__":
    import sys    
    sys.exit(main(sys.argv[1:]))