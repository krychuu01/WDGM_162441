
from WDGM_162441.cwiczenia.cw_2 import ColorModel
from WDGM_162441.cwiczenia.cw_2.BaseImage import BaseImage
import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb

img1 = BaseImage('lena.jpg', color_model=ColorModel.ColorModel.rgb)
# img2 = BaseImage('lena.jpg', color_model=ColorModel.ColorModel.rgb)
# img3 = BaseImage('lena.jpg', color_model=ColorModel.ColorModel.rgb)

hsv = img1.to_hsv()
# hsv.show_as_rgb_layers()
# hsv.show_img_without_axis()
# hsv.show_as_rgb_layers()
hsv.to_rgb()
# img2.to_hsi()
# img3.to_hsl()

hsv.show_img_without_axis()
hsv.show_as_rgb_layers()
# img1.show_as_rgb_layers()
# hsv.show_img()
# hsv.show_img_without_axis()
# img1.show_img_without_axis()
# img2.show_img_without_axis()
# img3.show_img_without_axis()
