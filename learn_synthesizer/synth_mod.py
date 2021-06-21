# https://github.com/yuma-m/synthesizer
from synthesizer import Player, Synthesizer, Waveform

from common.txintervals import TxChord, TxIntervals
from common.txtone import TxTones

from common import txintervals

player = Player()
player.open_stream()
synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
# Play A4
player.play_wave(synthesizer.generate_constant_wave(TxTones.A4_freq, 1.0))

chord = ["A4"]
player.play_wave(synthesizer.generate_chord(chord, 2.0))

chord = ["C3", "E3", "G3"]
player.play_wave(synthesizer.generate_chord(chord, 3.0))

player.play_wave(synthesizer.generate_chord(txintervals.Chord.freqs_mult(TxTones.A4_freq, TxChord.Type.major), 2.0))
player.play_wave(synthesizer.generate_chord(txintervals.Chord.freqs_mult(TxTones.A4_freq, TxChord.Type.minor), 2.0))
player.play_wave(synthesizer.generate_chord(txintervals.Chord.freqs_mult(TxTones.A4_freq, TxChord.Type.dim), 2.0))
player.play_wave(synthesizer.generate_chord(txintervals.Chord.freqs_mult(TxTones.A4_freq, TxChord.Type.aug), 2.0))

# Play C major
player.play_wave(synthesizer.generate_chord(TxChord.C_major_chord, 3.0))
