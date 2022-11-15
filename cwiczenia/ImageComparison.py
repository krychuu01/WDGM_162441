import math

from BaseImage import BaseImage
from Histogram import Histogram
from ImageDiffMethod import ImageDiffMethod
from GrayScaleTransform import GrayScaleTransform

"""
    Klasa reprezentujaca obraz, jego histogram oraz metody porównania
"""


class ImageComparison(BaseImage):

    """
        metoda zwracajaca mse lub rmse dla dwoch obrazow
    """

    def compare_to(self, other: BaseImage, method: ImageDiffMethod) -> float:
        if method == ImageDiffMethod.mse:
            return self.__count_mse(other)
        if method == ImageDiffMethod.rmse:
            return self.__count_rmse(other)
    @classmethod
    def __get_histogram(cls, image: BaseImage) -> Histogram:
        gray = GrayScaleTransform(image.data, image.color_model).to_gray()
        return Histogram(gray.data)

    def histogram(self) -> Histogram:
        return Histogram(self.data)

    def __count_mse(self, other: BaseImage) -> float:
        first_img = self.__get_histogram(self)
        second_img = self.__get_histogram(other)
        sum_ = 0
        n = 3
        for i in range(n):
            sum_ += (first_img.values[i] - second_img.values[i]) ** 2
        return sum_

    def __count_rmse(self, other) -> float:
        first_img = self.__get_histogram(self)
        second_img = self.__get_histogram(other)
        sum_ = 0
        n = 3
        for i in range(n):
            sum_ += (first_img.values[i] - second_img.values[i]) ** 2
            sum_ = math.sqrt(sum_)
        return sum_
