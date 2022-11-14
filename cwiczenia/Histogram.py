import numpy as np
import matplotlib.pyplot as plt

"""
    klasa reprezentujaca histogram danego obrazu
"""


class Histogram:
    values: np.ndarray  # atrybut przechowujacy wartosci histogramu danego obrazu

    def __init__(self, values: np.ndarray) -> None:
        if values.ndim == 2:
            self.values = np.histogram(values, bins=256, range=(0, 255))[0]
        else:
            first_layer, second_layer, third_layer = np.squeeze(np.dsplit(values, values.shape[-1]))
            first_layer = np.histogram(first_layer, bins=256, range=(0, 255))[0]
            second_layer = np.histogram(second_layer, bins=256, range=(0, 255))[0]
            third_layer = np.histogram(third_layer, bins=256, range=(0, 255))[0]
            self.values = np.dstack((first_layer, second_layer, third_layer))

    """
        metoda wyswietlajaca histogram na podstawie atrybutu values
    """

    def plot(self) -> None:
        if self.__is_three_dimensional():
            self.__show_multiple_histograms()
        else:
            self.__show_single_histogram()
        plt.show()

    def __show_single_histogram(self):
        plt.figure(figsize=(5, 6))
        plt.title("gray scale")
        plt.xlim([0, 256])
        bin_edges = np.linspace(0, 255, 256)
        plt.plot(bin_edges, self.values, color="gray")

    def __show_multiple_histograms(self):
        plt.figure(figsize=(15, 6))
        num = 1
        bin_edges = np.linspace(0, 255, 256)
        for layer in self.__get_img_layers():
            plt.subplot(1, 3, num)
            plt.title(self.__color_num(num))
            plt.xlim([0, 256])
            plt.plot(bin_edges, layer, color=self.__color_num(num))
            num += 1

    def __color_num(self, num: int) -> str:
        if num == 1:
            return "red"
        if num == 2:
            return "green"
        if num == 3:
            return "blue"

    def __get_img_layers(self) -> []:
        return np.squeeze(np.dsplit(self.values, self.values.shape[-1]))

    def __get_dimension(self) -> int:
        return self.values.ndim

    def __is_three_dimensional(self) -> bool:
        return self.__get_dimension() == 3
