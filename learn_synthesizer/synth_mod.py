# https://github.com/yuma-m/synthesizer
from synthesizer import Player, Synthesizer, Waveform

from common.txintervals import TxChord, TxIntervals
from common.txtone import TxTones

from common import txintervals

player = Player()
player.open_stream()
synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)

wave_A4 = synthesizer.generate_constant_wave(TxTones.A4_freq, 1.0)
player.play_wave(wave_A4)

player.play_wave(synthesizer.generate_chord(TxTones.A4, 2.0))

wave_C3_major_chord = synthesizer.generate_chord(TxChord.c3_major_chord_names, 3.0)
player.play_wave(wave_C3_major_chord)

player.play_wave(synthesizer.generate_chord(TxChord.C4_major_chord_freqs, 3.0))

for current_chord in TxChord.Type.all:
    freqs =list(txintervals.TxChord.freqs_mult(TxTones.A4_freq, current_chord))
    chord_wave = synthesizer.generate_chord(freqs, 2.0)
    player.play_wave(chord_wave)
