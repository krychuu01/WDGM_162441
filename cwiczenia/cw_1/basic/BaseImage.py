import numpy as np
import ColorModel
from matplotlib.image import imread
from matplotlib.pyplot import imshow
from matplotlib.image import imsave


class BaseImage:
    data: np.ndarray  # tensor przechowujacy piksele obrazu
    color_model: ColorModel  # atrybut przechowujacy biezacy model barw obrazu

    """
        inicjalizator wczytujacy obraz do atrybutu data na podstawie sciezki

    """
    def __init__(self, path: str) -> None:
        self.data = imread(path)
        pass

    """
        metoda zapisujaca obraz znajdujacy sie w atrybucie data do pliku
    """
    def save_img(self, path: str) -> None:
        imsave('image.jpg', self.data)
        pass

    """
        metoda wyswietlajaca obraz znajdujacy sie w atrybucie data
    """
    def show_img(self) -> None:
        imshow(self.data)
        pass

    def get_layer(self, layer_id: int) -> 'BaseImage':
        """
        metoda zwracajaca warstwe o wskazanym indeksie
        """
        pass

    def to_hsv(self) -> 'BaseImage':
        """
        metoda dokonujaca konwersji obrazu w atrybucie data do modelu hsv
        metoda zwraca nowy obiekt klasy image zawierajacy obraz w docelowym modelu barw
        """
        pass

    def to_hsi(self) -> 'BaseImage':
        """
        metoda dokonujaca konwersji obrazu w atrybucie data do modelu hsi
        metoda zwraca nowy obiekt klasy image zawierajacy obraz w docelowym modelu barw
        """
        pass

    def to_hsl(self) -> 'BaseImage':
        """
        metoda dokonujaca konwersji obrazu w atrybucie data do modelu hsl
        metoda zwraca nowy obiekt klasy image zawierajacy obraz w docelowym modelu barw
        """
        pass

    def to_rgb(self) -> 'BaseImage':
        """
        metoda dokonujaca konwersji obrazu w atrybucie data do modelu rgb
        metoda zwraca nowy obiekt klasy image zawierajacy obraz w docelowym modelu barw
        """
        pass