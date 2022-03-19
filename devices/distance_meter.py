import time

import RPi.GPIO as GPIO

import settings


class DistanceMeter:
    def __init__(self):
        super().__init__()
        self.trigger = settings.TRIGGER_PIN
        self.echo = settings.ECHO_PIN
        self.stop = False
        self.setup()

    def setup(self):
        GPIO.setmode(GPIO.BCM)  # Broadcom pin-numbering scheme
        GPIO.setup(self.trigger, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)
        GPIO.output(self.trigger, GPIO.LOW)
        time.sleep(2)

    def measure_distance(self):
        GPIO.output(self.trigger, GPIO.HIGH)
        GPIO.output(self.trigger, True)
        time.sleep(0.00001)
        GPIO.output(self.trigger, False)
        while GPIO.input(self.echo) == 0:
            pulse_start = time.time()
        while GPIO.input(self.echo) == 1:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17165
        distance = round(distance, 1)
        return distance
