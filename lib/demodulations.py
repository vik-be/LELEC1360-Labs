import numpy as np
from scipy import signal

def detecteur_de_crete(input_signal, t, fc, lp_cutoff=None):
    # Calculate sampling frequency from time array
    fs = len(t) / (t[-1] - t[0]) if len(t) > 1 else 1
    
    if lp_cutoff is None:
        lp_cutoff = fc / 2
    abs_signal = np.abs(input_signal)

    sos = signal.butter(2, lp_cutoff, btype='low', analog=False, fs=fs, output='sos') # RC low-pass filter for example
    return signal.sosfilt(sos, abs_signal)
    
def coherent_detector(s, t, fs, fc, lp_cutoff=None):
    if lp_cutoff is None:
        lp_cutoff = fc / 10  
    melangeur = np.cos(2 * np.pi * fc * t)
    sp = s * melangeur
    sos = signal.butter(2, lp_cutoff, btype='low', analog=False, fs=fs, output='sos')
    return signal.sosfilt(sos, sp)