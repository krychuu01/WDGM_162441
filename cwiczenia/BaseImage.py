from typing import Any

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.image import imread
from matplotlib.image import imsave
from matplotlib.pyplot import imshow
from math import sqrt, cos, acos, radians, pi

from ColorModel import ColorModel


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
        if self.color_model == ColorModel.gray:
            imshow(self.data, cmap='gray')
        else:
            imshow(self.data)
        plt.title(self.color_model.name)
        plt.show()

    def show_img_without_axis(self) -> None:
        if self.color_model == ColorModel.gray:
            imshow(self.data, cmap='gray')
        else:
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

    def get_layer(self, layer_id: int) -> 'np.ndarray':
        return self.data[:, :, layer_id]

    def __calculate_H(self, r, g, b):
        r = r.astype(int)
        g = g.astype(int)
        b = b.astype(int)
        calc = np.power(r, 2) + np.power(g, 2) + np.power(b, 2) - (r * g) - (r * b) - (g * b)
        calc_sqrt = np.sqrt(calc)
        calc_sqrt[calc_sqrt == 0] = 1
        H = np.where(g >= b,
                     np.arccos((r - (g / 2) - (b / 2)) / calc_sqrt) * 180 / pi,
                     360 - np.arccos(((r - (g / 2) - (b / 2)) / calc_sqrt)) * 180 / pi)
        return H

    """
        metoda dokonujaca konwersji obrazu w atrybucie data do modelu hsv
        metoda zwraca nowy obiekt klasy image zawierajacy obraz w docelowym modelu barw
    """
    def to_hsv(self) -> 'BaseImage':
        if self.color_model != ColorModel.rgb:
            raise Exception("Color model must be rgb!")
        red, green, blue = self.get_img_layers()
        MAX = np.max([red, green, blue], axis=0)
        MAX[MAX == 0] = 255
        MIN = np.min([red, green, blue], axis=0)
        H = self.__calculate_H(red, green, blue)
        S = np.where(MAX == 0, 0, (1 - MIN/MAX))
        V = MAX / 255
        return BaseImage(np.dstack((H, S, V)), ColorModel.hsv)

    def __hsv_to_rgb(self) -> 'BaseImage':
        if self.color_model != ColorModel.hsv:
            raise Exception("color_model must be hsv to use this method!")
        H, S, V = self.get_img_layers()
        C = V * S
        X = C * (1 - abs(((H / 60) % 2) - 1))
        m = V - C

        r = np.where(H >= 300, C, np.where(H >= 240, X, np.where(H >= 120, 0, np.where(H >= 60, X, C))))
        g = np.where(H >= 240, 0, np.where(H >= 180, X, np.where(H >= 60, C, X)))
        b = np.where(H >= 300, X, np.where(H >= 180, C, np.where(H >= 120, X, 0)))

        r = (r + m) * 255
        g = (g + m) * 255
        b = (b + m) * 255
        g[g > 255] = 255
        b[b > 255] = 255
        r[r > 255] = 255
        r[r < 0] = 0
        g[g < 0] = 0
        b[b < 0] = 0

        return BaseImage(np.dstack((r, g, b)).astype('uint8'), ColorModel.rgb)


    """
        metoda dokonujaca konwersji obrazu w atrybucie data do modelu hsi
        metoda zwraca nowy obiekt klasy image zawierajacy obraz w docelowym modelu barw
    """

    def to_hsi(self) -> 'BaseImage':
        if self.color_model != ColorModel.rgb:
            raise Exception("Color model must be RGB!")
        red, green, blue = np.float32(self.get_img_layers())
        sum_ = red + green + blue
        sum_[sum_ == 0] = 255
        r = red / sum_
        g = green / sum_
        b = blue / sum_
        MIN = np.min([r, g, b], axis=0)
        H = self.__calculate_H(red, green, blue)
        S = 1 - 3 * MIN
        I = (red + green + blue) / (3 * 255)

        return BaseImage(np.dstack((H, S, I)), ColorModel.hsi)

    def __hsi_to_rgb(self) -> 'BaseImage':
        if self.color_model != ColorModel.hsi:
            raise Exception("color_model must be hsi to use this method!")
        H, S, I = self.get_img_layers()
        h = H * np.pi / 180
        s = S
        i = I
        rows = self.data.shape[0]
        columns = self.data.shape[1]
        r = np.zeros((rows, columns))
        g = np.zeros((rows, columns))
        b = np.zeros((rows, columns))
        for k in range(rows):
            for j in range(columns):
                if h[k, j] < np.pi * 2 / 3:
                    x = i[k, j] * (1 - s[k, j])
                    y = i[k, j] * (1 + s[k, j] * np.cos(h[k, j]) / np.cos(np.pi / 3 - h[k, j]))
                    z = 3 * i[k, j] - (x + y)
                    r[k, j] = y
                    g[k, j] = z
                    b[k, j] = x
                if np.pi * 2 / 3 <= h[k, j] < np.pi * 4 / 3:
                    h[k, j] = h[k, j] - np.pi * 2 / 3
                    x = i[k, j] * (1 - s[k, j])
                    y = i[k, j] * (1 + s[k, j] * np.cos(h[k, j]) / np.cos(np.pi / 3 - h[k, j]))
                    z = 3 * i[k, j] - (x + y)
                    r[k, j] = x
                    g[k, j] = y
                    b[k, j] = z
                if np.pi * 4 / 3 < h[k, j] < np.pi * 2:
                    h[k, j] = h[k, j] - np.pi * 4 / 3
                    x = i[k, j] * (1 - s[k, j])
                    y = i[k, j] * (1 + s[k, j] * np.cos(h[k, j]) / np.cos(np.pi / 3 - h[k, j]))
                    z = 3 * i[k, j] - (x + y)
                    r[k, j] = z
                    g[k, j] = x
                    b[k, j] = y
        r[r > 1] = 1
        g[g > 1] = 1
        b[b > 1] = 1
        r = r * 255
        g = g * 255
        b = b * 255
        r[r < 0] = 0
        g[g < 0] = 0
        b[b < 0] = 0
        return BaseImage(np.dstack((r, g, b)).astype('uint8'), ColorModel.rgb)


    def to_hsl(self) -> 'BaseImage':
        if self.color_model != ColorModel.rgb:
            raise Exception("Color model must be rgb!")
        red, green, blue = self.get_img_layers()
        MAX = np.max([red, green, blue], axis=0)
        MIN = np.min([red, green, blue], axis=0)
        D = (MAX - MIN) / 255
        H = self.__calculate_H(red, green, blue)
        L = (0.5 * (MAX.astype(int) + MIN.astype(int))).astype(int) / 255
        calc = (1 - abs(2 * L - 1))
        calc[calc == 0] = 1
        S = np.where(L > 0, D / calc, 0)
        S[S > 1] = 1
        S[S < 0] = 0.001

        return BaseImage(np.dstack((H, S, L)), ColorModel.hsl)

    def __hsl_to_rgb(self) -> 'BaseImage':
        if self.color_model != ColorModel.hsl:
            raise Exception("to use this method, color model of img must be hsl!")
        H, S, L = self.get_img_layers()
        d = S * (1 - abs(2 * L - 1))
        MIN = 255 * (L - 0.5 * d)
        x = d * (1 - abs(H / 60 % 2 - 1))
        r = np.where(H >= 300, 255 * d + MIN,
                     np.where(H >= 240, 255 * x + MIN,
                              np.where(H >= 180, MIN,
                                       np.where(H >= 120, MIN,
                                                np.where(H >= 60, 255 * x + MIN, 255 * d + MIN)))))
        g = np.where(H >= 300, MIN,
                     np.where(H >= 240, MIN,
                              np.where(H >= 180, 255 * x + MIN,
                                       np.where(H >= 120, 255 * d + MIN,
                                                np.where(H >= 60, 255 * d + MIN, 255 * x + MIN)))))
        b = np.where(H >= 300, 255 * x + MIN,
                     np.where(H >= 240, 255 * d + MIN,
                              np.where(H >= 180, 255 * d + MIN,
                                       np.where(H >= 120, 255 * x + MIN, MIN))))
        g[g > 255] = 255
        b[b > 255] = 255
        r[r > 255] = 255
        r[r < 0] = 0
        g[g < 0] = 0
        b[b < 0] = 0
        return BaseImage(np.dstack((r, g, b)).astype('uint8'), ColorModel.rgb)

    """
        metoda dokonujaca konwersji obrazu w atrybucie data do modelu rgb
        metoda zwraca nowy obiekt klasy image zawierajacy obraz w docelowym modelu barw
    """

    def to_rgb(self) -> 'BaseImage':
        if self.color_model == ColorModel.hsv:
            return self.__hsv_to_rgb()
        if self.color_model == ColorModel.hsi:
            return self.__hsi_to_rgb()
        if self.color_model == ColorModel.hsl:
            return self.__hsl_to_rgb()
