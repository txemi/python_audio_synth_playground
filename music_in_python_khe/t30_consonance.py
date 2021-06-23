#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Consonance and dissonance in music.

@author: khe
"""
import matplotlib.pyplot as plt

from common.interval_package.playground import synth_and_play_and_plot_and_writewav_interval
from common.interval_package.txintervals import interval_example_perfect_consonant_octave, \
    interval_example_imperfect_consonance_major_third, interval_example_dissonance_minor_seconds
from common.note_package import note_freq_funcs

plt.style.use('seaborn-dark')

note_freqs = note_freq_funcs.get_piano_notes_khe()

synth_and_play_and_plot_and_writewav_interval(note_freqs, interval_example_perfect_consonant_octave,
                                             'Perfect Consonance (Octave)',
                                             'Octave')

synth_and_play_and_plot_and_writewav_interval(note_freqs, interval_example_imperfect_consonance_major_third,
                                             'Imperfect Consonance (Major Thirds)', 'Major Thirds')

synth_and_play_and_plot_and_writewav_interval(note_freqs, interval_example_dissonance_minor_seconds,
                                             'Perfect Consonance (Minor Seconds)', 'Minor Seconds')
