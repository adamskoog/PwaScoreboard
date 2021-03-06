import pygame

class Buttons(object):
    
    def __init__(self):

        self.GPIO = None
        try:
            import RPi.GPIO as GPIO
            self.GPIO = GPIO
        except:
            pass
       
        # SETUP GPIO PORTS
        self.BUTTON_P1 = 12
        self.BUTTON_RESET = 20
        self.BUTTON_P2 = 16
        self.BUZZER = 21
        
        if self.GPIO != None:

            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.BUTTON_RESET, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.setup(self.BUTTON_P1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.setup(self.BUTTON_P2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.setup(self.BUZZER, GPIO.OUT)
            GPIO.add_event_detect(self.BUTTON_P1, GPIO.FALLING, callback=self.button_callback, bouncetime=1000)
            GPIO.add_event_detect(self.BUTTON_P2, GPIO.FALLING, callback=self.button_callback, bouncetime=1000)
            GPIO.add_event_detect(self.BUTTON_RESET, GPIO.FALLING, callback=self.button_callback, bouncetime=1000)

    def button_callback(self, channel):
        if channel == self.BUTTON_P1:
            event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT)
        if channel == self.BUTTON_P2:
            event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT)
        if channel == self.BUTTON_RESET:
            event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN)

        pygame.event.post(event)

