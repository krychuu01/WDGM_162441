
from BaseImage import BaseImage
from ColorModel import ColorModel
from Histogram import Histogram
from GrayScaleTransform import GrayScaleTransform


import numpy as np


class ImageAligning(BaseImage):

    def __init__(self, baseImg: BaseImage) -> None:
        super().__init__(baseImg.data, baseImg.color_model)

    def align_image(self, tail_elimination: bool = True) -> BaseImage:
        if tail_elimination is False:
            return self.__get_aligned_image_without_tail_elimination()
        if tail_elimination is True:
            pass

    def __align(self, layer: np.ndarray) -> np.ndarray:
        min_pixel = np.min(layer)
        max_pixel = np.max(layer)
        max_minus_min = max_pixel - min_pixel
        aligned = np.multiply(np.subtract(layer, min_pixel), 255 / max_minus_min)
        return aligned.astype('uint8')

    def __get_aligned_image_without_tail_elimination(self) -> BaseImage:
        if self.color_model.is_gray():
            aligned_layer = self.__align(self.data)
            return BaseImage(aligned_layer, self.color_model)

        if not self.color_model.is_gray():
            first_layer, second_layer, third_layer = self.get_img_layers()
            first_layer = self.__align(first_layer)
            second_layer = self.__align(second_layer)
            third_layer = self.__align(third_layer)
            aligned_layers = np.dstack((first_layer, second_layer, third_layer))
            return BaseImage(aligned_layers, self.color_model)
