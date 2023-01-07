from BaseImage import BaseImage
import numpy as np


class Thresholding(BaseImage):

    def __init__(self, baseImage: BaseImage):
        super().__init__(baseImage.data, baseImage.color_model)

    def threshold(self, value: int) -> BaseImage:
        value = np.where(self.data >= value, 255, 0)
        return BaseImage(value, self.color_model)
