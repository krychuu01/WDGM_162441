
from GrayScaleTransform import GrayScaleTransform


class Image(GrayScaleTransform):
    """
    klasa stanowiaca glowny interfejs biblioteki
    w pozniejszym czasie bedzie dziedziczyla po kolejnych klasach
    realizujacych kolejne metody przetwarzania obrazow
    """
    def __init__(self) -> None:
        super().__init__()