#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Consonance and dissonance in music.

@author: khe
"""
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

import common.buildwave.from_numpy_khe
import common.txtone

plt.style.use('seaborn-dark')
from common import utils_khe
from common.play.from_pytheory import playKatiNotes

note_freqs = common.txtone.get_piano_notes()

##############################################################################
# Perfect Consonance (Octave)
##############################################################################
C4 = common.buildwave.from_numpy_khe.get_sine_wave(note_freqs['C4'], 2, amplitude=2048)  # Middle C
C5 = common.buildwave.from_numpy_khe.get_sine_wave(note_freqs['C5'], 2, amplitude=2048)  # C one octave above
playKatiNotes('C4', 'C5')
wavfile.write('data/octave.wav', rate=44100, data=((C4+C5)/2).astype(np.int16))

plt.figure(figsize=(12,4))
plt.plot(C4[:2500], label='C4')
plt.plot(C5[:2500], label='C5')
plt.plot((C4+C5)[:2500], label='Octave')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Perfect Consonance (Octave)')
plt.grid()
plt.legend()
plt.savefig('data/octave.jpg')

##############################################################################
# Imperfect Consonance (Major Thirds)
##############################################################################
C4 = common.buildwave.from_numpy_khe.get_sine_wave(note_freqs['C4'], 2, amplitude=2048)  # Middle C
E4 = common.buildwave.from_numpy_khe.get_sine_wave(note_freqs['E4'], 2, amplitude=2048)  # E just above
playKatiNotes('C4', 'E4')
wavfile.write('data/major_thirds.wav', rate=44100, data=((C4+E4)/2).astype(np.int16))

plt.figure(figsize=(12,4))
plt.plot(C4[:2500], label='C4')
plt.plot(E4[:2500], label='E4')
plt.plot((C4+E4)[:2500], label='Thirds')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Perfect Consonance (Major Thirds)')
plt.grid()
plt.legend()
plt.savefig('data/major_thirds.jpg')

##############################################################################
# Dissonance (Minor Seconds)
##############################################################################
C4 = common.buildwave.from_numpy_khe.get_sine_wave(note_freqs['C4'], 2, amplitude=2048)  # Middle C
c4 = common.buildwave.from_numpy_khe.get_sine_wave(note_freqs['c4'], 2, amplitude=2048)  # C sharp/D flat
playKatiNotes('C4', 'c4')
wavfile.write('data/minor_seconds.wav', rate=44100, data=((C4+c4)/2).astype(np.int16))

plt.figure(figsize=(12,4))
plt.plot(C4[:2500], label='C4')
plt.plot(c4[:2500], label='c4')
plt.plot((C4+c4)[:2500], label='Seconds')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Perfect Consonance (Minor Seconds)')
plt.grid()
plt.legend()
plt.savefig('data/minor_seconds.jpg')