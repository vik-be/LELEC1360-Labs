


def A3_modulation(signal1, signal2, ka):
    return (1+ka*signal1)*signal2

def DSB_SC_modulation(signal1, signal2):
    return signal1*signal2