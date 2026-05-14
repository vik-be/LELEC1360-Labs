import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.fft import fft, fftfreq
import numpy as np





def plot_signals(t, signals: dict, title: str, save_path: str = None):
    """signals = {"Signal modulant": m, "Porteuse": c, ...}"""
    plt.figure(figsize=(6, 4))
    for label, sig in signals.items():
        plt.plot(t, sig, label=label)
    plt.legend(); plt.grid(); plt.title(title)
    plt.xlabel("Temps (s)"); plt.ylabel("Amplitude")
    if save_path:
        plt.savefig(save_path)
    plt.show()

def plot_spectrum(t, signal, title="Spectre", save_path=None):



    N = len(signal)
    dt = t[1] - t[0]
    freqs = fftfreq(N, dt)
    spectrum = np.abs(fft(signal)) / N

    plt.figure(figsize=(6, 4))
    plt.plot(freqs, spectrum)
    plt.xlim(-max(freqs)/8, max(freqs)/8) 
    plt.xlabel("Fréquence (Hz)")
    plt.ylabel("|X(f)|")
    plt.title(title)
    plt.grid()
    if save_path:
        plt.savefig(save_path)
    plt.show()


def XY_plot(s1, s2, title="XY Plot", save_path=None):
    plt.figure()
    plt.plot(s1, s2)
    plt.xlabel("Modulant")
    plt.ylabel("Démodulé")
    plt.title(title)
    plt.grid()
    if save_path:
        plt.savefig(save_path)
    plt.show()