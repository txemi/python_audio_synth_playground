# https://github.com/yuma-m/synthesizer
from txpymusiclib.chords_package.txchord import TxChord
from txpymusiclib.note_package import txnote_khe_wrap
from txpymusiclib.play.play_floatfreqs_in_syntetizer import play_chord_from_freq_and_chord, play_init, play_chord_from_freqs
from txpymusiclib.play.play_mingus_in_synthesizer import play_chord_from_mingus_note_container

player, synthesizer_instance = play_init()

play_chord_from_freqs(player, synthesizer_instance, TxChord.C4_major_chord_freqs, 3.0)

for current_chord in TxChord.Type.all:
    play_chord_from_freq_and_chord(player, synthesizer_instance, txnote_khe_wrap.note_A4.freq, current_chord,
                                   1.0)

play_chord_from_mingus_note_container(player, synthesizer_instance, [txnote_khe_wrap.note_A4.khe_name], 2.0)

play_chord_from_mingus_note_container(player, synthesizer_instance, TxChord.c3_major_chord_names, 3.0)
