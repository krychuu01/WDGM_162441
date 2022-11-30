import math

from BaseImage import BaseImage
from Histogram import Histogram
from ImageDiffMethod import ImageDiffMethod
from GrayScaleTransform import GrayScaleTransform

"""
    Klasa reprezentujaca obraz, jego histogram oraz metody porównania
"""


class ImageComparison(BaseImage):

    def __init__(self, baseImg: BaseImage):
        super().__init__(baseImg.data, baseImg.color_model)

    """
        metoda zwracajaca mse lub rmse dla dwoch obrazow
    """

    def compare_to(self, other: BaseImage, method: ImageDiffMethod) -> float:
        if method == ImageDiffMethod.mse:
            return self.__count_mse(other)
        if method == ImageDiffMethod.rmse:
            return self.__count_rmse(other)
    @classmethod
    def get_histogram(cls, baseImg: BaseImage) -> Histogram:
        gray = GrayScaleTransform(baseImg).to_gray()
        return Histogram(gray.data)

    def histogram(self) -> Histogram:
        return Histogram(self.data)

    def __count_mse(self, other: BaseImage) -> float:
        first_img = self.get_histogram(self).values
        second_img = self.get_histogram(other).values
        sum_ = 0
        n = len(first_img)
        for i in range(n):
            sum_ += (first_img[i] - second_img[i]) ** 2
        return sum_ * 1/n

    def __count_rmse(self, other) -> float:
        first_img = self.get_histogram(self).values
        second_img = self.get_histogram(other).values
        sum_ = 0
        n = len(first_img)
        for i in range(n):
            sum_ += 1/n * (first_img[i] - second_img[i]) ** 2
        return math.sqrt(sum_) * 1/n
