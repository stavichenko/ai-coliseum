import numpy as np


player1 = 'human'
player2 = 'engine1'


field2 = np.zeros([10, 10])


while True:
    # todo: implement game loop
    x, y = player1.get_move()
    status = field2[x, y]
    player1.notify(x, y, status)