from lib.signals import *
from lib.modulations import A3_modulation
from lib import plotting as libplot
import matplotlib.pyplot as plt



#Python project for analog modulation and demodulation

f_m = 20e3 #Freq signal modulant
A_m = 1 #Amplitude signal modulant
f_c = 1000e6 #Freq signal porteuse
A_c = 1 #Amplitude signal porteuse
T = 1/f_m #Periode signal modulant

t = create_time_axis(f_m, f_c, 100)
m = create_cosine_signal(A_m, f_m, t)
c = create_cosine_signal(A_c, f_c, t)

A3_signal = A3_modulation(m, c, 0.7)

def plot_A3_modulation(t, m, c, A3_signal):
    plt.figure(figsize=(6,4))
    plt.plot(t, m, label="Signal modulant")
    plt.plot(t, c, label="Signal porteuse")
    plt.plot(t, A3_signal, label="Signal modulé en amplitude")
    plt.legend()
    plt.xlabel("Temps (s)")
    plt.ylabel("Amplitude")
    plt.title("Modulation A3")
    plt.grid()
    plt.savefig("figures/A3_modulation.pdf")
    plt.show()



if __name__ == "__main__":
    libplot.plot_signals(t,
        {"Modulant": m, "Porteuse": c, "Signal A3": A3_signal},
        title="Modulation A3",
        save_path="figures/lab1_A3.pdf"
    )

