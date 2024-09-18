import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

# Construction of the Time Signal
Fs = 10000
durata = 0.03
f0 = 100
f1 = 200
f2 = 300
t = np.linspace(0, durata, int(Fs * durata))  # Time steps

sin0 = 1 * np.sin(2*np.pi * f0 * t)
sin1 = 1 * np.sin(2*np.pi * f1 * t)
sin2 = 1 * np.sin(2*np.pi * f2 * t)

st0 = np.abs(sp.signal.sawtooth(2 * np.pi * f0 * t))
st1 = np.abs(sp.signal.sawtooth(2 * np.pi * f1 * t))
st2 = np.abs(sp.signal.sawtooth(2 * np.pi * f2 * t))

sq0 = sp.signal.square(2*np.pi * f0 * t)
sq1 = sp.signal.square(2*np.pi * f1 * t)
sq2 = sp.signal.square(2*np.pi * f2 * t)

# Compute FFT
sin0_fft = np.fft.rfft(sin0, norm="forward")
freq = np.fft.rfftfreq(int(Fs * durata), 1/Fs)

# Plot
plt.plot(freq, sin0_fft.real)

plt.show()
