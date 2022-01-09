import numpy as np


ships_set = np.array([4, 3, 2, 1])


def validate_field(field: np.ndarray):
    """
    Validate ships setup on given field
    :param field:
    :return:
    """

    return False


def is_alive(field: np.ndarray):
    """
    Checks if player has at least one alive ship
    :param field:
    :return:
    """
    raise NotImplementedError()