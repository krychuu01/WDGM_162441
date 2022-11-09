
from WDGM_162441.cwiczenia.cw_2.BaseImage import BaseImage
from WDGM_162441.cwiczenia.cw_3.GrayScaleTransform import GrayScaleTransform
from WDGM_162441.cwiczenia.cw_2.ColorModel import ColorModel
from WDGM_162441.cwiczenia.cw_4.Histogram import Histogram

img_rgb = BaseImage('lena.jpg', color_model=ColorModel.rgb)
img_gray_scale = GrayScaleTransform('lena.jpg', color_model=ColorModel.rgb)
img_gray_scale = img_gray_scale.to_gray()

img_rgb_hist = Histogram(img_rgb.data)
img_gray_scale_hist = Histogram(img_gray_scale.data)

img_rgb_hist.plot()
img_gray_scale_hist.plot()
