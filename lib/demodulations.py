import numpy as np
from scipy import signal
 
 
def detecteur_de_crete(input_signal, fs, fc, lp_cutoff=None):
    if lp_cutoff is None:
        lp_cutoff = fc / 2
    abs_signal = np.abs(input_signal)
    sos = signal.butter(2, lp_cutoff, btype='low', analog=False, fs=fs, output='sos')
    return signal.sosfilt(sos, abs_signal)
 
 
def coherent_detector(s, fs, fc, lp_cutoff=None):
    if lp_cutoff is None:
        lp_cutoff = fc / 10
 
    t = np.arange(len(s)) / fs
    local_carrier = np.cos(2 * np.pi * fc * t)
    mixed = s * local_carrier
 
    sos = signal.butter(2, lp_cutoff, btype='low', analog=False, fs=fs, output='sos')
    return signal.sosfilt(sos, mixed)
 