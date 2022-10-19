from WDGM_162441.cwiczenia.cw_2 import ColorModel
from WDGM_162441.cwiczenia.cw_2.BaseImage import BaseImage

img1 = BaseImage('lena.jpg', color_model=ColorModel.ColorModel.rgb)
img2 = BaseImage('lena.jpg', color_model=ColorModel.ColorModel.rgb)
img3 = BaseImage('lena.jpg', color_model=ColorModel.ColorModel.rgb)

img1.to_hsv()
# img2.to_hsi()
# img3.to_hsl()

img1.show_img_without_axis()
# img2.show_img_without_axis()
# img3.show_img_without_axis()
