
from BaseImage import BaseImage
from GrayScaleTransform import GrayScaleTransform
from ColorModel import ColorModel
from Histogram import Histogram
from ImageComparison import ImageComparison
from ImageDiffMethod import ImageDiffMethod


# img_rgb = BaseImage('lena.jpg', color_model=ColorModel.rgb)
#
# img_hsv = img_rgb.to_hsv()
#
# img_hsv_konwersja_do_rgb_dlugi_wzor = img_hsv.hsv_to_rgb()
# img_hsv_konwersja_do_rgb_skrocony_wzor = img_hsv.hsv_to_rgb_skrocony_wzor()
#
# porownanie = ImageComparison(img_hsv_konwersja_do_rgb_dlugi_wzor.data, img_hsv_konwersja_do_rgb_dlugi_wzor.color_model)
# wartosc_porownania = porownanie.compare_to(img_hsv_konwersja_do_rgb_skrocony_wzor, ImageDiffMethod.mse)
#
# print(f'wartosc po porownaniu obrazka z dlugiego wzoru z obrazkiem ze skroconego wzoru: {wartosc_porownania}')
#
# img_hsv_konwersja_do_rgb_dlugi_wzor.show_img_without_axis()

img_rgb = BaseImage('lena.jpg', color_model=ColorModel.rgb)

img_hsv = img_rgb.to_hsv()
img_hsv = img_hsv.to_rgb()

img_rgb = ImageComparison(img_rgb.data, img_rgb.color_model)

val = img_rgb.compare_to(img_hsv, ImageDiffMethod.mse)

print(val)

