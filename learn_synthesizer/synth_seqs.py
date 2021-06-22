# https://github.com/yuma-m/synthesizer
from common.play.from_syntetizer import play_sequence_notes, play_scale
from common import tx_scale
from common import txtone

play_scale(txtone.TxTones.A4_freq, tx_scale.blues, 0.2)
play_sequence_notes(tx_scale.c_major_scale, 0.3)
