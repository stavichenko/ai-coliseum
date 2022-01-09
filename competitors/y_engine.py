from players import AbstractPlayer
import numpy as np


class YPlayer(AbstractPlayer):
    def __init__(self):
        self.opponent_field = np.zeros([10, 10])

    def get_setup(self):
        return np.zeros([10, 10])

    def get_move(self):
        pass

    def notify(self, x, y, status):
        self.opponent_field[x, y] = status


player = YPlayer()
