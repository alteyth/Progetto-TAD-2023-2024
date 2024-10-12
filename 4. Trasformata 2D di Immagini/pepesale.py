import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as fft
import scipy.signal as signal
import matplotlib.image as image

if __name__ == '__main__':
    image = image.imread("saltandpepper_lena.jpg")
    print(np.ndim(image))