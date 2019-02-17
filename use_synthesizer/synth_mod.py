from synthesizer import Player, Synthesizer, Waveform

from common.tones import Chord, Intervals, Tones

from common import tones

player = Player()
player.open_stream()
synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
# Play A4
player.play_wave(synthesizer.generate_constant_wave(Tones.A4_freq, 1.0))

player.play_wave(synthesizer.generate_chord(tones.Chord.chord_major_freqs(Tones.A4_freq, Chord.Type.major), 2.0))
player.play_wave(synthesizer.generate_chord(tones.Chord.chord_major_freqs(Tones.A4_freq, Chord.Type.minor), 2.0))
player.play_wave(synthesizer.generate_chord(tones.Chord.chord_major_freqs(Tones.A4_freq, Chord.Type.dim), 2.0))
player.play_wave(synthesizer.generate_chord(tones.Chord.chord_major_freqs(Tones.A4_freq, Chord.Type.aug), 2.0))

# Play C major
player.play_wave(synthesizer.generate_chord(Chord.C_major_chord, 3.0))
