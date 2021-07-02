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
from txpymusiclib.interval_package.txintervals import TxKheIntervalExample
from txpymusiclib.interval_package.txintervals import interval_example_perfect_consonant_octave, \
    interval_example_imperfect_consonance_major_third, interval_example_dissonance_minor_seconds
from txpymusiclib.note_package import txnote_khe_wrap
from txpymusiclib.note_package.convert_khe_musthe import musthe_note_to_txkhenote
from txpymusiclib.note_package.txnote_khe_wrap import TxNoteKheWrap

plt.style.use('seaborn-dark')


def note_musthe_2_mingus_name(musthe_note: musthe.Note):
    # TODO: handel octave
    return musthe_note.letter.name


def check_fifth():
    note_A = musthe.Note(txnote_khe_wrap.note_A.khe_name)
    fifth = musthe.Interval('P5')
    seventh = musthe.Interval('m7')
    note_A_plus_fifth = note_A + fifth
    note_A_plus_seventh = note_A + seventh
    according_to_mingus = mingus_core_intervals.fifth(note_musthe_2_mingus_name(note_A), 'C')
    assert note_A_plus_seventh.letter.name == according_to_mingus
    fifth_txinterval = TxKheIntervalExample(TxNoteKheWrap(musthe_note_to_txkhenote(note_A)),
                                            TxNoteKheWrap(musthe_note_to_txkhenote(note_A_plus_fifth)), 'seventh',
                                            'seventh')
    synth_and_play_and_plot_and_writewav_khe_interval(fifth_txinterval)


check_fifth()
a = mingus_core_intervals.second("E", "C")
b = mingus_core_intervals.minor_second("C")
d = mingus_core_intervals.from_shorthand("A", "3")
e = mingus_core_intervals.determine("C", "E")
f = mingus_core_intervals.measure("C", "D")
print(1)

synth_and_play_and_plot_and_writewav_khe_interval(interval_example_perfect_consonant_octave)

synth_and_play_and_plot_and_writewav_khe_interval(interval_example_imperfect_consonance_major_third)

synth_and_play_and_plot_and_writewav_khe_interval(interval_example_dissonance_minor_seconds)
