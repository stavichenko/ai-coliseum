from players import AbstractPlayer
import numpy as np


class ProbabilityPlayer(AbstractPlayer):
    def __init__(self):
        self.field = np.array([AbstractPlayer.config["field_size"]])
        self.opponent_field = np.array([AbstractPlayer.config["field_size"]])

    def get_setup(self):
        return self.field

    def get_move(self):
        pass

    def notify(self, x, y, status):
        pass

    def bound_zeroes(self, ship: np.array):
        x0 = min(ship[:, 0])
        y0 = min(ship[:, 1])
        x0 = x0 if (x0 - 1) < 0 else x0 - 1
        y0 = y0 if (y0 - 1) < 0 else y0 - 1

        x1 = max(ship[:, 0])
        y1 = max(ship[:, 1])
        x1 = x1 if (x1 + 1) > self.field.shape[0] - 1 else x1 + 1
        y1 = y1 if (y1 + 1) > self.field.shape[0] - 1 else y1 + 1

        for i in range(x0, x1 + 1):
            for j in range(y0, y1 + 1):
                self.field[i, j] = 0 if not self.field[i, j] else 1


player = ProbabilityPlayer()
