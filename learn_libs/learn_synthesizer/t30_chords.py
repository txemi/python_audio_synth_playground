# https://github.com/yuma-m/synthesizer
from txpymusiclib.chords_package.txchord import TxChord
from txpymusiclib.note_package import note_names_and_freq_static
from txpymusiclib.play.from_syntetizer import play_chord_from_freq_and_chord, play_init, play_chord_from_symbolic, \
    play_chord_from_freqs

player, synthesizer_instance = play_init()

play_chord_from_freqs(player, synthesizer_instance, TxChord.C4_major_chord_freqs, 3.0)

for current_chord in TxChord.Type.all:
    play_chord_from_freq_and_chord(player, synthesizer_instance, note_names_and_freq_static.note_A4.freq, current_chord,
                                   1.0)

play_chord_from_symbolic(player, synthesizer_instance, [note_names_and_freq_static.note_A4.name], 2.0)

play_chord_from_symbolic(player, synthesizer_instance, TxChord.c3_major_chord_names, 3.0)
