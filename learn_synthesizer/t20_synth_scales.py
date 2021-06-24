# https://github.com/yuma-m/synthesizer
import time

import txpymusiclib.scales_package.scale_static_examples_from_note_names
from txpymusiclib.note_package import note_names_and_freq_static
from txpymusiclib.play.from_syntetizer import play_sequence_notes, play_scale_from_freq
from txpymusiclib.scales_package import scale_static_examples

play_sequence_notes(txpymusiclib.scales_package.scale_static_examples_from_note_names.c_major_scale, 0.3)
time.sleep(1)
play_scale_from_freq(note_names_and_freq_static.note_A4.freq, scale_static_examples.major, 0.2)
time.sleep(1)
play_scale_from_freq(note_names_and_freq_static.note_A4.freq, scale_static_examples.blues, 0.2)
time.sleep(1)
play_scale_from_freq(note_names_and_freq_static.note_A4.freq, scale_static_examples.doble_armonica, 0.2)
