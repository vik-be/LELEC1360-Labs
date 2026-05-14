import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq


def plot_signals(t, signals: dict, title: str, save_path: str = None):
    plt.figure(figsize=(6, 4))
    for label, sig in signals.items():
        plt.plot(t, sig, label=label)
    plt.legend()
    plt.grid()
    plt.title(title)
    plt.xlabel("Temps (s)")
    plt.ylabel("Amplitude")
    if save_path:
        plt.savefig(save_path)
    plt.show()


def plot_spectrum(t, sig, title="Spectre", zoom_factor=8, save_path=None):

    N = len(sig)
    dt = t[1] - t[0]
    freqs = fftfreq(N, dt)
    spectrum = np.abs(fft(sig)) / N

    plt.figure(figsize=(6, 4))
    plt.plot(freqs, spectrum)
    plt.xlim(-max(freqs) / zoom_factor, max(freqs) / zoom_factor)
    plt.xlabel("Fréquence (Hz)")
    plt.ylabel("|X(f)|")
    plt.title(title)
    plt.grid()
    if save_path:
        plt.savefig(save_path)
    plt.show()


def XY_plot(s1, s2, title="XY Plot", save_path=None):

    if len(s1) != len(s2):
        raise ValueError(
            f"XY_plot: s1 and s2 must have the same length "
            f"(got {len(s1)} and {len(s2)})."
        )
    plt.figure()
    plt.plot(s1, s2)
    plt.xlabel("Modulant")
    plt.ylabel("Démodulé / Modulé")
    plt.title(title)
    plt.grid()
    if save_path:
        plt.savefig(save_path)
    plt.show()