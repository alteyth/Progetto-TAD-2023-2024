import matplotlib.pyplot as plt
import soundfile as sf
import numpy as np

if __name__ == '__main__':
    file = "diapason.wav"
    data, samplerate = sf.read(file)
    if np.ndim(data) > 1:
        data = np.mean(data, axis=1)
    print(data)
    # sf.write("pulita_semplice_mono.wav", data, samplerate)
    Time = np.linspace(0, len(data) / samplerate, num=len(data))
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title(file)
    plt.plot(Time, data)
    plt.show()

