from BaseImage import BaseImage
from Image import Image
from Histogram import Histogram
from ImageDiffMethod import ImageDiffMethod

"""
    Klasa reprezentujaca obraz, jego histogram oraz metody porównania
"""


class ImageComparison(BaseImage):

    def histogram(self) -> Histogram:
        return Histogram(self.data)

    """
        metoda zwracajaca mse lub rmse dla dwoch obrazow
    """
    def compare_to(self, other: Image, method: ImageDiffMethod) -> float:
        if method.is_mse():
            return self.__count_mse(self, other)
        if method.is_rmse():
            return self.__count_rmse(self, other)

    def __count_mse(self, other: Image):
        first_img = self.to_gray()
        second_img = other.to_gray()
        return 0.0
