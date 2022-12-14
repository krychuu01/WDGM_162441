
from typing import Any
import numpy as np

from BaseImage import BaseImage
from ColorModel import ColorModel


class GrayScaleTransform(BaseImage):
    alpha_beta: tuple
    w: int

    def __init__(self, baseImg : BaseImage) -> None:
        super().__init__(baseImg.data, baseImg.color_model)

    """
        metoda zwracajaca obraz w skali szarosci jako obiekt klasy BaseImage
    """

    def to_gray(self) -> BaseImage:
        if self.color_model != ColorModel.rgb:
            raise Exception("Color model must be RGB!")
        r, g, b = self.get_img_layers()
        r_avg = np.multiply(r, 0.299)
        g_avg = np.multiply(g, 0.587)
        b_avg = np.multiply(b, 0.114)
        gray_scale = np.add(r_avg, g_avg, b_avg)
        # gray_scale = r_avg + g_avg + b_avg # mniejsze roznice na histogramie, tzn. mniej pionowych kresek
        return BaseImage(gray_scale.astype('uint8'), ColorModel.gray)

    """
        metoda zwracajaca obraz w sepii jako obiekt klasy BaseImage
        sepia tworzona metoda 1 w przypadku przekazania argumentu alpha_beta
        lub metoda 2 w przypadku przekazania argumentu w
    """

    def to_sepia(self, alpha_beta: tuple = (None, None), w: int = None) -> BaseImage:
        self.__set_alpha_beta_and_w(alpha_beta, w)
        gray_scale_img = self.to_gray()
        sepia = self.__transform_gray_scale_to_sepia(gray_scale_img, alpha_beta, w)
        return BaseImage(sepia, ColorModel.sepia)

    def __set_alpha_beta_and_w(self, alpha_beta, w):
        self.alpha_beta = alpha_beta
        self.w = w

    def __transform_gray_scale_to_sepia(self, gray_scale_img, alpha_beta, w) -> []:
        if self.__alphabeta_and_w_given():
            raise Exception("You should specify either alpha_beta or w parameter, not two of them in the same time!")
        if self.__alphabeta_given():
            sepia = self.__use_alpha_beta(gray_scale_img, alpha_beta)
        if self.__w_given():
            sepia = self.__use_w(gray_scale_img, w)
        return sepia

    def __w_given(self) -> bool:
        return self.w is not None

    def __alphabeta_given(self) -> bool:
        return self.alpha_beta[0] and self.alpha_beta[1] is not None

    def __alphabeta_and_w_given(self) -> bool:
        return (self.alpha_beta[0] or self.alpha_beta[1] is not None) and self.w is not None

    def __use_alpha_beta(self, gray_scale_img, alpha_beta: tuple) -> []:
        alpha, beta = alpha_beta[0], alpha_beta[1]
        if alpha + beta != 2 or beta > alpha:
            raise Exception("Sum of alpha + beta must be 2.0 and alpha must be greater than beta.")
        L0, L1, L2 = self.__get_gray_scale_img_data(gray_scale_img)
        L0 = np.where(L0 * alpha > 255, 255, L0 * alpha)
        L2 = np.where(L2 * beta > 255, 255, L2 * beta)
        return np.dstack((L0, L1, L2)).astype('i')

    def __use_w(self, gray_scale_img, w: int) -> []:
        if not (20 <= w <= 40):
            raise Exception("'w' must be greater than or equal 20 and less than or equal 40")
        L0, L1, L2 = self.__get_gray_scale_img_data(gray_scale_img)
        L0 = np.where(L0 + 2 * w > 255, 255, L0 + 2 * w)
        L1 = np.where(L1 + w > 255, 255, L1 + w)
        return np.dstack((L0, L1, L2)).astype('i')

    def __get_gray_scale_img_data(self, gray_scale_img) -> []:
        L0, L1, L2 = gray_scale_img.data, gray_scale_img.data, gray_scale_img.data
        return np.array([L0, L1, L2])
