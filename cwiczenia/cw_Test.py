
from BaseImage import BaseImage
from GrayScaleTransform import GrayScaleTransform
from ColorModel import ColorModel
from Histogram import Histogram

img_rgb = BaseImage('lena.jpg', color_model=ColorModel.rgb)
img_gray_scale = GrayScaleTransform('lena.jpg', color_model=ColorModel.rgb)
img_gray_scale = img_gray_scale.to_gray()

img_rgb_hist = Histogram(img_rgb.data)
img_gray_scale_hist = Histogram(img_gray_scale.data)

img_rgb_hist.plot()
img_gray_scale_hist.plot()

hsv = img_rgb.to_hsv()
hsv.show_img_without_axis()
rgb = hsv.to_rgb()
rgb.show_img_without_axis()