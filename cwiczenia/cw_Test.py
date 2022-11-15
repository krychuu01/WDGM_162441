import sys

from BaseImage import BaseImage
from GrayScaleTransform import GrayScaleTransform
from ColorModel import ColorModel
from Histogram import Histogram
from ImageComparison import ImageComparison
from ImageDiffMethod import ImageDiffMethod

# sys.path.append("C:\\Users\\local\\Videos\\WDGM_162441\\cwiczenia\\cw_2")
# sys.path.append("C:\\Users\\local\\Videos\\WDGM_162441\\cwiczenia\\cw_3")
# sys.path.append("C:\\Users\\local\\Videos\\WDGM_162441\\cwiczenia\\cw_4")

img_rgb = BaseImage('lena.jpg', color_model=ColorModel.rgb)
img2 = img_rgb
img3 = img_rgb
img4 = img_rgb
# img_rgb = img_rgb.to_hsv().to_rgb()
img2 = img2.to_hsv()
img3 = img3.to_hsi()
img4 = img4.to_hsl()
# img2.show_img_without_axis()
# img2.show_img_without_axis()

# var = ImageComparison(img_rgb.data, img_rgb.color_model)
# val = var.compare_to(img2, ImageDiffMethod.rmse)

# print(val)
