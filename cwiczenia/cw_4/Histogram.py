import numpy as np
import matplotlib.pyplot as plt

"""
    klasa reprezentujaca histogram danego obrazu
"""


class Histogram:
    values: np.ndarray  # atrybut przechowujacy wartosci histogramu danego obrazu

    def __init__(self, values: np.ndarray) -> None:
        self.values = values

    """
        metoda wyswietlajaca histogram na podstawie atrybutu values
    """

    def plot(self) -> None:
        # if self.values.shape
        pass

    def __get_img_layers(self) -> []:
        return np.squeeze(np.dsplit(self.data, self.data.shape[-1]))
