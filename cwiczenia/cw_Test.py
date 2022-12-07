
from BaseImage import BaseImage
from GrayScaleTransform import GrayScaleTransform
from ColorModel import ColorModel
from Histogram import Histogram
from ImageComparison import ImageComparison
from ImageDiffMethod import ImageDiffMethod
from ImageAligning import ImageAligning


base_img = BaseImage('lena.jpg', color_model=ColorModel.rgb)

img_rgb = base_img
# img_rgb = GrayScaleTransform(img_rgb).to_gray()
# img_rgb.show_img_without_axis()
# img_rgb_hist = Histogram(img_rgb.data)
# img_rgb_hist.plot()

img_rgb_aligned = ImageAligning(img_rgb).align_image(tail_elimination=False)
# img_rgb_aligned.show_img_without_axis()

# comp = ImageComparison(img_rgb)
# val = comp.compare_to(img_rgb_aligned, method=ImageDiffMethod.rmse)
# print(val)

img_rgb_align_gray = GrayScaleTransform(img_rgb_aligned).to_gray()
img_rgb_align = Histogram(img_rgb_align_gray.data)

img_rgb_align.to_cumulated()
img_rgb_align.plot()
