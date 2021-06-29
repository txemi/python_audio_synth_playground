from beartype import beartype
from mingus.containers import NoteContainer as MingusNoteContainer
from synthesizer import Player, Synthesizer

from txpymusiclib.chords_package import chord_conversion
from txpymusiclib.play.play_floatfreqs_in_syntetizer import play_init


@beartype
def play_chord_from_symbolic_mingus(player: Player, synthesizer_instance: Synthesizer, chords: MingusNoteContainer,
                                    duration=1.0):
    hz = [a.to_hertz() for a in chords.notes]
    chord_wave = synthesizer_instance.generate_chord(hz, duration)
    player.play_wave(chord_wave)


@beartype
def play_chord_chord_notation_with_mingus(player: Player, synthesizer_instance: Synthesizer, current_chord_name: str):
    chord_notes = chord_conversion.mingus_chord_to_notes(current_chord_name)
    play_chord_from_symbolic_mingus(player, synthesizer_instance, chord_notes, 1.0)


@beartype
def play_chords_chord_notation_with_mingus(player: Player, synthesizer_instance: Synthesizer, chordseq: (list, tuple)):
    for current_chord_name in chordseq:
        play_chord_chord_notation_with_mingus(player, synthesizer_instance, current_chord_name)


@beartype
def play_chords_loop_chord_notation(chordseq: (list[str], tuple), times: int):
    player, synt = play_init()
    for i in range(times):
        play_chords_chord_notation_with_mingus(player, synt, chordseq)


@beartype
def play_progressions(progressions: tuple[str]):
    player, synthesizer_instance = play_init()
    for prog in progressions:
        nc = chord_conversion.mingus_progression_to_notes(prog)
        play_chord_from_symbolic_mingus(player, synthesizer_instance, nc)