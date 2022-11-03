from cwiczenia.cw_3.GrayScaleTransform import GrayScaleTransform
from cwiczenia.cw_4.ImageComparison import ImageComparison


class Image(GrayScaleTransform, ImageComparison):
    """
    klasa stanowiaca glowny interfejs biblioteki
    w pozniejszym czasie bedzie dziedziczyla po kolejnych klasach
    realizujacych kolejne metody przetwarzania obrazow
    """
    def __init__(self) -> None:
        super().__init__()