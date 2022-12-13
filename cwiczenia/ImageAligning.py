
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
            return self.__get_aligned_image_with_tail_elimination()

    def __align(self, layer: np.ndarray) -> np.ndarray:
        min_pixel = np.min(layer)
        max_pixel = np.max(layer)
        max_minus_min = max_pixel - min_pixel
        aligned = np.multiply(np.subtract(layer, min_pixel), 255 / max_minus_min)
        return aligned.astype('uint8')

    def __align_with_tail_elimination(self, layer: np.ndarray) -> np.ndarray:
        cumulated_histogram = Histogram(layer).to_cumulated().values
        range_in_cumulated_hist = cumulated_histogram[-1]
        min_tail = 0
        max_tail = 0

        for value in cumulated_histogram:
            if value <= 0.05 * range_in_cumulated_hist:
                min_tail += 1
            if value <= 0.95 * range_in_cumulated_hist:
                max_tail += 1

        layer_copy = np.float64(np.copy(layer))
        max_tail_minus_min_tail = max_tail - min_tail

        aligned = ((layer_copy - min_tail) * (255 / max_tail_minus_min_tail)).astype('i')
        aligned[aligned > 255] = 255
        aligned[aligned < 0] = 0
        return aligned

    def __get_aligned_image_with_tail_elimination(self) -> BaseImage:
        if self.color_model.is_gray():
            aligned_layer = self.__align_with_tail_elimination(self.data)
            return BaseImage(aligned_layer, self.color_model)

        if not self.color_model.is_gray():
            first_layer, second_layer, third_layer = self.get_img_layers()
            first_layer = self.__align_with_tail_elimination(first_layer)
            second_layer = self.__align_with_tail_elimination(second_layer)
            third_layer = self.__align_with_tail_elimination(third_layer)
            aligned_layers = np.dstack((first_layer, second_layer, third_layer))
            return BaseImage(aligned_layers, self.color_model)

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
