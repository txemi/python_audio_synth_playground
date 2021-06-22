# https://github.com/yuma-m/synthesizer
import common.play.from_syntetizer
from common.txchord import TxChord
from common.txtone import TxTones

from common.play.from_syntetizer import play_chord2, play_init, play_wave, play_chord3, play_chord1

player, synthesizer_instance = play_init()

play_wave(player, synthesizer_instance, TxTones.A4_freq, 1.0)

play_chord1(player, synthesizer_instance, TxChord.C4_major_chord_freqs, 3.0)

for current_chord in TxChord.Type.all:
    play_chord2(player, synthesizer_instance, TxTones.A4_freq, current_chord, 1.0)

play_chord3(player, synthesizer_instance, TxTones.A4, 2.0)

play_chord3(player, synthesizer_instance, TxChord.c3_major_chord_names, 3.0)
