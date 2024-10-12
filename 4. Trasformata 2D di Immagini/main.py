import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as fft
import scipy.signal as signal
import matplotlib.image as image

if __name__ == '__main__':
    image = image.imread("lena_std.tif")
    image = np.mean(image, axis=2)
    print(f"Numero di Dimensioni: {np.ndim(image)}")
    image_fft = fft.fft2(image)
    print(image_fft.shape)
    image_fft_shifted = fft.fftshift(image_fft)
    image_ps = np.abs(image_fft_shifted)
    plt.imshow(image_ps, norm="log")
    plt.xlabel('Frequenza Righe')
    plt.ylabel('Frequenza Colonne')

    plt.show()
