import time

from beartype import beartype
from mingus.containers import Note as MingusNote
from mingus.containers import NoteContainer as MingusNoteContainer
from musthe import Scale as MustheScale
from synthesizer import Player, Synthesizer, Waveform

from common.chords_package.chord_conversion import mingus_chord_to_notes
from common.interval_package import txintervals
from common.note_package import note_conversions
from common.note_package import note_freq_funcs
from common.scales_package.scale_functions import musthescale_notes


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
def play_sequence_notes(notes, duration_secs: float):
    note2freq = note_freq_funcs.get_piano_notes_mingus()
    freqs = [note2freq[note_conversions.notestr2mingus_int(note)] for note in notes]
    play_sequence_freqs(freqs, duration_secs)


@beartype
def play_scale_from_freq(freq: float, scale, duration_secons: float):
    freqs = list(txintervals.freqs_mult_accumulate(freq, scale))
    tail = list(reversed(freqs))[1:]
    print(freqs)
    play_sequence_freqs(freqs + tail, duration_secons)


@beartype
def play_scale_from_musthescale(current_scale: MustheScale):
    notes_in_scale, description = musthescale_notes(current_scale)
    print(description)
    play_sequence_notes(notes_in_scale, 0.5)
    time.sleep(1)


@beartype
def play_chord_from_freqs(player1: Player, synthesizer1: Synthesizer, freqs, duration):
    chord_wave = synthesizer1.generate_chord(freqs, duration)
    player1.play_wave(chord_wave)


@beartype
def play_chord_from_freq_and_chord(player1: Player, synthesizer1: Synthesizer, freq: float, chord, duration):
    freqs = list(txintervals.freqs_mult(freq, chord))
    play_chord_from_freqs(player1, synthesizer1, freqs, duration)


@beartype
def play_chord_from_symbolic(player: Player, synthesizer_instance: Synthesizer, chords: MingusNoteContainer, duration):
    hz = [a.to_hertz() for a in chords.notes]
    chord_wave = synthesizer_instance.generate_chord(hz, duration)
    player.play_wave(chord_wave)


@beartype
def play_chord_chord_notation(player: Player, synthesizer_instance: Synthesizer, current_chord_name: str):
    chord_notes = mingus_chord_to_notes(current_chord_name)
    play_chord_from_symbolic(player, synthesizer_instance, chord_notes, 1.0)


@beartype
def play_chords_chord_notation(player: Player, synthesizer_instance: Synthesizer, chordseq: (list, tuple)):
    for current_chord_name in chordseq:
        play_chord_chord_notation(player, synthesizer_instance, current_chord_name)


@beartype
def play_chords_loop_chord_notation(chordseq: (list, tuple), times: int):
    player, synt = play_init()
    for i in range(times):
        play_chords_chord_notation(player, synt, chordseq)
