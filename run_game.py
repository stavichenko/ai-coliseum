import numpy as np
from players import AbstractPlayer
from exceptions import DisqualificationException
from competitors import player1, player2
from utils import walk_ship


field1 = player1.get_setup()
field2 = player2.get_setup()


def player_session(player: AbstractPlayer, field: np.ndarray):
    status = 3
    while status > 2:
        try:
            x, y = player.get_move()

            if field[x, y] == 0:
                field[x, y] = 2
            elif field[x, y] == 1:
                field[x, y] = 3
                bounds, sibling = walk_ship(field, [y, x])
                if 1 not in sibling:
                    for iy, ix in bounds:
                        field[iy, ix] = 4
                # todo: add misses if hurt at least twice

            player.notify(x, y, field[x, y])
        except Exception:
            raise DisqualificationException()
    return


while True:
    player_session(player1, field2)
    player_session(player2, field1)
