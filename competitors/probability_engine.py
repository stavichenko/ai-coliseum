from players import AbstractPlayer
import numpy as np


class ProbabilityPlayer(AbstractPlayer):
    def get_setup(self):
        return np.zeros([10, 10])

    def get_move(self):
        pass

    def notify(self, x, y, status):
        pass


player = ProbabilityPlayer()