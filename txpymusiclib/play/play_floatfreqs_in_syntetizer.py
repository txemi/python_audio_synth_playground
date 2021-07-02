from beartype import beartype
from synthesizer import Player, Synthesizer, Waveform

from txpymusiclib.interval_package import txintervals


@beartype
def play_init():
    player = Player()
    player.open_stream()
    synthesizer_instance = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    return player, synthesizer_instance


@beartype
def play_wave(player: Player, synthesizer_instance: Synthesizer, freq, duration_in_secs: float):
    wave_data = synthesizer_instance.generate_constant_wave(freq, duration_in_secs)
    player.play_wave(wave_data)


@beartype
def play_sequence_freqs(freqs, duration_seqs: float):
    player, synthesizer_instance = play_init()
    for freq in freqs:
        play_wave(player, synthesizer_instance, freq, duration_seqs)


@beartype
def play_chord_from_freqs(player1: Player, synthesizer1: Synthesizer, freqs, duration):
    chord_wave = synthesizer1.generate_chord(freqs, duration)
    player1.play_wave(chord_wave)


@beartype
def play_chord_from_freq_and_chord(player1: Player, synthesizer1: Synthesizer, freq: float, chord, duration):
    freqs = list(txintervals.do_interval_jumps_to_freq(freq, chord))
    play_chord_from_freqs(player1, synthesizer1, freqs, duration)


