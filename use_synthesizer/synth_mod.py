from synthesizer import Player, Synthesizer, Waveform

from common.tones import A4_freq, C_major_chord
from common import tones

player = Player()
player.open_stream()
synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
# Play A4
player.play_wave(synthesizer.generate_constant_wave(A4_freq, 1.0))

player.play_wave(synthesizer.generate_chord(tones.acorde(A4_freq), 2.0))

# Play C major
player.play_wave(synthesizer.generate_chord(C_major_chord, 3.0))
