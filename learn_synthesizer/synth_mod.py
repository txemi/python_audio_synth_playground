# https://github.com/yuma-m/synthesizer
from synthesizer import Player, Synthesizer, Waveform

from common.txchord import TxChord
from common.txtone import TxTones

from common.play.from_syntetizer import play_chord

player = Player()
player.open_stream()
synthesizer_instance = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)

wave_A4 = synthesizer_instance.generate_constant_wave(TxTones.A4_freq, 1.0)
player.play_wave(wave_A4)

player.play_wave(synthesizer_instance.generate_chord(TxTones.A4, 2.0))

wave_C3_major_chord = synthesizer_instance.generate_chord(TxChord.c3_major_chord_names, 3.0)
player.play_wave(wave_C3_major_chord)

player.play_wave(synthesizer_instance.generate_chord(TxChord.C4_major_chord_freqs, 3.0))

for current_chord in TxChord.Type.all:
    play_chord(player,synthesizer_instance,TxTones.A4_freq, current_chord)
