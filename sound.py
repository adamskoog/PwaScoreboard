import time
import RPi.GPIO as GPIO

class Sound():
    def __init__(self, buzzerPort):
        self.BuzzerPort = buzzerPort

    def _sound(self, durations):
        for i,j in durations:
        	GPIO.output(self.BuzzerPort, GPIO.HIGH)
        	time.sleep(i)
        	GPIO.output(self.BuzzerPort, GPIO.LOW)
        	time.sleep(j)

    def LeftScore(self):
        self._sound( [(0.1,0.1) , (0.1, 0.1)] )
    def RightScore(self):
        self._sound( [(0.1,0.1) , (0.1, 0.1)] )
    def Reset(self):
	    self._sound( [(1.0,0.1) , (0.1,0.1)] )
    def Winner(self):
        self._sound( [(0.1,0.1) , (0.1,0.1), (0.1,0.1), (0.1,0.1)] )
