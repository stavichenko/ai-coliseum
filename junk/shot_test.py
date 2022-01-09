import numpy as np
from utils import walk_ship, make_shoot

field = np.array(
    [
        [0, 0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
)

make_shoot(field, 2, 0)
print(field, '\n')

make_shoot(field, 2, 1)
print(field, '\n')

make_shoot(field, 2, 2)
print(field, '\n')

make_shoot(field, 2, 4)
print(field, '\n')

make_shoot(field, 2, 5)
print(field, '\n')

make_shoot(field, 2, 7)
print(field, '\n')