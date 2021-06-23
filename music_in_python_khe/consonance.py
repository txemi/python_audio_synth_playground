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
note_E4 = 'E4'
note_c4 = 'c4'
interval_example_perfect_consonant_octave = (note_C4, note_C5)  # Perfect Consonance (Octave)


@beartype
def synt_and_play_and_plot_and_writewav_interval(consonant_interval_example, plot_title1: str, plot_label1: str):
    C4 = common.synt_wave.from_numpy_khe.get_sine_wave(note_freqs[consonant_interval_example[0]], 2,
                                                       amplitude=2048)  # Middle C
    C5 = common.synt_wave.from_numpy_khe.get_sine_wave(note_freqs[consonant_interval_example[1]], 2,
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
    plt.savefig('data/' + plot_label1.lower().replace(" ", "_") + '.jpg')


synt_and_play_and_plot_and_writewav_interval(interval_example_perfect_consonant_octave, 'Perfect Consonance (Octave)',
                                             'Octave')
##############################################################################
# Imperfect Consonance (Major Thirds)
##############################################################################

interval_example_imperfect_consonance_major_third = (note_C4, note_E4)  # Imperfect Consonance (Major Thirds)

synt_and_play_and_plot_and_writewav_interval(interval_example_imperfect_consonance_major_third,
                                             'Imperfect Consonance (Major Thirds)', 'Major Thirds')

##############################################################################
# Dissonance (Minor Seconds)
##############################################################################

interval_example_dissonance_minor_seconds = (note_C4, note_c4)  # Dissonance (Minor Seconds)

synt_and_play_and_plot_and_writewav_interval(interval_example_dissonance_minor_seconds,
                                             'Perfect Consonance (Minor Seconds)', 'Minor Seconds')
