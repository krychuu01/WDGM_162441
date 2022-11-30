
from BaseImage import BaseImage
from GrayScaleTransform import GrayScaleTransform
from ColorModel import ColorModel
from Histogram import Histogram
from ImageComparison import ImageComparison
from ImageDiffMethod import ImageDiffMethod
from ImageAligning import ImageAligning


img_rgb = BaseImage('lena.jpg', color_model=ColorModel.rgb)

img_align = ImageAligning(img_rgb)

img_rgb = GrayScaleTransform(img_rgb).to_gray()
img_rgb_align = img_align.align_image()


img_rgb = Histogram(img_rgb.data)
img_rgb.plot()

img_rgb_align = Histogram(img_rgb_align.data)
img_rgb_align.plot()

