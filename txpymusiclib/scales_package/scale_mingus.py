import typing
from collections.abc import Iterable
from typing import Generator

from beartype import beartype
from mingus import containers, core as mingus_core
from mingus.containers import Note, NoteContainer
from mingus.containers.note_container import Note as MingusNote
from mingus.core import scales

import txpymusiclib.scales_package.txscales
from txpymusiclib.note_package import txnote_khe_wrap
from txpymusiclib.scales_package.txscales import TxScaleSt


@beartype
def _mingus_names_to_notes(scale_notes: Iterable[str]):
    for note_str in scale_notes:
        assert isinstance(note_str, str)
        if True:
            try:
                mingus_note = containers.Note(name=note_str[:-1], octave=int(note_str[-1:]))
            except:
                mingus_note = containers.Note(name=note_str[:-1], octave=int(note_str[-1:]))
                raise
        else:
            # from_shorthand es otra cosa NO USAR
            mingus_note = containers.Note().from_shorthand(note_str)
            mingus_note.octave = int(note_str[-1:])
        yield mingus_note


@beartype
def mingus_names_to_mingusnotecontainer(scale_notes: Iterable[str]) -> NoteContainer:
    return NoteContainer(_mingus_names_to_notes(scale_notes))


@beartype
def _generate_all_scales() -> typing.Generator[scales._Scale, None, None]:
    """
    """

    for key in scales.keys:
        for scale in scales._Scale.__subclasses__():
            if "diatonic" in str(scale).lower():
                continue
            if scale.type == "major":
                yield scale(key[0])
            elif scale.type == "minor":
                yield scale(scales.get_notes(key[1])[0])
            elif scale.type == "ancient" or scale.type == "other":
                yield scale(key[0])
            else:
                raise NotImplementedError()


@beartype
def find_scale_by_name(scale_name: str) -> scales._Scale:
    for current_scale in _generate_all_scales():
        if current_scale.name == scale_name:
            return current_scale


@beartype
def _get_semitones_from_mingus_notes_2(ascending):
    last = None
    modifier = 0
    for mingus_note in ascending:
        assert isinstance(mingus_note, MingusNote)
        cur = int(mingus_note) + modifier
        if last is not None:
            diff = cur - last
            if diff < 0:
                modifier = 12
                cur = cur + modifier
                diff = cur - last
            elif diff > 12:
                modifier = -12
                cur = cur + modifier
                diff = cur - last
            yield diff
        last = cur


@beartype
def mingus_note_str_to_mingus_note(note_str: str, octave: int) -> Note:
    try:
        if len(note_str) < 1:
            raise NotImplementedError()
    except:
        raise
    # mingus_note = Note().from_shorthand(note_str[:1])
    mingus_note = Note(name=note_str[:1], octave=octave)
    for note_decorator in note_str[1:]:
        if note_decorator == 'b':
            mingus_note.diminish()
        elif note_decorator == '#':
            mingus_note.augment()
        else:
            raise NotImplementedError()
    return mingus_note


@beartype
def mingus_scale_to_notes(mingus_scale: scales._Scale, octave: int) -> Generator[Note, None, None]:
    # scales._Scale
    try:
        ascending = mingus_scale.ascending()
    except:
        raise
    for note in ascending:
        yield mingus_note_str_to_mingus_note(note, octave=octave)


@beartype
def _get_semitones_from_mingus_notes(ascending: Iterable[Note]):
    last = -1
    modifier = 0
    for mingus_note in ascending:

        cur = int(mingus_note) + modifier
        if last != -1:
            diff = cur - last
            if diff < 0:
                modifier = 12
                cur = cur + modifier
                diff = cur - last
            yield diff
        last = cur


@beartype
def _get_semitones_from_mingus_scale(mingus_scale: scales._Scale, octave: int):
    return _get_semitones_from_mingus_notes(mingus_scale_to_notes(mingus_scale, octave=octave))


@beartype
def get_semitones_from_mingus_scale(mingus_scale: scales._Scale, octave: int) -> TxScaleSt:
    return TxScaleSt(list(_get_semitones_from_mingus_scale(mingus_scale, octave=octave)))


@beartype
def find_scale_by_semitones(scale_interval_semitones: txpymusiclib.scales_package.txscales.TxScaleSt) -> Generator[
    scales._Scale, None, None]:
    for current_scale in _generate_all_scales():
        current_scale_semitones = get_semitones_from_mingus_scale(current_scale)
        if current_scale_semitones == scale_interval_semitones:
            yield current_scale


@beartype
def mingus_iterate_scales():
    for MingusScaleSubclass in mingus_core.scales._Scale.__subclasses__():
        if MingusScaleSubclass is mingus_core.scales.Diatonic:
            continue

        try:
            mingus_scale_instance = MingusScaleSubclass(txnote_khe_wrap.note_C4.khe_name[0])
        except:
            mingus_scale_instance = MingusScaleSubclass(txnote_khe_wrap.note_C4.khe_name)
        yield mingus_scale_instance


def mingus_scale_to_container(mingus_scale: mingus_core.scales._Scale, octave: int) -> NoteContainer:
    mingus_notes = list(mingus_scale_to_notes(mingus_scale, octave=octave))
    for mingus_note in mingus_notes:
        assert isinstance(mingus_note, Note)
    container = NoteContainer(mingus_notes)
    return container


def mingus_scale_build_from_name(scale_name: str, base_note: str, octaves: int):
    if scale_name == txpymusiclib.scales_package.txscales_examples.phrygian.name:
        return mingus_core.scales.Phrygian(note=base_note, octaves=octaves)
    if scale_name == txpymusiclib.scales_package.txscales_examples.major.name:
        return mingus_core.scales.Major(note=base_note, octaves=octaves)
    raise NotImplementedError()
