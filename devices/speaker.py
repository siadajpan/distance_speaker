from playsound import playsound


class Speaker:
    def play(self):
        playsound('/home/karol/Downloads/sweep.wav')


if __name__ == '__main__':
    s = Speaker()
    s.play()

