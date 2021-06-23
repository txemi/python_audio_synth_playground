# https://github.com/yuma-m/synthesizer
import common.tonepackage.note_names_and_freq_static
from common.play.from_syntetizer import play_sequence_notes, play_scale_from_freq
from common import tx_scale
from common.tonepackage import note_conversions
import time

play_sequence_notes(tx_scale.c_major_scale, 0.3)
time.sleep(1)
play_scale_from_freq(common.tonepackage.note_names_and_freq_static.TxTones.A4_freq, tx_scale.mayor, 0.2)
time.sleep(1)
play_scale_from_freq(common.tonepackage.note_names_and_freq_static.TxTones.A4_freq, tx_scale.blues, 0.2)
time.sleep(1)
play_scale_from_freq(common.tonepackage.note_names_and_freq_static.TxTones.A4_freq, tx_scale.doble_armonica, 0.2)
