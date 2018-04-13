from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class H(BaseHTTPRequestHandler):
    scoreboard = None

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

    def do_POST(self):
        self._set_headers()

        # Read the POSTED data
        # 0 = clear the score
        # 1 = increment player 1 score
        # 2 = incrment player 2 score
        # -1 and -2 decrement the score
        length = int(self.headers['Content-Length'])
        value = int(self.rfile.read(length))

        if value == 0:
            H.scoreboard.Reset()
        elif value == 1:
            H.scoreboard.AddLeftScore()
        elif value == 2:
            H.scoreboard.AddRightScore()
        else:
            pass

        self._set_headers()
        self.wfile.write("OK")
 
def run(scoreboard):
    print scoreboard
    H.scoreboard = scoreboard
    httpd = HTTPServer(('', 80), H)
    httpd.serve_forever()
