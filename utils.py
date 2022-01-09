import numpy as np


ships_set = np.array([4, 3, 2, 1])


def validate_field(field: np.ndarray):
    """
    Validate ships setup on given field
    :param field:
    :return:
    """

    return True


def walk_ship(field, p):
    state = field[tuple(p)]
    bounds = np.stack([p, p])
    siblings = np.zeros([2, 2])
    steps = [-1, 1]

    for dim in 0, 1:
        for dir in 0, 1:
            while field[tuple(bounds[dir])] == state:
                bounds[dir, dim] += steps[dir]
                if bounds[dir, dim] < 0 or bounds[dir, dim] >= field.shape[dim]:
                    siblings[dir, dim] = 0
                    break
            else:
                siblings[dir, dim] = field[tuple(bounds[dir])]

            bounds[dir, dim] += -steps[dir]

    bounds[1, :] += 1

    return bounds, siblings


def make_shoot(field, x, y):
    if field[y, x] == 0:
        # mark as known empty
        field[y, x] = 2
    elif field[y, x] == 1:
        # mark as hurt
        field[y, x] = 3

        bounds, siblings = walk_ship(field, [y, x])

        if 1 not in siblings:
            # mark as killed and add known empty border
            y1, y2 = max(bounds[0, 0] - 1, 0), min(bounds[1, 0] + 1, field.shape[0])
            x1, x2 = max(bounds[0, 1] - 1, 0), min(bounds[1, 1] + 1, field.shape[1])

            for iy in range(y1, y2):
                for ix in range(x1, x2):
                    if (bounds[0, 0] <= iy < bounds[1, 0]) and (bounds[0, 1] <= ix < bounds[1, 1]):
                        field[iy, ix] = 4
                    else:
                        field[iy, ix] = 2


def is_alive(field: np.ndarray, x, y):
    """
    Checks if ship under x, y coordinates is alive
    :param field:
    :return:
    """
    for dir in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        edge = walk_ship(field, (y, x), dir)
        if edge == 1:
            return True

    return False
