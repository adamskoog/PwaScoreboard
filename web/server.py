import logging
from web.bottle import Bottle, template, static_file
from threading import Thread

class Server:
    def __init__(self, scoreboard, args):
        self.scoreboard = scoreboard
        self.enabled = args.http_server
        self.host = args.http_host
        self.port = args.http_port

        self._app = Bottle()
        self.initialize()

    def start(self):
        if self.enabled:
            self.initialize()

            self.server = Thread(target = self._app.run, kwargs={ "host": self.host, "port": self.port })
            self.server.setDaemon(True)
            self.server.start()

            logging.info("Web Server running on: {}:{}".format(self.host, self.port))
        else:
            logging.info("Web Server not running.")

    # The stop is something that doesn't seem to be needed to implement. The thread will be
    # terminated 2 seconds after the parent thread is destroyed.
    def stop(self):
        pass

    def initialize(self):
        self._app.route("/", "GET", self.remote)
        self._app.route("/score", "GET", self.scoreInfo)
        self._app.route("/score/left/add", "POST", self.scoreLeft)
        self._app.route("/score/left/remove", "POST", self.removeScoreLeft)
        self._app.route("/score/right/add", "POST", self.scoreRight)
        self._app.route("/score/right/remove", "POST", self.removeScoreRight)
        self._app.route("/reset", "POST", self.reset)

    # Below are functions for routing of requests
    def remote(self):
        return static_file("remote.html", root="./web/files/")

    def scoreInfo(self):
        return { "left": self.scoreboard.LeftScore, "right": self.scoreboard.RightScore }

    def scoreLeft(self):
        self.scoreboard.AddLeftScore()
        return { "left": self.scoreboard.LeftScore, "right": self.scoreboard.RightScore }

    def removeScoreLeft(self):
        self.scoreboard.SubtractLeftScore()
        return { "left": self.scoreboard.LeftScore, "right": self.scoreboard.RightScore }

    def scoreRight(self):
        self.scoreboard.AddRightScore()
        return { "left": self.scoreboard.LeftScore, "right": self.scoreboard.RightScore }

    def removeScoreRight(self):
        self.scoreboard.SubtractRightScore()
        return { "left": self.scoreboard.LeftScore, "right": self.scoreboard.RightScore }

    def reset(self):
        self.scoreboard.Reset()
        return { "left": self.scoreboard.LeftScore, "right": self.scoreboard.RightScore }
