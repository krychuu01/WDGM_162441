
from enum import Enum


class ColorModel(Enum):
    rgb = 0
    hsv = 1
    hsi = 2
    hsl = 3
    gray = 4  # obraz 2d
    sepia = 5

    def is_gray(self):
        return self == ColorModel.gray
