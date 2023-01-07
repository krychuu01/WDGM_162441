import numpy as np

class Filter:

    IDENTITY = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    HIGH_PASS = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    LOW_PASS = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])  # use it with prefix = 1/9
    GAUSSIAN_BLUR_3x3 = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])  # use it with prefix = 1/10
    GAUSSIAN_BLUR_5x5 = np.array([[1, 4, 6, 4, 1], [4, 16, 24, 16, 4],
                                  [6, 24, 36, 24, 6], [4, 16, 24, 16, 4], [1, 4, 6, 4, 1]])  # use it with prefix 1/256
    SOBEL_0deg = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    SOBEL_45deg = np.array([[0, 1, 2], [-1, 0, 1], [-2, -1, 0]])
    SOBEL_90deg = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    SOBEL_135deg = np.array([[2, 1, 0], [1, 0, -1], [0, -1, -2]])
