# https://github.com/yuma-m/synthesizer
from synthesizer import Player, Synthesizer, Waveform

from common.txintervals import TxChord, TxIntervals
from common.txtone import TxTones

from common import txintervals

player = Player()
player.open_stream()
synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)

uu = synthesizer.generate_constant_wave(TxTones.A4_freq, 1.0)
player.play_wave(uu)

player.play_wave(synthesizer.generate_chord(TxTones.A4, 2.0))

iu = synthesizer.generate_chord(TxChord.c3_major_chord_names, 3.0)
player.play_wave(iu)

player.play_wave(synthesizer.generate_chord(TxChord.C4_major_chord_freqs, 3.0))

for chord1 in TxChord.Type.all:
    rrr = txintervals.TxChord.freqs_mult(TxTones.A4_freq, chord1)
    aaa = synthesizer.generate_chord(rrr)
    player.play_wave(aaa, 2.0)
