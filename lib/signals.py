import numpy as np
from scipy import signal


def create_time_axis(f_m, f_c, points_per_period=100):
    N = int(points_per_period * f_c / f_m)
    return np.linspace(0, 1/f_m, N)

def create_cosine_signal(A, f, t):
    return A*np.cos(2*np.pi*f*t)

