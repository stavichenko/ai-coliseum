import numpy as np


def validate_field(field: np.ndarray):
    """
    Validate ships setup on given field
    :param field:
    :return:
    """
    raise NotImplementedError()


def is_alive(field: np.ndarray):
    """
    Checks if player has at least one alive ship
    :param field:
    :return:
    """
    raise NotImplementedError()