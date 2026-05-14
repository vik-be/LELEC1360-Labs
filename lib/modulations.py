import numpy as np


def A3_modulation(message, carrier, ka):
    return (1+ka*message)*carrier

def DSB_SC_modulation(message, carrier):
    return message*carrier

def FM_modulation(message, Ac, fc, kf, t):
    dt = t[1] - t[0]  # time step
    return Ac * np.cos(2*np.pi*fc*t + 2*np.pi*kf * np.cumsum(message) * dt)