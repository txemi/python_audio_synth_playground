# https://github.com/yuma-m/synthesizer
import time

import txpymusiclib.scales_package.scale_static_examples_from_note_names
from txpymusiclib.note_package import txnote_khe_wrap
from txpymusiclib.play.play_txnote_in_synthetizer import play_sequence_txnotes, play_scale_from_freq
from txpymusiclib.scales_package import txscales_examples

play_sequence_txnotes(txpymusiclib.scales_package.scale_static_examples_from_note_names.c_major_scale_notes_2, 0.3)
time.sleep(1)
play_scale_from_freq(txnote_khe_wrap.note_A4.freq, txscales_examples.major, 0.2)
time.sleep(1)
play_scale_from_freq(txnote_khe_wrap.note_A4.freq, txscales_examples.blues, 0.2)
time.sleep(1)
play_scale_from_freq(txnote_khe_wrap.note_A4.freq, txscales_examples.doble_armonica, 0.2)
