import time

class Sound():
    def __init__(self, buzzerPort):

        self.GPIO = None
        try:
            import RPi.GPIO as GPIO
            self.GPIO = GPIO
        except:
            pass

        self.BuzzerPort = buzzerPort

    def _sound(self, durations):
        if self.GPIO != None:           
            for i,j in durations:
                self.GPIO.output(self.BuzzerPort, self.GPIO.HIGH)
                time.sleep(i)
                self.GPIO.output(self.BuzzerPort, self.GPIO.LOW)
                time.sleep(j)

    def LeftScore(self):
        self._sound( [(0.1,0.1) , (0.1, 0.1)] )

    def RightScore(self):
        self._sound( [(0.1,0.1) , (0.1, 0.1)] )

    def Reset(self):
        self._sound( [(1.0,0.1) , (0.1,0.1)] )
        
    def Winner(self):
        self._sound( [(0.1,0.1) , (0.1,0.1), (0.1,0.1), (0.1,0.1)] )
