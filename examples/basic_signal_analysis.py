import numpy as np
from src.filters import apply_lowpass_filter

# Generate a sample noisy signal
fs = 500  # Sampling frequency
t = np.linspace(0, 1, fs)
signal = np.sin(2 * np.pi * 50 * t) + 0.5 * np.random.randn(fs)

# Apply a lowpass filter
filtered_signal = apply_lowpass_filter(signal, cutoff=30, fs=fs)