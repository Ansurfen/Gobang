from pygame.constants import *
from pygame.time import *

class Timer:
    def __init__(self):
        self.sec = 0
        self.minus = 0
        self.hour = 0
        self.stop = False
        self.TIMEOUT = USEREVENT + 1
        self.clock = Clock()

    def add(self):
        self.sec += 1
        self.minus += self.sec // 60
        self.hour += self.minus // 60
        self.sec %= 60
        self.minus %= 60

    def toString(self):
        return str(self.hour) + ':' + str(self.minus) + ':' + str(self.sec)