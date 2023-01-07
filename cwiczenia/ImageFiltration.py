from BaseImage import BaseImage
from typing import Optional
import numpy as np


class ImageFiltration:

    def __conv_layer(self, layer_to_converse: np.ndarray, kernel: np.ndarray) -> np.ndarray:
        rows, columns = layer_to_converse.shape
        reshaped_layer = np.reshape(layer_to_converse, (1, layer_to_converse.size))
        reshaped_kernel = np.reshape(kernel, (1, kernel.size))
        conv_layer = np.convolve(reshaped_layer[0], reshaped_kernel[0], 'same')
        conv_layer = np.reshape(conv_layer, (rows, columns))
        return conv_layer

    def conv_2d(self, image: BaseImage, kernel: np.ndarray, prefix: Optional[float] = 1) -> BaseImage:
        if image.data.ndim == 2:
            conv_layer = self.__conv_layer(image.data, kernel) * prefix
            conv_layer[conv_layer > 255] = 255
            conv_layer[conv_layer < 0] = 0
            return BaseImage(conv_layer, image.color_model)
        else:
            r, g, b = image.get_img_layers()
            conv_r = self.__conv_layer(r, kernel) * prefix
            conv_g = self.__conv_layer(g, kernel) * prefix
            conv_b = self.__conv_layer(b, kernel) * prefix
            converted_layers = np.dstack((conv_r, conv_g, conv_b))
            converted_layers[converted_layers > 255] = 255
            converted_layers[converted_layers < 0] = 0
            return BaseImage(converted_layers.astype('i'), image.color_model)
