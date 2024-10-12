import matplotlib.pyplot as plt
import soundfile as sf
import numpy as np
import scipy.signal as signal

if __name__ == '__main__':
    file = "3. Garage Band/diapason.wav"
    data, samplerate = sf.read(file)
    if np.ndim(data) > 1:
        data = np.mean(data, axis=1)
    # sf.write("3. Garage Band/pulita_semplice_mono.wav", data, samplerate)
    Time = np.linspace(0, len(data) / samplerate, num=len(data))
    data_fft = np.fft.rfft(data, norm="forward")
    data_imag = data_fft.imag
    data_real = data_fft.real
    freq = np.fft.rfftfreq(len(data), 1/samplerate)
    data_ps = np.abs(data_fft)**2

    """""
    fig, ax = plt.subplots(nrows=5, ncols=1)
    ax[0].plot(data_real)
    ax[1].plot(data_imag)
    ax[2].plot(freq, data_real)
    ax[3].plot(freq, data_imag)
    ax[4].plot(freq, data_ps)
    plt.show()
    """""

    bandwidth = 10
    peaks_index, properties = signal.find_peaks(data_ps, height=5e-6, distance=10)
    max_index = peaks_index[np.argmax(data_ps[peaks_index])]
    secondary_peaks = np.array([x for x in peaks_index if x != max_index])
    main_peak_freq = freq[max_index]
    secondary_peak_freqs = freq[secondary_peaks]
    freq_band = [freq[max_index] - bandwidth, freq[max_index] + bandwidth]
    print(freq[0], freq[1])
    bandwidth = 15 * freq[1]
    print(bandwidth)

    mask = np.zeros(freq.shape)
    for i in range(len(mask)):
        if max_index+15 >= i >= max_index-15:
            mask[i] = 1
        else:
            mask[i] = 0

    # print(mask * data_ps)

    print(secondary_peaks)
    print(peaks_index)
    print(max_index)
    print(freq[peaks_index])
    # print(properties["peak_heights"])
    peaks_width = signal.peak_widths(data_ps, peaks_index, rel_height=0.99)
    print(peaks_width[0])

    plt.plot(freq[:1000], mask[:1000])
    plt.show()
