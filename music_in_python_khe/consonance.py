#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Consonance and dissonance in music.

@author: khe
"""
import matplotlib.pyplot as plt

import common.tonepackage.note_conversions
import common.tonepackage.note_freq_funcs
from common.interval_package.playground import synt_and_play_and_plot_and_writewav_interval
from common.interval_package.txintervals import interval_example_perfect_consonant_octave, \
    interval_example_imperfect_consonance_major_third, interval_example_dissonance_minor_seconds

plt.style.use('seaborn-dark')

note_freqs = common.tonepackage.note_freq_funcs.get_piano_notes_khe()



synt_and_play_and_plot_and_writewav_interval(interval_example_perfect_consonant_octave, 'Perfect Consonance (Octave)',
                                             'Octave')


synt_and_play_and_plot_and_writewav_interval(interval_example_imperfect_consonance_major_third,
                                             'Imperfect Consonance (Major Thirds)', 'Major Thirds')


synt_and_play_and_plot_and_writewav_interval(interval_example_dissonance_minor_seconds,
                                             'Perfect Consonance (Minor Seconds)', 'Minor Seconds')
