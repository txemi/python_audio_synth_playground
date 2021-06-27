#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mimic a middle C on the piano.

@author: khe
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

from txpymusiclib import synt_wave
from txpymusiclib.note_package import note_freq_funcs
from txpymusiclib.note_package import note_names_and_freq_static
from txpymusiclib.synt_wave import synt_song_khe, sample_rates

plt.style.use('seaborn-dark')

# Get middle C frequency
note_freqs = note_freq_funcs.get_piano_notes_khe()
frequency = note_freqs[note_names_and_freq_static.note_C4.name]

# Pure sine synt_wave
sine_wave = synt_wave.from_numpy_khe.get_sine_wave(frequency, duration=2, amplitude=2048)
wavfile.write('data/pure_c.wav', rate=sample_rates.sample_rate_44100, data=sine_wave.astype(np.int16))

# Load data from wav file
sample_rate, middle_c = wavfile.read('data/piano_c.wav')

# Plot sound synt_wave
plt.plot(middle_c[500:2500])
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Sound Wave of Middle C on Piano')
plt.grid()
plt.savefig('data/piano_sound_wave.jpg')

# FFT
t = np.arange(middle_c.shape[0])
freq = np.fft.fftfreq(t.shape[-1]) * sample_rate
sp = np.fft.fft(middle_c)

# Plot spectrum
plt.plot(freq, abs(sp.real))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Spectrum of Middle C Recording on Piano')
plt.xlim((0, 2000))
plt.grid()
plt.savefig('data/spectrum.jpg')

# Get positive frequency
idx = np.where(freq > 0)[0]
freq = freq[idx]
sp = sp[idx]

# Get dominant frequencies
sort = np.argsort(-abs(sp.real))[:100]
dom_freq = freq[sort]

# Round and calculate amplitude ratio
freq_ratio = np.round(dom_freq / frequency)
unique_freq_ratio = np.unique(freq_ratio)
amp_ratio = abs(sp.real[sort] / np.sum(sp.real[sort]))
factor = np.zeros((int(unique_freq_ratio[-1]),))
for i in range(factor.shape[0]):
    idx = np.where(freq_ratio == i + 1)[0]
    factor[i] = np.sum(amp_ratio[idx])
factor = factor / np.sum(factor)

# Construct harmonic series
note = synt_song_khe.apply_overtones(frequency, duration=2.5, factor=factor)

# Apply smooth ADSR weights
weights = synt_song_khe.get_adsr_weights(frequency, duration=2.5, length=[0.05, 0.25, 0.55, 0.15],
                                         decay=[0.075, 0.02, 0.005, 0.1], sustain_level=0.1)

# Write to file
data = note * weights
data = data * (4096 / np.max(data))  # Adjusting the Amplitude
wavfile.write('data/synthetic_c.wav', sample_rate, data.astype(np.int16))
