import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

# Construction of the Time Signal
f0 = 100
f1 = 200
f2 = 300
t = np.linspace(0, 0.03, 1000)  # Time steps

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

# Plot
fig, ax = plt.subplots(nrows=3, ncols=3)

ax[0, 0].plot(t, sin0)
ax[0, 1].plot(t, sin1)
ax[0, 2].plot(t, sin2)

ax[1, 0].plot(t, st0)
ax[1, 1].plot(t, st1)
ax[1, 2].plot(t, st2)

ax[2, 0].plot(t, sq0)
ax[2, 1].plot(t, sq1)
ax[2, 2].plot(t, sq2)

ax[2, 0].set_xlabel("Time (s)")
ax[2, 1].set_xlabel("Time (s)")
ax[2, 2].set_xlabel("Time (s)")

ax[0, 0].set_ylabel("sin")
ax[1, 0].set_ylabel("sin")
ax[2, 0].set_ylabel("sin")

plt.show()
