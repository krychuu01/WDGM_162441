import numpy as np

from BaseImage import BaseImage
from Image import Image
from GrayScaleTransform import GrayScaleTransform
from ColorModel import ColorModel
from Histogram import Histogram
from ImageComparison import ImageComparison
from ImageDiffMethod import ImageDiffMethod
from ImageAligning import ImageAligning
from Thresholding import Thresholding
from ImageFiltration import ImageFiltration
from Filter import Filter

base_img = BaseImage('lena.jpg', color_model=ColorModel.rgb)
hsv = base_img.to_hsl().to_rgb()
hsv.show_img_without_axis()
# base_img = GrayScaleTransform(base_img).to_gray()
# thr = Thresholding(base_img)
# thr = thr.threshold(117)
# thr.show_img_without_axis()
# filtered = ImageFiltration().conv_2d(base_img, Filter.GAUSSIAN_BLUR_3x3, 1/16)
# filtered.show_img_without_axis()



# SUDOKU

# base_img = BaseImage('sudoku.jpg', color_model=ColorModel.rgb)

# test = BaseImage((base_img.data * 255).astype('uint8'), color_model=ColorModel.rgb)
# test.show_img_without_axis()
# base_img.show_img_without_axis()

# sob0 = ImageFiltration().conv_2d(test, Filter.SOBEL_0deg)
# sob45 = ImageFiltration().conv_2d(test, Filter.SOBEL_45deg)
# sob90 = ImageFiltration().conv_2d(test, Filter.SOBEL_90deg)
# sob135 = ImageFiltration().conv_2d(test, Filter.SOBEL_135deg)
# edges = (sob0.data + sob45.data + sob90.data + sob135.data).astype('uint8')
#
# img = BaseImage(edges, ColorModel.rgb)
# img.show_img_without_axis()

# KONIEC SUDOKU

# base_img.show_img_without_axis()
# img_rgb = base_img
# img_rgb = GrayScaleTransform(img_rgb).to_gray()
# img_rgb.show_img_without_axis()
# img_rgb_hist = Histogram(img_rgb.data)
# img_rgb_hist.plot()

# img_rgb_aligned = ImageAligning(img_rgb).align_image(tail_elimination=True)
# img_rgb_aligned.show_img_without_axis()

# comp = ImageComparison(img_rgb)
# val = comp.compare_to(img_rgb_aligned, method=ImageDiffMethod.rmse)
# print(val)

# img_rgb_align_gray = GrayScaleTransform(img_rgb_aligned).to_gray()
# img_rgb_align = Histogram(img_rgb_align_gray.data)
#
# img_rgb_align.to_cumulated()
# img_rgb_align.plot()
