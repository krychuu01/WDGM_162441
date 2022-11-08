import numpy as np


class Histogram:
    """
        klasa reprezentujaca histogram danego obrazu
        """
    values: np.ndarray  # atrybut przechowujacy wartosci histogramu danego obrazu

    def __init__(self, values: np.ndarray) -> None:
        self.values = values

    def plot(self) -> None:
        """
        metoda wyswietlajaca histogram na podstawie atrybutu values
        """
        pass
