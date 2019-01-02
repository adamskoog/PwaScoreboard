import sound

class RaspPi(object):
    
    def __init__(self, pygame):

        self.IsPI = False
        try:
            import RPi.GPIO as GPIO
            self.IsPI = True
        except:
            pass
            
        self.pygame = pygame
        
        # SETUP GPIO PORTS
        self.BUTTON_P1 = 12
        self.BUTTON_RESET = 20
        self.BUTTON_P2 = 16
        self.BUZZER = 21
        
        if self.IsPI:

            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.BUTTON_RESET, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.setup(self.BUTTON_P1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.setup(self.BUTTON_P2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.setup(self.BUZZER, GPIO.OUT)
            GPIO.add_event_detect(self.BUTTON_P1, GPIO.FALLING, callback=self.button_callback, bouncetime=1000)
            GPIO.add_event_detect(self.BUTTON_P2, GPIO.FALLING, callback=self.button_callback, bouncetime=1000)
            GPIO.add_event_detect(self.BUTTON_RESET, GPIO.FALLING, callback=self.button_callback, bouncetime=1000)

        # Create the sound object
        self.sound = sound.Sound(self.BUZZER)

    def button_callback(self, channel):
        if channel == self.BUTTON_P1:
            event = self.pygame.event.Event(self.pygame.KEYDOWN, key=self.pygame.K_LEFT)
        if channel == self.BUTTON_P2:
            event = self.pygame.event.Event(self.pygame.KEYDOWN, key=self.pygame.K_RIGHT)
        if channel == self.BUTTON_RESET:
            event = self.pygame.event.Event(self.pygame.KEYDOWN, key=self.pygame.K_DOWN)

        self.pygame.event.post(event)

