#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Consonance and dissonance in music.

@author: khe
"""
import time

import matplotlib.pyplot as plt
import musthe
from mingus.core import intervals as mingus_core_intervals

from txpymusiclib.interval_package.playground import synth_and_play_and_plot_and_writewav_khe_interval
from txpymusiclib.interval_package.txintervals import TxKheIntervalExample
from txpymusiclib.interval_package.txintervals import interval_example_perfect_consonant_octave, \
    interval_example_imperfect_consonance_major_third, interval_example_dissonance_minor_seconds
from txpymusiclib.note_package import txnote_khe_wrap
from txpymusiclib.note_package.convert_khe_musthe import musthe_note_to_txkhenote
from txpymusiclib.note_package.convert_mingus_muse import note_musthe_2_mingus_name
from txpymusiclib.note_package.txnote_khe_wrap import TxNoteKheWrap

plt.style.use('seaborn-dark')


def check_interval(musthe_interval_name: str, mingus_interval: int, description: str):
    note_A = musthe.Note(txnote_khe_wrap.note_A.khe_name)
    musthe_interval = musthe.Interval(musthe_interval_name)
    note_A_plus_musthe_fifth = note_A + musthe_interval

    # TODO: take out this
    seventh = musthe.Interval('m7')
    note_A_plus_seventh = note_A + seventh

    # according_to_mingus = mingus_core_intervals.fifth(note_musthe_2_mingus_name(note_A), 'C')
    according_to_mingus = mingus_core_intervals.interval(start_note=note_musthe_2_mingus_name(note_A), key='C',
                                                         interval=mingus_interval)
    try:
        assert note_A_plus_musthe_fifth.letter.name == according_to_mingus
    except:
        raise
    tx_interval = TxKheIntervalExample(TxNoteKheWrap(musthe_note_to_txkhenote(note_A)),
                                       TxNoteKheWrap(musthe_note_to_txkhenote(note_A_plus_musthe_fifth)),
                                       description,
                                       musthe_interval_name)
    synth_and_play_and_plot_and_writewav_khe_interval(tx_interval)
    time.sleep(1)


# no lo entiendo, el segundo argumento
d = mingus_core_intervals.from_shorthand("A", "3")

# cálculo complicado
e = mingus_core_intervals.determine("C", "E")

# comprensible
f = mingus_core_intervals.measure("C", "D")

# el algoritmo de mingus es rarino
b = mingus_core_intervals.minor_second("C")
check_interval(musthe_interval_name='m2', mingus_interval=7, description='minor_seconds')
synth_and_play_and_plot_and_writewav_khe_interval(interval_example_dissonance_minor_seconds)

a = mingus_core_intervals.second(note="E", key="C")
check_interval(musthe_interval_name='M2', mingus_interval=1, description='second')

check_interval(musthe_interval_name='M3', mingus_interval=7, description='major_third')
synth_and_play_and_plot_and_writewav_khe_interval(interval_example_imperfect_consonance_major_third)

check_interval(musthe_interval_name='P5', mingus_interval=4, description='fifth')

check_interval(musthe_interval_name='P8', mingus_interval=7, description='perfect_consonant_octave')
synth_and_play_and_plot_and_writewav_khe_interval(interval_example_perfect_consonant_octave)

print(1)
