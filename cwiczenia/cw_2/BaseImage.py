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
        if self.color_model == ColorModel.rgb or self.color_model is None:
            imshow(self.data.astype('uint8'))
        else:
            imshow(self.data.astype('uint16'))
        plt.show()

    def show_img_without_axis(self) -> None:
        if self.color_model == ColorModel.rgb or self.color_model is None:
            imshow(self.data.astype('uint8'))
        else:
            hsv_to_rgb(self.data)
        plt.axis('off')
        plt.show()

    def show_as_rgb_layers(self) -> None:
        r_layer, g_layer, b_layer = np.squeeze(np.dsplit(self.data, self.data.shape[-1]))
        f, axis_arr = plt.subplots(1, 3)
        axis_arr[0].imshow(r_layer, cmap='gray')
        axis_arr[1].imshow(g_layer, cmap='gray')
        axis_arr[2].imshow(b_layer, cmap='gray')
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
        red, green, blue = self.get_img_layers()
        M = np.max([red, green, blue], axis=0)
        m = np.min([red, green, blue], axis=0)
        V = M / 255
        S = np.where(M > 0, 1 - m / M, 0)
        additionMinusSubtraction = np.double(
            np.power(red, 2) + np.power(green, 2) + np.power(blue, 2) - red * green - red * blue - green * blue)
        H = np.where(green >= blue,
                     np.cos((red - green / 2.0 - blue / 2.0) / np.sqrt(additionMinusSubtraction)) ** (-1),
                     360 - np.cos((red - green / 2.0 - blue / 2.0) / np.sqrt(additionMinusSubtraction)) ** (-1))

        data_np = np.dstack((H, S, V))
        return BaseImage(data_np, ColorModel.hsv)

    def hsv_to_rgb(self) -> 'BaseImage':
        self.data = self.data.copy()
        if self.color_model != ColorModel.hsv:
            raise Exception("color_model must be hsv to use this method!")
        for pixel in self.data:
            for color in pixel:
                H, S, V = color[0], color[1], color[2]
                M = 255 * V
                m = M * (1 - S)
                z = (M - m) * (1 - math.fabs(((H / 60) % 2) - 1))
                if H >= 300:
                    color[0] = M
                    color[1] = z + m
                    color[2] = m
                elif H >= 240:
                    color[0] = z + m
                    color[1] = m
                    color[2] = M
                elif H >= 180:
                    color[0] = m
                    color[1] = M
                    color[2] = z + m
                elif H >= 120:
                    color[0] = m
                    color[1] = M
                    color[2] = z + m
                elif H >= 60:
                    color[0] = z + m
                    color[1] = M
                    color[2] = m
                elif H >= 0:
                    color[0] = M
                    color[1] = z + m
                    color[2] = m
        self.color_model = ColorModel.rgb
        return self


    """
        metoda dokonujaca konwersji obrazu w atrybucie data do modelu hsi
        metoda zwraca nowy obiekt klasy image zawierajacy obraz w docelowym modelu barw
    """

    def to_hsi(self) -> 'BaseImage':
        red, green, blue = self.get_img_layers()
        M = np.max([red, green, blue], axis=0)
        m = np.min([red, green, blue], axis=0)
        I = (red + green + blue) / 3
        S = np.where(M > 0, 1 - m / M, 0)
        additionMinusSubtraction = red ** 2 + green ** 2 + blue ** 2 - red * green - red * blue - green * blue
        H = np.where(green >= blue,
                     np.cos((red - green / 2 - blue / 2) / np.sqrt(additionMinusSubtraction)) ** (-1),
                     360 - np.cos((red - green / 2 - blue / 2) / np.sqrt(additionMinusSubtraction)) ** (-1))

        data_np = np.dstack((H, S, I))
        return BaseImage(data_np, ColorModel.hsi)

    def hsi_to_rgb(self) -> 'BaseImage':
        self.data = self.data.copy()
        if self.color_model != ColorModel.hsi:
            raise Exception("color_model must be hsi to use this method!")
        for pixel in self.data:
            for color in pixel:
                H, S, I = color[0], color[1], color[2]
                if H >= 240:
                    color[0] = I + I * S * (1 - math.cos(H - 240) / math.cos(300 - H))
                    color[1] = I - I * S
                    color[2] = I + I * S * (math.cos(H - 240) / math.cos(300 - H))
                elif H == 240:
                    color[0] = I - I * S
                    color[1] = I - I * S
                    color[2] = I + 2 * I * S
                elif H > 120:
                    color[0] = I - I * S
                    color[1] = I + I * S * (math.cos(H - 120) / math.cos(180 - H))
                    color[2] = I + I * S * (1 - math.cos(H - 120) / math.cos(180 - H))
                elif H == 120:
                    color[0] = I - I * S
                    color[1] = I + 2 * I * S
                    color[2] = I - I * S
                elif H > 0:
                    color[0] = I + I * S * math.cos(H) / math.cos(60 - H)
                    color[1] = I + I * S * (1 - math.cos(H) / math.cos(60 - H))
                    color[2] = I - I * S
                elif H == 0:
                    color[0] = I + 2 * I * S
                    color[1] = I - I * S
                    color[2] = I - I * S
        self.color_model = ColorModel.rgb
        return self

    def to_hsl(self) -> 'BaseImage':
        self.data = self.data.copy()
        for pixel in self.data:
            for color in pixel:
                red, green, blue = color[0] / 255, color[1] / 255, color[2] / 255
                M = max(red, green, blue)
                m = min(red, green, blue)
                d = (M - m) / 255
                L = (0.5 * (M + m)) / 255
                S = d / (1 - math.fabs(2 * L - 1)) if L > 0 else 0
                addition = red ** 2 + green ** 2 + blue ** 2
                subtraction = red * green - red * blue - green * blue
                additionMinusSubtraction = addition - subtraction
                if green >= blue:
                    H = math.acos((red - green / 2 - blue / 2) / math.sqrt(additionMinusSubtraction))
                else:
                    H = 360 - math.acos((red - green / 2 - blue / 2) / math.sqrt(additionMinusSubtraction))
                color[0] = H * 255
                color[1] = S * 255
                color[2] = L * 255

        self.color_model = ColorModel.hsl
        return self

    def hsl_to_rgb(self) -> 'BaseImage':
        self.data = self.data.copy()
        if self.color_model != ColorModel.hsl:
            raise Exception("color_model must be hsl to use this method!")
        for pixel in self.data:
            for color in pixel:
                H, S, L = color[0], color[1], color[2]
                d = S * (1 - math.fabs(2 * L - 1))
                m = 255 * (L - 0.5 * d)
                x = d * (1 - (math.fabs(((H / 60) % 2) - 1)))
                if H > 300:
                    color[0] = 255 * d + m
                    color[1] = m
                    color[2] = 255 * x + m
                elif H > 240:
                    color[0] = 255 * x + m
                    color[1] = m
                    color[2] = 255 * d + m
                elif H > 180:
                    color[0] = m
                    color[1] = 255 * x + m
                    color[2] = 255 * d + m
                elif H > 120:
                    color[0] = m
                    color[1] = 255 * d + m
                    color[2] = 255 * x + m
                elif H > 60:
                    color[0] = 255 * x + m
                    color[1] = 255 * d + m
                    color[2] = m
                elif H > 0:
                    color[0] = 255 * d + m
                    color[1] = 255 * x + m
                    color[2] = m
        self.color_model = ColorModel.rgb
        return self

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
