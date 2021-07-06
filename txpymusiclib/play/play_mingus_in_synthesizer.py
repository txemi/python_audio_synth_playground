import copy
from typing import Union

from beartype import beartype
from mingus import core as mingus_core
from mingus.containers import NoteContainer as MingusNoteContainer
from synthesizer import Player, Synthesizer

from txpymusiclib.chords_package import chord_conversion
from txpymusiclib.play.play_floatfreqs_in_syntetizer import play_init
from txpymusiclib.play.play_mode import ScalePlayMode
from txpymusiclib.play.play_txnote_in_synthetizer import play_sequence_txnotes
from txpymusiclib.scales_package import txnotecontainer


@beartype
def play_chord_from_mingus_note_container(player: Player, synthesizer_instance: Synthesizer,
                                          chords: MingusNoteContainer,
                                          duration=1.0):
    hz = [a.to_hertz() for a in chords.notes]
    chord_wave = synthesizer_instance.generate_chord(hz, duration)
    player.play_wave(chord_wave)


@beartype
def play_chord_chord_notation_with_mingus(player: Player, synthesizer_instance: Synthesizer, current_chord_name: str):
    chord_notes = chord_conversion.mingus_chord_to_note_container(current_chord_name)
    assert isinstance(chord_notes, MingusNoteContainer)
    play_chord_from_mingus_note_container(player, synthesizer_instance, chord_notes, 1.0)


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
def play_progressions_roman(progressions: Union[tuple, list]):
    player, synthesizer_instance = play_init()
    for prog in progressions:
        mingus_note_container = chord_conversion.mingus_progression_to_note_container(prog)
        assert isinstance(mingus_note_container, MingusNoteContainer)
        if mingus_note_container is False:
            raise NotImplementedError()
        play_chord_from_mingus_note_container(player, synthesizer_instance, mingus_note_container)


@beartype
def mingus_scale_play(mingus_scale: mingus_core.scales._Scale, duration_secs: float = 0.5, octave=4,
                      mode: ScalePlayMode = ScalePlayMode.octave_and_return):
    # octave=4
    assert isinstance(mingus_scale, mingus_core.scales._Scale)
    tx_note_container_1 = txnotecontainer.TxNoteContainer().build_from_mingus_scale(mingus_scale, octave=octave)

    if mode is ScalePlayMode.octave_and_return or mode is ScalePlayMode.octave:
        first = tx_note_container_1.get_mingus_note_list()[0]
        last = copy.deepcopy(first)
        last.octave = last.octave + 1
        tx_note_container_1.append(last)

    if mode is ScalePlayMode.octave_and_return:
        mingus_notes = list(reversed(tx_note_container_1.get_mingus_note_list()[0:-1]))
        tx_note_container_1.append_all(mingus_notes)

    play_sequence_txnotes(tx_note_container_1, duration_secs=duration_secs)
