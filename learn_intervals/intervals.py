#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Consonance and dissonance in music.

@author: khe
"""
import matplotlib.pyplot as plt
import musthe
from mingus.core import intervals as mingus_core_intervals

from txpymusiclib.interval_package.playground import synth_and_play_and_plot_and_writewav_khe_interval
from txpymusiclib.interval_package.txintervals import interval_example_perfect_consonant_octave, \
    interval_example_imperfect_consonance_major_third, interval_example_dissonance_minor_seconds
from txpymusiclib.note_package import txnote

a = musthe.Note(txnote.note_A.name)
fifth = musthe.Interval('P5')
seventh = musthe.Interval('m7')
a1 = a + fifth

a2 = a + seventh
print(1)

a = mingus_core_intervals.second("E", "C")
b = mingus_core_intervals.minor_second("C")
d = mingus_core_intervals.from_shorthand("A", "3")
e = mingus_core_intervals.determine("C", "E")
f = mingus_core_intervals.measure("C", "D")
print(1)

plt.style.use('seaborn-dark')

synth_and_play_and_plot_and_writewav_khe_interval(interval_example_perfect_consonant_octave)

synth_and_play_and_plot_and_writewav_khe_interval(interval_example_imperfect_consonance_major_third)

synth_and_play_and_plot_and_writewav_khe_interval(interval_example_dissonance_minor_seconds)
