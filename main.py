import time

import numpy as np

import settings
from devices.distance_meter import DistanceMeter
from devices.speaker import Speaker


class Controller:
    def __init__(self):
        self.distance = DistanceMeter()
        self.distances = np.zeros(10)

        self.array_filled = False
        self.player = Speaker()
        self.time_last_played = 0
        print('main initialized')

    def loop(self):
        distance_index = 0
        while True:
            # Measure distance
            distance = self.distance.measure_distance()
            print('distance', distance)

            # Fill distances array
            self.distances[distance_index] = distance
            distance_index += 1

            if distance_index >= len(self.distances):
                self.array_filled = True
                distance_index = 0

            time.sleep(0.1)

            # Check conditions to play sound
            if not self.array_filled:
                continue
            if time.time() - self.time_last_played < settings.PLAY_TIMEOUT:
                continue
            if abs(distance - np.mean(
                    self.distances)) < settings.TRIGGER_DISTANCE:
                continue

            # Play sound
            self.player.play_random(settings.SOUNDS_FOLDER)
            self.time_last_played = time.time()

if __name__ == '__main__':
    controller = Controller()
    controller.loop()
