import numpy as np
import cv2
from dataclasses import dataclass
from rules import validate_field


@dataclass
class FieldStyle:
    empty_color = (220, 240, 250)
    filled_color = (0, 140, 40)
    miss_color = (0, 140, 40)
    miss_radius = 5
    grid_line_color = (0, 0, 0)
    grid_line_size = 1
    cell_size = 30
    cross_size = 3


def draw_field(field: np.ndarray, stl=FieldStyle()) -> np.ndarray:
    w = field.shape[1] * stl.cell_size + (field.shape[1] + 1) * stl.grid_line_size
    h = field.shape[0] * stl.cell_size + (field.shape[0] + 1) * stl.grid_line_size
    img = np.zeros((h, w, 3), 'uint8')

    pad = stl.grid_line_size

    img[0:pad, :] = stl.grid_line_color
    img[:, 0:pad] = stl.grid_line_color

    for i in range(field.shape[0]):
        for j in range(field.shape[1]):
            x1 = pad * (j + 1) + j * stl.cell_size
            x2 = x1 + stl.cell_size

            y1 = pad * (i + 1) + i * stl.cell_size
            y2 = y1 + stl.cell_size

            if field[i, j] == 0:
                cv2.rectangle(img, (x1, y1), (x2,y2), stl.empty_color, -1)
            elif field[i, j] == 1:
                cv2.rectangle(img, (x1, y1), (x2,y2), stl.filled_color, -1)
            elif field[i, j] == 2:
                cv2.rectangle(img, (x1, y1), (x2,y2), stl.empty_color, -1)
                cv2.circle(img, ((x2 - x1) // 2, (y2 - y1) // 2), stl.miss_radius, stl.miss_color, -1)
            elif field[i, j] == 3:
                cv2.line(img, (x1, y1), (x2, y2), stl.filled_color, stl.cross_size)

            img[y2:y2+pad, x1:x2] = stl.grid_line_color
            img[y1:y2, x2:x2+pad] = stl.grid_line_color

    return img


def read_human_setup(field: np.ndarray, stl=FieldStyle()):
    def mouse_callback(event, px, py, flags, param):
        if event != cv2.EVENT_LBUTTONUP:
            return

        cell_size = stl.grid_line_size + stl.cell_size

        x = np.ceil(px / cell_size).astype(int) - 1
        y = np.ceil(py / cell_size).astype(int) - 1

        field[y, x] = 1 - field[y, x]

    cv2.namedWindow('setup')
    cv2.setMouseCallback('setup', mouse_callback)

    valid_setup = False

    while True:
        img = draw_field(field, stl)
        cv2.imshow('setup', img)
        key = cv2.waitKey(20)
        if key == 13 and valid_setup:
            break

        valid_setup = validate_field(field)

    return field
