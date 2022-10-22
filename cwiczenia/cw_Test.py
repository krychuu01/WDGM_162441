from WDGM_162441.cwiczenia.cw_2 import ColorModel
from WDGM_162441.cwiczenia.cw_2.BaseImage import BaseImage

img1 = BaseImage('lena.jpg', color_model=ColorModel.ColorModel.rgb)
img2 = BaseImage('lena.jpg', color_model=ColorModel.ColorModel.rgb)
img3 = BaseImage('lena.jpg', color_model=ColorModel.ColorModel.rgb)

hsv = img1.to_hsv()
hsv.to_rgb()
# hsv.show_img_without_axis()
# hsv.show_as_rgb_layers()

hsi = img2.to_hsi()
hsi.to_rgb()
# hsi.show_img_without_axis()
# hsv.show_as_rgb_layers()

hsl = img3.to_hsl()
hsl.to_rgb()
# hsl.show_img_without_axis()
# hsl.show_as_rgb_layers()

BaseImage.show_all_plots(img1, hsv, hsi, hsl)
