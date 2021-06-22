# https://github.com/yuma-m/synthesizer
from common.txchord import TxChord
from common.txtone import TxTones
from common.play.from_syntetizer import play_chord_from_freq_and_chord, play_init, play_wave, play_chord_from_symbolic, play_chord_from_freqs

player, synthesizer_instance = play_init()



play_chord_from_freqs(player, synthesizer_instance, TxChord.C4_major_chord_freqs, 3.0)

for current_chord in TxChord.Type.all:
    play_chord_from_freq_and_chord(player, synthesizer_instance, TxTones.A4_freq, current_chord, 1.0)

play_chord_from_symbolic(player, synthesizer_instance, TxTones.A4, 2.0)

play_chord_from_symbolic(player, synthesizer_instance, TxChord.c3_major_chord_names, 3.0)
