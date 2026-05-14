import sys
import os
from pathlib import Path
 
import matplotlib.pyplot as plt
 
# Allow running the script directly (python lab1-AM.py) or as part of a package
sys.path.insert(0, str(Path(__file__).parent.parent))
 
from lib.signals import create_time_axis, create_cosine_signal
from lib.modulations import A3_modulation, DSB_SC_modulation
from lib.demodulations import detecteur_de_crete, coherent_detector
import lib.plotting as libplot
 
# ---------------------------------------------------------------------------
# Parameters
# ---------------------------------------------------------------------------
f_m = 400e3      # Fréquence modulant
A_m = 1.0        # Amplitude du signal modulant
f_c = 20e6       # Fréquence porteuse
A_c = 1.0        # Amplitude de la porteuse (V)
ka  = 0.7        # Index de modulation A3
 
# Low-pass filter cutoff frequencies
f_lp_crete    = 4e6   # Pour le détecteur de crête
f_lp_coherent = 1e6   # Pour détecteur cohérent
 

t     = create_time_axis(f_m, f_c, oversampling_factor=100, n_periods=3)
t_fft = create_time_axis(f_m, f_c, oversampling_factor=100, n_periods=10) ##Mieux pour spectre (plus de points => meilleure résolution en fréquence)
 
fs     = 1.0 / (t[1]     - t[0])
fs_fft = 1.0 / (t_fft[1] - t_fft[0])  # same value, kept explicit for clarity
 
# ---------------------------------------------------------------------------
# Signals
# ---------------------------------------------------------------------------
m     = create_cosine_signal(A_m, f_m, t)
m_fft = create_cosine_signal(A_m, f_m, t_fft)
c     = create_cosine_signal(A_c, f_c, t)
c_fft = create_cosine_signal(A_c, f_c, t_fft)
 
# --- A3 modulation ---
A3_signal     = A3_modulation(m,     c,     ka)
A3_signal_fft = A3_modulation(m_fft, c_fft, ka)
 
# --- A3 demodulation ---
A3_demod_crete    = detecteur_de_crete(A3_signal_fft, fs_fft, f_c, f_lp_crete)
A3_demod_coherent = coherent_detector(A3_signal,      fs,     f_c, f_lp_coherent)
 
# --- DSB-SC modulation ---
DSB_signal     = DSB_SC_modulation(m,     c)
DSB_signal_fft = DSB_SC_modulation(m_fft, c_fft)
 
# --- DSB-SC demodulation ---
DSB_demod_crete    = detecteur_de_crete(DSB_signal,     fs,     f_c, f_lp_crete)
DSB_demod_coherent = coherent_detector(DSB_signal,      fs,     f_c, f_lp_coherent)
 
# ---------------------------------------------------------------------------
# Plotting functions — A3
# ---------------------------------------------------------------------------
 
def plot_A3_modulation():
    libplot.plot_signals(
        t,
        {"Modulant": m, "Porteuse": c, "Signal A3": A3_signal},
        title="Modulation A3",
        save_path="figures/lab1/lab1_A3.pdf",
    )
 
 
def plot_A3_spectrum():
    libplot.plot_spectrum(
        t_fft, A3_signal_fft,
        title="Spectre du signal A3",
        save_path="figures/lab1/lab1_A3_spectrum.pdf",
    )
 
 
def plot_A3_demodulation_crete():
    libplot.plot_signals(
        t_fft,
        {"Signal démodulé (détecteur de crête)": A3_demod_crete},
        title="Démodulation A3 — détecteur de crête",
        save_path="figures/lab1/lab1_A3_demodulation_crete.pdf",
    )
 
 
def plot_A3_demodulation_coherent():
    libplot.plot_signals(
        t,
        {"Signal démodulé (démodulation cohérente)": A3_demod_coherent},
        title="Démodulation A3 — démodulateur cohérent",
        save_path="figures/lab1/lab1_A3_demodulation_coherent.pdf",
    )
 
 
def plot_XY_A3_modulant_module():
    libplot.XY_plot(
        m_fft, A3_signal_fft,
        title="A3 — X-Y : signal modulant vs signal modulé",
        save_path="figures/lab1/lab1_A3_XY_modulant_module.pdf",
    )
 
 
def plot_XY_A3_modulant_demodule_crete():
    libplot.XY_plot(
        m_fft, A3_demod_crete,
        title="A3 — X-Y : modulant vs démodulé (crête)",
        save_path="figures/lab1/lab1_A3_XY_modulant_demodule_crete.pdf",
    )
 
 
def plot_XY_A3_modulant_demodule_coherent():
    libplot.XY_plot(
        m, A3_demod_coherent,
        title="A3 — X-Y : modulant vs démodulé (cohérent)",
        save_path="figures/lab1/lab1_A3_XY_modulant_demodule_coherent.pdf",
    )
 
 
# ---------------------------------------------------------------------------
# Plotting functions — DSB-SC
# ---------------------------------------------------------------------------
 
def plot_DSB_SC_modulation():
    libplot.plot_signals(
        t,
        {"Modulant": m, "Porteuse": c, "Signal DSB-SC": DSB_signal},
        title="Modulation DSB-SC",
        save_path="figures/lab1/lab1_DSB_SC.pdf",
    )
 
 
def plot_DSB_SC_spectrum():
    libplot.plot_spectrum(
        t_fft, DSB_signal_fft,
        title="Spectre du signal DSB-SC",
        save_path="figures/lab1/lab1_DSB_SC_spectrum.pdf",
    )
 
 
def plot_DSB_SC_demodulation_crete():
    libplot.plot_signals(
        t,
        {"Signal démodulé (détecteur de crête)": DSB_demod_crete},
        title="Démodulation DSB-SC — détecteur de crête",
        save_path="figures/lab1/lab1_DSB_SC_demodulation_crete.pdf",
    )
 
 
def plot_DSB_SC_demodulation_coherent():
    libplot.plot_signals(
        t,
        {"Signal démodulé (démodulation cohérente)": DSB_demod_coherent},
        title="Démodulation DSB-SC — démodulateur cohérent",
        save_path="figures/lab1/lab1_DSB_SC_demodulation_coherent.pdf",
    )
 
 
def plot_XY_DSB_SC_modulant_module():
    libplot.XY_plot(
        m_fft, DSB_signal_fft,
        title="DSB-SC — X-Y : signal modulant vs signal modulé",
        save_path="figures/lab1/lab1_DSB_SC_XY_modulant_module.pdf",
    )
 
 
def plot_XY_DSB_SC_modulant_demodule_crete():
    libplot.XY_plot(
        m, DSB_demod_crete,
        title="DSB-SC — X-Y : modulant vs démodulé (crête)",
        save_path="figures/lab1/lab1_DSB_SC_XY_modulant_demodule_crete.pdf",
    )
 
 
def plot_XY_DSB_SC_modulant_demodule_coherent():
    libplot.XY_plot(
        m, DSB_demod_coherent,
        title="DSB-SC — X-Y : modulant vs démodulé (cohérent)",
        save_path="figures/lab1/lab1_DSB_SC_XY_modulant_demodule_coherent.pdf",
    )
 
 
# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
 
if __name__ == "__main__":
    os.makedirs("figures/lab1", exist_ok=True)
 
    # --- A3 ---
    plot_A3_modulation()
    plot_A3_spectrum()
    plot_A3_demodulation_crete()
    plot_A3_demodulation_coherent()
    plot_XY_A3_modulant_module()
    plot_XY_A3_modulant_demodule_crete()
    plot_XY_A3_modulant_demodule_coherent()
 
    # --- DSB-SC ---
    plot_DSB_SC_modulation()
    plot_DSB_SC_spectrum()
    plot_DSB_SC_demodulation_crete()
    plot_DSB_SC_demodulation_coherent()
    plot_XY_DSB_SC_modulant_module()
    plot_XY_DSB_SC_modulant_demodule_crete()
    plot_XY_DSB_SC_modulant_demodule_coherent()