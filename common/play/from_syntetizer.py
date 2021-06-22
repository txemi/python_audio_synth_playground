import common.play
import common.txchord
from beartype import beartype
from synthesizer import Player, Synthesizer, Waveform


@beartype
def play_init():
    player = Player()
    player.open_stream()
    synthesizer_instance = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    return player, synthesizer_instance


@beartype
def play_wave(player: Player, synthesizer_instance: Synthesizer, freq, duration):
    wave_A4 = synthesizer_instance.generate_constant_wave(freq, duration)
    player.play_wave(wave_A4)


@beartype
def play_chord1(player1: Player, synthesizer1: Synthesizer, freqs, duration):
    chord_wave = synthesizer1.generate_chord(freqs, duration)
    player1.play_wave(chord_wave)


@beartype
def play_chord2(player1: Player, synthesizer1: Synthesizer, freq, chord, duration):
    freqs = list(common.txchord.TxChord.freqs_mult(freq, chord))
    play_chord1(player1, synthesizer1, freqs, duration)


@beartype
def play_chord3(player: Player, synthesizer_instance: Synthesizer, chords, duration):
    wave_C3_major_chord = synthesizer_instance.generate_chord(chords, duration)
    player.play_wave(wave_C3_major_chord)
