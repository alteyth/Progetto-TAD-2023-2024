import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as fft
import scipy.signal as signal
import matplotlib.image as image

if __name__ == '__main__':
    image = image.imread("4. Trasformata 2D di Immagini/immagini/saltandpepper_lena.jpg")
    #image = np.mean(image, axis=2)

    image_fft = fft.fft2(image)
    image_fft_shifted = fft.fftshift(image_fft)
    image_ps = np.abs(image_fft)
    image_ps_shifted = np.abs(image_fft_shifted)
    
    plt.imshow(image_ps_shifted, norm="log")
    plt.xlabel('Frequenza Righe')
    plt.ylabel('Frequenza Colonne')

    plt.show()
