import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

# Costruzione del Segnale
Fs = 10000
durata = 0.03
f0 = 100
f1 = 200
f2 = 440
t = np.linspace(0, durata, int(Fs * durata))  # Tempo

sin0 = 1 * np.sin(2*np.pi * f0 * t)
sin1 = 1 * np.sin(2*np.pi * f1 * t)
sin2 = 1 * np.sin(2*np.pi * f2 * t)

st0 = np.abs(sp.signal.sawtooth(2 * np.pi * f0 * t))
st1 = np.abs(sp.signal.sawtooth(2 * np.pi * f1 * t))
st2 = np.abs(sp.signal.sawtooth(2 * np.pi * f2 * t))

sq0 = sp.signal.square(2*np.pi * f0 * t)
sq1 = sp.signal.square(2*np.pi * f1 * t)
sq2 = sp.signal.square(2*np.pi * f2 * t)

# Calcolo FFT
freq = np.fft.rfftfreq(int(Fs * durata), 1/Fs)

sin0_fft = np.fft.rfft(sin0, norm="forward")
sin0_p = (np.abs(sin0_fft))**2
sin1_fft = np.fft.rfft(sin1, norm="forward")
sin1_p = (np.abs(sin1_fft))**2
sin2_fft = np.fft.rfft(sin2, norm="forward")
sin2_p = (np.abs(sin2_fft))**2

sin_composite = sin0 + sin1 + sin2
sin_composite_fft = np.fft.rfft(sin_composite, norm="forward")
sin_composite_p = (np.abs(sin_composite_fft))**2

st0_fft = np.fft.rfft(st0, norm="forward")
st0_p = (np.abs(st0_fft))**2
st1_fft = np.fft.rfft(st1, norm="forward")
st1_p = (np.abs(st1_fft))**2
st2_fft = np.fft.rfft(st2, norm="forward")
st2_p = (np.abs(st2_fft))**2

sq0_fft = np.fft.rfft(sq0, norm="forward")
sq0_p = (np.abs(sq0_fft))**2
sq1_fft = np.fft.rfft(sq1, norm="forward")
sq1_p = (np.abs(sq1_fft))**2
sq2_fft = np.fft.rfft(sq2, norm="forward")
sq2_p = (np.abs(sq2_fft))**2

# Plot
# fig, ax = plt.subplots(nrows=3, ncols=3)

fig, ax = plt.subplots(nrows=1, ncols=3)

# Composite Sin
ax[0].plot(freq, sin_composite_fft.real)
ax[1].plot(freq, sin_composite_fft.imag)
ax[2].plot(freq, sin_composite_p)
ax[0].set_title('Parte Reale')
ax[1].set_title('Parte Immaginaria')
ax[2].set_title('Spettro di Potenza')
ax[1].set_xlabel("Freq")
ax[0].set_ylabel("Amplitude")



# Sin
# ax[0, 0].plot(freq, sin0_fft.real)
# ax[0, 1].plot(freq, sin1_fft.real)
# ax[0, 2].plot(freq, sin2_fft.real)
# ax[1, 0].plot(freq, sin0_fft.imag)
# ax[1, 1].plot(freq, sin1_fft.imag)
# ax[1, 2].plot(freq, sin2_fft.imag)
# ax[2, 0].plot(freq, sin0_p)
# ax[2, 1].plot(freq, sin1_p)
# ax[2, 2].plot(freq, sin2_p)

# Sawtooth
# ax[0, 0].plot(freq, st0_fft.real)
# ax[0, 1].plot(freq, st1_fft.real)
# ax[0, 2].plot(freq, st2_fft.real)
# ax[1, 0].plot(freq, st0_fft.imag)
# ax[1, 1].plot(freq, st1_fft.imag)
# ax[1, 2].plot(freq, st2_fft.imag)
# ax[2, 0].plot(freq, st0_p)
# ax[2, 1].plot(freq, st1_p)
# ax[2, 2].plot(freq, st2_p)

# Square
# ax[0, 0].plot(freq, sq0_fft.real)
# ax[0, 1].plot(freq, sq1_fft.real)
# ax[0, 2].plot(freq, sq2_fft.real)
# ax[1, 0].plot(freq, sq0_fft.imag)
# ax[1, 1].plot(freq, sq1_fft.imag)
# ax[1, 2].plot(freq, sq2_fft.imag)
# ax[2, 0].plot(freq, sq0_p)
# ax[2, 1].plot(freq, sq1_p)
# ax[2, 2].plot(freq, sq2_p)

fig.suptitle("Parte Reale, Immaginaria e Spettro di Potenza della FFT della somma dei Sin")

# ax[0, 0].set_title('100hz')
# ax[0, 1].set_title('200hz')
# ax[0, 2].set_title('440hz')

# ax[2, 0].set_xlabel("Freq")
# ax[2, 1].set_xlabel("Freq")
# ax[2, 2].set_xlabel("Freq")

# ax[0, 0].set_ylabel("Amplitude")
# ax[1, 0].set_ylabel("Amplitude")
# ax[2, 0].set_ylabel("Amplitude")

plt.show()
