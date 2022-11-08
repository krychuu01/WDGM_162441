
from WDGM_162441.cwiczenia.cw_2.BaseImage import BaseImage
from WDGM_162441.cwiczenia.cw_3.GrayScaleTransform import GrayScaleTransform
from WDGM_162441.cwiczenia.cw_2.ColorModel import ColorModel

# img1 = GrayScaleTransform('lena.jpg', color_model=ColorModel.rgb)
img1 = BaseImage('lena.jpg', color_model=ColorModel.rgb)
# ss = img1.to_sepia(w=40)
# ss.show_img_without_axis()
# ss2 = img1.to_sepia(alpha_beta=(1.95, 0.05))
# ss2.show_img_without_axis()

# img1.show_as_rgb_layers()
hsv = img1.to_hsv()
print(hsv.data.shape)
# hsv = hsv.to_rgb()
hsv.show_img_without_axis()
# hsv.show_as_rgb_layers()

# hsi = img1.to_hsi()
# hsi = hsi.to_rgb()
# hsi.show_img_without_axis()
# hsi.show_as_rgb_layers()

# hsl = img1.to_hsl()
# hsl = hsl.to_rgb()
# hsl.show_img_without_axis()
# hsl.show_as_rgb_layers()

# BaseImage.show_all_plots(img1, hsv, hsi, hsl)
