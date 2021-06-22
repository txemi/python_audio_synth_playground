# https://github.com/yuma-m/synthesizer
from common.txchord import TxChord
from common.txtone import TxTones
from common.play.from_syntetizer import play_chord_from_freq_and_chord, play_init, play_wave, play_chord_from_symbolic, play_chord_from_freqs

player, synthesizer_instance = play_init()

play_wave(player, synthesizer_instance, TxTones.A4_freq, 1.0)


