
from GrayScaleTransform import GrayScaleTransform
from ImageComparison import ImageComparison
from ImageAligning import ImageAligning
from ImageFiltration import ImageFiltration
from Thresholding import Thresholding
from typing import Any
from ColorModel import ColorModel



class Image(GrayScaleTransform, ImageComparison, ImageAligning, ImageFiltration, Thresholding):
    """
    klasa stanowiaca glowny interfejs biblioteki
    w pozniejszym czasie bedzie dziedziczyla po kolejnych klasach
    realizujacych kolejne metody przetwarzania obrazow
    """
    def __init__(self, data: Any, color_model: ColorModel) -> None:
        super().__init__(data, color_model)
