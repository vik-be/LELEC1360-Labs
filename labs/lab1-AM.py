import sys
from pathlib import Path

# Add parent directory to path so lib module can be found
sys.path.insert(0, str(Path(__file__).parent.parent))

from lib.signals import *
from lib.modulations import A3_modulation, DSB_SC_modulation
from lib.demodulations import detecteur_de_crete, coherent_detector
from lib import plotting as libplot
import matplotlib.pyplot as plt



#Python project for analog modulation and demodulation

f_m = 400e3 #Freq signal modulant
A_m = 1 #Amplitude signal modulant
f_c = 20e6 #Freq signal porteuse
A_c = 1 #Amplitude signal porteuse
f_coupure = 4e6 #Frequence de coupure du filtre du détecteur de crête (par défaut à fc/2)
f_coupure_coherent = 1e6 #Frequence de coupure du filtre du détecteur cohérent (par défaut à fc/10)

t = create_time_axis(f_m, f_c, 100, n_periods=3)
t_fft = create_time_axis(f_m, f_c, 100, n_periods=10)
fs = 1 / (t[1] - t[0])
m = create_cosine_signal(A_m, f_m, t)
m_fft = create_cosine_signal(A_m, f_m, t_fft)
c = create_cosine_signal(A_c, f_c, t)

A3_signal = A3_modulation(m, c, 0.7)
A3_signal_fft = A3_modulation(create_cosine_signal(A_m, f_m, t_fft), create_cosine_signal(A_c, f_c, t_fft), 0.7)
A3_demodulated_crete = detecteur_de_crete(A3_signal_fft, t, f_c, f_coupure)
A3_demodulated_coherent = coherent_detector(A3_signal, t, fs, f_c, f_coupure_coherent)
DSB_SC_signal = DSB_SC_modulation(m, c)
DSB_SC_signal_fft = DSB_SC_modulation(create_cosine_signal(A_m, f_m, t_fft), create_cosine_signal(A_c, f_c, t_fft))
DSB_demodulated_crete = detecteur_de_crete(DSB_SC_signal, t, f_c, f_coupure)
DSB_demodulated_coherent = coherent_detector(DSB_SC_signal,  t, fs, f_c, f_coupure_coherent)


###MODULATION
def plot_A3_modulation(t, m, c, A3_signal):
    libplot.plot_signals(t,
        {"Modulant": m, "Porteuse": c, "Signal A3": A3_signal},
        title="Modulation A3",
        save_path="figures/lab1/lab1_A3.pdf"
    )

def plot_DSB_SC_modulation(t, m, c, DSB_SC_signal):
    libplot.plot_signals(t,
        {"Modulant": m, "Porteuse": c, "Signal DSB-SC": DSB_SC_signal},
        title="Modulation DSB-SC",
        save_path="figures/lab1/lab1_DSB_SC.pdf"
    )

###SPECTRES
def plot_A3_spectrum(t, A3_signal):
    libplot.plot_spectrum(t, A3_signal_fft, title="Spectre du signal A3", save_path="figures/lab1/lab1_A3_spectrum.pdf")

def plot_DSB_SC_spectrum(t, DSB_SC_signal):
    libplot.plot_spectrum(t, DSB_SC_signal_fft, title="Spectre du signal DSB-SC", save_path="figures/lab1/lab1_DSB_SC_spectrum.pdf")

###DEMODULATIONS
def plot_A3_demodulation_crete(t, A3_demodulated_crete):
    libplot.plot_signals(t,
        {"Signal démodulé (détecteur de crête)": A3_demodulated_crete},
        title="Démodulation du signal A3",
        save_path="figures/lab1/lab1_A3_demodulation.pdf"
    )

def plot_A3_demodulation_coherent(t, A3_demodulated_coherent):
    libplot.plot_signals(t,
        {"Signal démodulé (démodulation cohérente)": A3_demodulated_coherent},
        title="Démodulation du signal A3",
        save_path="figures/lab1/lab1_A3_demodulation_coherent.pdf"
    )
    
def plot_XY_A3_modulant_démodulé_crete(m_fft, A3_demodulated_crete):
    libplot.XY_plot(m_fft, A3_demodulated_crete, title="XY Plot du signal modulant vs signal démodulé", save_path="figures/lab1/lab1_XY_modulant_modulé.pdf")

def plot_XY_A3_modulant_démodulé_coherent(m_fft, A3_demodulated_coherent):
    libplot.XY_plot(m_fft, A3_demodulated_coherent, title="XY Plot du signal modulant vs signal démodulé", save_path="figures/lab1/lab1_XY_modulant_modulé_coherent.pdf")

def plot_XY_A3_modulant_modulé(m_fft, A3_signal_fft):
    libplot.XY_plot(m_fft, A3_signal_fft, title="XY Plot du signal modulant vs signal modulé", save_path="figures/lab1/lab1_XY_modulant_modulé.pdf")

def plot_XY_DSB_SC_modulant_modulé(m_fft, DSB_SC_signal_fft):
    libplot.XY_plot(m_fft, DSB_SC_signal_fft, title="XY Plot du signal modulant vs signal modulé", save_path="figures/lab1/lab1_XY_modulant_modulé_DSB_SC.pdf")

def plot_DSB_SC_demodulation_crete(t, DSB_demodulated_crete):
    libplot.plot_signals(t,
        {"Signal démodulé (détecteur de crête)": DSB_demodulated_crete},
        title="Démodulation du signal DSB-SC avec détecteur de crête",
        save_path="figures/lab1/lab1_DSB_SC_demodulation_crete.pdf"
    )

def plot_DSB_SC_demodulation_coherent(t, DSB_demodulated_coherent):
    libplot.plot_signals(t,
        {"Signal démodulé (démodulation cohérente)": DSB_demodulated_coherent},
        title="Démodulation du signal DSB-SC avec démodulation cohérente",
        save_path="figures/lab1/lab1_DSB_SC_demodulation_coherent.pdf"
    )

def plot_XY_DSB_SC_modulant_démodulé(m_fft, DSB_demodulated_crete, DSB_demodulated_coherent):
    libplot.XY_plot(m_fft, DSB_demodulated_crete, title="XY Plot du signal modulant vs signal démodulé (détecteur de crête)", save_path="figures/lab1/lab1_XY_DSB_SC_modulant_démodulé_crete.pdf")
    libplot.XY_plot(m_fft, DSB_demodulated_coherent, title="XY Plot du signal modulant vs signal démodulé (démodulation cohérente)", save_path="figures/lab1/lab1_XY_DSB_SC_modulant_démodulé_coherent.pdf")

def plot_XY_DSB_SC_modulant_modulé(m_fft, DSB_SC_signal_fft):
    libplot.XY_plot(m_fft, DSB_SC_signal_fft, title="XY Plot du signal modulant vs signal modulé", save_path="figures/lab1/lab1_XY_DSB_SC_modulant_modulé.pdf")

def plot_DSB_SC_demodulation_crete(t, DSB_demodulated_crete):
    libplot.plot_signals(t,
        {"Signal démodulé (détecteur de crête)": DSB_demodulated_crete},
        title="Démodulation du signal DSB-SC avec détecteur de crête",
        save_path="figures/lab1/lab1_DSB_SC_demodulation_crete.pdf"
    )

def plot_DSB_SC_demodulation_coherent(t, DSB_demodulated_coherent):
    libplot.plot_signals(t,
        {"Signal démodulé (démodulation cohérente)": DSB_demodulated_coherent},
        title="Démodulation du signal DSB-SC avec démodulation cohérente",
        save_path="figures/lab1/lab1_DSB_SC_demodulation_coherent.pdf"
    )

if __name__ == "__main__":
    plot_A3_modulation(t, m, c, A3_signal)
    plot_DSB_SC_modulation(t, m, c, DSB_SC_signal)
    plot_A3_spectrum(t, A3_signal)
    plot_DSB_SC_spectrum(t, DSB_SC_signal)
    plot_A3_demodulation_crete(t_fft, A3_demodulated_crete)
    plot_A3_demodulation_coherent(t, A3_demodulated_coherent)
    plot_XY_A3_modulant_démodulé_crete(m_fft, A3_demodulated_crete)
    plot_XY_A3_modulant_démodulé_coherent(m, A3_demodulated_coherent)
    plot_XY_A3_modulant_modulé(m_fft, A3_signal_fft)
    plot_XY_DSB_SC_modulant_modulé(m_fft, DSB_SC_signal_fft)
    plot_A3_demodulation_coherent(t, A3_demodulated_coherent)
    plot_DSB_SC_demodulation_crete(t, DSB_demodulated_crete)
    plot_DSB_SC_demodulation_coherent(t, DSB_demodulated_coherent)
    plot_XY_DSB_SC_modulant_démodulé(m, DSB_demodulated_crete, DSB_demodulated_coherent)
    plot_XY_DSB_SC_modulant_modulé(m_fft, DSB_SC_signal_fft)
    plot_DSB_SC_demodulation_crete(t, DSB_demodulated_crete)
    plot_DSB_SC_demodulation_coherent(t, DSB_demodulated_coherent)
