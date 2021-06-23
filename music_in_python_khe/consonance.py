#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Consonance and dissonance in music.

@author: khe
"""
import matplotlib.pyplot as plt
import numpy as np
from beartype import beartype
from scipy.io import wavfile

import common.synt_wave.from_numpy_khe
import common.txtone

plt.style.use('seaborn-dark')
from common.play.from_pytheory import playKatiNotes

note_freqs = common.txtone.get_piano_notes_khe()

##############################################################################
# Perfect Consonance (Octave)
##############################################################################
note_C4 = 'C4'  # Middle C
note_C5 = 'C5'  # C one octave above
interval_example_perfect_consonant_octave = (note_C4, note_C5) # Perfect Consonance (Octave)


@beartype
def synt_and_play_and_plot_and_writewav_interval(consonant_interval_example, plot_title1: str, plot_label1:str):
    C4 = common.buildwave.from_numpy_khe.get_sine_wave(note_freqs[consonant_interval_example[0]], 2,
                                                       amplitude=2048)  # Middle C
    C5 = common.buildwave.from_numpy_khe.get_sine_wave(note_freqs[consonant_interval_example[1]], 2,
                                                       amplitude=2048)  # C one octave above
    playKatiNotes(consonant_interval_example[0], consonant_interval_example[1])
    wavfile.write('data/octave.wav', rate=44100, data=((C4 + C5) / 2).astype(np.int16))

    plt.figure(figsize=(12, 4))
    plt.plot(C4[:2500], label=consonant_interval_example[1])
    plt.plot(C5[:2500], label=consonant_interval_example[1])
    plt.plot((C4 + C5)[:2500], label=plot_label1)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title(plot_title1)
    plt.grid()
    plt.legend()
    plt.savefig('data/' + plot_label1.tolower() + '.jpg')


synt_and_play_and_plot_and_writewav_interval(interval_example_perfect_consonant_octave, 'Perfect Consonance (Octave)', 'Octave')
##############################################################################
# Imperfect Consonance (Major Thirds)
##############################################################################
C4 = common.buildwave.from_numpy_khe.get_sine_wave(note_freqs['C4'], 2, amplitude=2048)  # Middle C
E4 = common.buildwave.from_numpy_khe.get_sine_wave(note_freqs['E4'], 2, amplitude=2048)  # E just above
playKatiNotes('C4', 'E4')
wavfile.write('data/major_thirds.wav', rate=44100, data=((C4 + E4) / 2).astype(np.int16))

plt.figure(figsize=(12, 4))
plt.plot(C4[:2500], label='C4')
plt.plot(E4[:2500], label='E4')
plt.plot((C4 + E4)[:2500], label='Thirds')
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
wavfile.write('data/minor_seconds.wav', rate=44100, data=((C4 + c4) / 2).astype(np.int16))

plt.figure(figsize=(12, 4))
plt.plot(C4[:2500], label='C4')
plt.plot(c4[:2500], label='c4')
plt.plot((C4 + c4)[:2500], label='Seconds')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Perfect Consonance (Minor Seconds)')
plt.grid()
plt.legend()
plt.savefig('data/minor_seconds.jpg')
