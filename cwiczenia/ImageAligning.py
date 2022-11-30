import math
from typing import Any

from BaseImage import BaseImage
from ColorModel import ColorModel
from Histogram import Histogram
from GrayScaleTransform import GrayScaleTransform


import numpy as np


class ImageAligning(BaseImage):

    def __init__(self, baseImg: BaseImage) -> None:
        super().__init__(baseImg.data, baseImg.color_model)

    def align_image(self, tail_elimination: bool = True) -> 'BaseImage':
        gray_scale = GrayScaleTransform(self).to_gray()
        min_pixel = np.min(gray_scale.data)
        max_pixel = np.max(gray_scale.data)
        max_minus_min = max_pixel - min_pixel

        for r in range(512):
            for c in range(512):
                gray_scale.data[r][c] = (gray_scale.data[r][c] - min_pixel) * 255/max_minus_min

        return BaseImage(gray_scale.data.astype('uint8'), color_model=ColorModel.gray)


