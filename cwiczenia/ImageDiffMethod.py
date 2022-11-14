from enum import Enum


class ImageDiffMethod(Enum):
    mse = 0
    rmse = 1

    def is_mse(self) -> bool:
        return self.value == ImageDiffMethod.mse

    def is_rmse(self) -> bool:
        return self.value == ImageDiffMethod.rmse
