import common.txchord
from beartype import beartype
from synthesizer import Player, Synthesizer, Waveform

@beartype
def play_chord(player1: Player, synthesizer1: Synthesizer, freq, chord):
    freqs = list(common.txchord.TxChord.freqs_mult(freq, chord))
    chord_wave = synthesizer1.generate_chord(freqs, 2.0)
    player1.play_wave(chord_wave)
