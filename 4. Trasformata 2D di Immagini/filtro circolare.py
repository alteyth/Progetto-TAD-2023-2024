import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as fft
import scipy.signal as signal
import matplotlib.image as image

if __name__ == '__main__':
    image = image.imread("lena_std.tif")
    image = np.mean(image, axis=2)
    image_fft = fft.fft2(image)
    image_fft_shifted = fft.fftshift(image_fft)
    image_ps = np.abs(image_fft_shifted)

    mask = np.zeros(image_ps.shape)
    center_x = image_ps.shape[0] / 2
    center_y = image_ps.shape[1] / 2
    print(center_x, center_y)
    distance = 100

    for i in range(image_ps.shape[0]):
        for j in range(image_ps.shape[1]):
            if (center_x-i)**2 + (center_y-j)**2 <= distance**2:
                mask[i, j] = 1

    masked_ps = image_ps * mask

    plt.imshow(masked_ps, norm="log")
    plt.xlabel('Frequenza Righe')
    plt.ylabel('Frequenza Colonne')
    plt.show()
