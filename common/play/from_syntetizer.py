from mingus.core import chords as chords

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
def play_chord_from_freqs(player1: Player, synthesizer1: Synthesizer, freqs, duration):
    chord_wave = synthesizer1.generate_chord(freqs, duration)
    player1.play_wave(chord_wave)


@beartype
def play_chord_from_freq_and_chord(player1: Player, synthesizer1: Synthesizer, freq, chord, duration):
    freqs = list(common.txchord.TxChord.freqs_mult(freq, chord))
    play_chord_from_freqs(player1, synthesizer1, freqs, duration)


@beartype
def play_chord_from_symbolic(player: Player, synthesizer_instance: Synthesizer, chords, duration):
    chord_wave = synthesizer_instance.generate_chord(chords, duration)
    player.play_wave(chord_wave)


@beartype
def play_chords_loop(chordseq: list, times: int):
    p, s = play_init()
    for i in range(times):
        for current_chord_name in chordseq:
            mingus_chord = chords.from_shorthand(current_chord_name)
            d = chords.determine(mingus_chord)
            print(current_chord_name + " " + str(mingus_chord) + " " + str(d))
            # fails fluidsynth.play_Note(mingus_chord[0] + '-4')
            chord2 = [x + "4" for x in mingus_chord]
            play_chord_from_symbolic(p, s, chord2, 1.0)
