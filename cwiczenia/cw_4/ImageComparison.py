from cwiczenia.cw_2.BaseImage import BaseImage
from cwiczenia.cw_3.Image import Image
from cwiczenia.cw_4.Histogram import Histogram
from cwiczenia.cw_4.ImageDiffMethod import ImageDiffMethod


class ImageComparison(BaseImage):
    """
    Klasa reprezentujaca obraz, jego histogram oraz metody porównania
    """

    def histogram(self) -> Histogram:
        """
        metoda zwracajaca obiekt zawierajacy histogram biezacego obrazu (1- lub wielowarstwowy)
        """
        pass

    def compare_to(self, other: Image, method: ImageDiffMethod) -> float:
        """
        metoda zwracajaca mse lub rmse dla dwoch obrazow
        """
        pass
