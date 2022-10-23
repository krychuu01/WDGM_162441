import math

import matplotlib.pyplot as plt
import numpy as np

from WDGM_162441.cwiczenia.cw_2.ColorModel import ColorModel

from matplotlib.colors import hsv_to_rgb
from matplotlib.image import imread
from matplotlib.pyplot import imshow
from matplotlib.image import imsave
from typing import Any


class BaseImage:
    data: np.ndarray  # tensor przechowujacy piksele obrazu
    color_model: ColorModel  # atrybut przechowujacy biezacy model barw obrazu

    def __init__(self, data: Any, color_model: ColorModel) -> None:
        if data is None:
            self.data = None
        elif isinstance(data, str):
            self.data = imread(data)
        else:
            self.data = data
        self.color_model = color_model

    def save_img(self) -> None:
        imsave('image.jpg', self.data)

    def show_img(self) -> None:
        imshow(self.data)
        plt.title(self.color_model.name)
        plt.show()

    def show_img_without_axis(self) -> None:
        imshow(self.data)
        plt.title(self.color_model.name)
        plt.axis('off')
        plt.show()

    @classmethod
    def show_all_plots(cls, rgb, hsv, hsi, hsl) -> None:
        figure, axis = plt.subplots(2, 2)
        axis[0][0].imshow(rgb.data)
        axis[0][0].set_title("before any conversion")
        axis[0][1].imshow(hsv.data)
        axis[0][1].set_title("after hsv conversion")
        axis[1][0].imshow(hsi.data)
        axis[1][0].set_title("after hsi conversion")
        axis[1][1].imshow(hsl.data)
        axis[1][1].set_title("after hsl conversion")
        figure.set_figwidth(10)
        figure.set_figheight(9)
        plt.show()

    def show_as_rgb_layers(self) -> None:
        r_layer, g_layer, b_layer = np.squeeze(np.dsplit(self.data, self.data.shape[-1]))
        f, axis_arr = plt.subplots(1, 3)
        axis_arr[0].imshow(r_layer, cmap='gray')
        axis_arr[1].imshow(g_layer, cmap='gray')
        axis_arr[2].imshow(b_layer, cmap='gray')
        f.set_figwidth(12)
        f.set_figheight(6)
        axis_arr[1].set_title(self.color_model.name)
        plt.show()

    def get_img_layers(self) -> []:
        return np.squeeze(np.dsplit(self.data, self.data.shape[-1]))

    """
        metoda zwracajaca warstwe o wskazanym indeksie
    """

    def get_layer(self, layer_id: int) -> 'BaseImage':
        return self.data[:, :, layer_id]

    """
        metoda dokonujaca konwersji obrazu w atrybucie data do modelu hsv
        metoda zwraca nowy obiekt klasy image zawierajacy obraz w docelowym modelu barw
    """

    def to_hsv(self) -> 'BaseImage':
        red, green, blue = self.get_img_layers() / 255.0
        M = np.max([red, green, blue], axis=0)
        m = np.min([red, green, blue], axis=0)
        V = M / 255
        S = np.where(M > 0, 1 - m / M, 0)
        additionMinusSubtraction = np.power(red, 2) + np.power(green, 2) + np.power(blue, 2) - red * green - red * blue - green * blue
        H = np.where(green >= blue,
                     np.cos((red - green / 2.0 - blue / 2.0) / np.sqrt(additionMinusSubtraction)) ** (-1),
                     360 - np.cos((red - green / 2.0 - blue / 2.0) / np.sqrt(additionMinusSubtraction)) ** (-1))

        return BaseImage(np.dstack((H, S, V)), ColorModel.hsv)

    def hsv_to_rgb(self) -> 'BaseImage':
        if self.color_model != ColorModel.hsv:
            raise Exception("color_model must be hsv to use this method!")
        H, S, V = self.get_img_layers()
        M = 255 * V
        m = M * (1 - S)
        z = (M - m) * (1 - np.fabs(((H / 60) % 2) - 1))
        r = np.where(H >= 300, M, np.where(H >= 240, z + m, np.where(H >= 120, m, np.where(H >= 60, z + m, M))))
        g = np.where(H >= 300, z + m, np.where(H >= 240, m, np.where(H >= 120, M, np.where(H >= 60, M, z + m))))
        b = np.where(H >= 300, m, np.where(H >= 240, M, np.where(H >= 120, z + m, m)))

        return BaseImage(np.dstack((r, g, b)), ColorModel.rgb)


    """
        metoda dokonujaca konwersji obrazu w atrybucie data do modelu hsi
        metoda zwraca nowy obiekt klasy image zawierajacy obraz w docelowym modelu barw
    """

    def to_hsi(self) -> 'BaseImage':
        red, green, blue = self.get_img_layers() / 255.0
        M = np.max([red, green, blue], axis=0)
        m = np.min([red, green, blue], axis=0)
        I = (red + green + blue) / 3.0
        S = np.where(M > 0, 1 - m / M, 0)
        additionMinusSubtraction = red ** 2 + green ** 2 + blue ** 2 - red * green - red * blue - green * blue
        H = np.where(green >= blue,
                     np.cos((red - green / 2 - blue / 2) / np.sqrt(additionMinusSubtraction)) ** (-1),
                     360 - np.cos((red - green / 2 - blue / 2) / np.sqrt(additionMinusSubtraction)) ** (-1))

        return BaseImage(np.dstack((H, S, I)), ColorModel.hsi)

    def hsi_to_rgb(self) -> 'BaseImage':
        if self.color_model != ColorModel.hsi:
            raise Exception("color_model must be hsi to use this method!")
        H, S, I = self.get_img_layers()
        IS = I * S
        r = np.where(H > 240, I + IS * np.fabs(1 - np.cos(H - 240) / np.cos(300 - H)), np.where(H >= 120, I - IS, np.where(H > 0.99, I + IS * np.cos(H)/np.cos(60-H), I + 2 * IS)))
        g = np.where(H >= 240, I - IS, np.where(H > 120, I + IS * np.cos(H - 120) / np.cos(180 - H), np.where(np.logical_and(119.99 < H, H < 120.99), I + 2 * IS, np.where(H > 0.99, I + IS * np.fabs(1 - np.cos(H) / np.cos(60 - H)), I - IS))))
        b = np.where(H > 240, I + IS * np.cos(H - 240) / np.cos(300 - H), np.where(H == 240, I + 2 * IS, np.where(H > 120, I + IS * np.fabs(1 - np.cos(H - 120)/np.cos(180-H)), I - IS)))

        return BaseImage(np.dstack((r, g, b)), ColorModel.rgb)

    def to_hsl(self) -> 'BaseImage':
        red, green, blue = self.get_img_layers() / 255.0
        M = np.max([red, green, blue], axis=0)
        m = np.min([red, green, blue], axis=0)
        L = (0.5 * (M + m)) / 255
        d = (M - m) / 255
        S = np.where(L > 0, d / (1 - np.fabs(2 * L - 1)), 0)
        # S = np.where(M > 0, 1 - m / M, 0)
        additionMinusSubtraction = np.power(red, 2) + np.power(green, 2) + np.power(blue, 2) - red * green - red * blue - green * blue
        H = np.where(green >= blue,
                     np.cos((red - green / 2.0 - blue / 2.0) / np.sqrt(additionMinusSubtraction)) ** (-1),
                     360 - np.cos((red - green / 2.0 - blue / 2.0) / np.sqrt(additionMinusSubtraction)) ** (-1))

        return BaseImage(np.dstack((H, S, L)), ColorModel.hsl)

    def hsl_to_rgb(self) -> 'BaseImage':
        if self.color_model != ColorModel.hsl:
            raise Exception("to use this method, color model of img must be hsl!")
        H, S, L = self.get_img_layers()
        d = S * (1 - np.fabs(2 * L - 1))
        m = 255 * (L - 0.5 * d)
        x = d * (1 - np.fabs(((H / 60) % 2) - 1))
        r = np.where(H >= 300, 255 * d + m, np.where(H >= 240, 255 * x + m, np.where(H >= 120, m, np.where(H >= 60, 255 * x + m, 255 * d + m))))
        g = np.where(H >= 240, m, np.where(H >= 180, 255 * x + m, np.where(H >= 120, 255 * d + m, np.where(H >= 60, 255 * d + m, 255 * x + m))))
        b = np.where(H >= 300, 255 * x + m, np.where(H >= 240, 255 * d + m, np.where(H >= 180, 255 * d + m, np.where(H >= 120, 255 * x + m, m))))
        return BaseImage(np.dstack((r, g, b)), ColorModel.rgb)

    """
        metoda dokonujaca konwersji obrazu w atrybucie data do modelu rgb
        metoda zwraca nowy obiekt klasy image zawierajacy obraz w docelowym modelu barw
    """

    def to_rgb(self) -> 'BaseImage':
        if self.color_model == ColorModel.hsv:
            return self.hsv_to_rgb()
        if self.color_model == ColorModel.hsi:
            return self.hsi_to_rgb()
        if self.color_model == ColorModel.hsl:
            return self.hsl_to_rgb()

