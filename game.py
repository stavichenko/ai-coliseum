from players import AbstractPlayer
from exceptions import DisqualificationException
from competitors import player1, player2


field1 = player1.get_setup()
field2 = player2.get_setup()


def player_session(player: AbstractPlayer):
    status = 3
    while status > 2:
        try:
            x, y = player1.get_move()
            status = field2[x, y]
            player.notify(x, y, status)
        except Exception:
            raise DisqualificationException()
    return


while True:
    player_session(player1)
    player_session(player2)
