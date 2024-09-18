import numpy as np
import matplotlib.pyplot as plt

# Genera una lista di n numeri dispari
def odd_k(n):
    k = []
    for i in range(0, n):
        k.append(i * 2 + 1)
    return k

# Calcola la sommatoria seguendo la formula sul PDF
def sommatoria(m, f, l):
    result = []
    x = 0
    k_numbers = odd_k(m)
    for i in k_numbers:
        x += (1 / i) * ((-1)**((i - 1) / 2)) * np.cos(2 * np.pi * i * f * l)
    return x

# Generazione del grafico
if __name__ == '__main__':
    t = np.linspace(0, 1, 1000)
    f0 = 2
    for y in [5, 50, 5000]:
        dft = (1 / 2) + (2 / np.pi) * sommatoria(y, f0, t)
        plt.plot(t, dft, label=f'{y} coefficienti')
    
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.legend()
    plt.show()
