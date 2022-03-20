import pygame
from glob import glob
import random
import os


class Speaker:
    def __init__(self):
        pygame.mixer.init()

    def play(self, path):
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

    def play_random(self, folder):
        sounds = glob(os.path.join(folder, '*'))
        random_sound = random.choice(sounds)
        print('playing sound from', random_sound)
        self.play(random_sound)

