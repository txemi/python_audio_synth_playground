import typing
from collections.abc import Iterable

from beartype import beartype
from mingus import containers
from mingus.containers import Note
from mingus.core import scales

from txpymusiclib.scales_package import musical_mode_examples
from txpymusiclib.scales_package.musical_mode_examples import TxMusicalMode


@beartype
def scale_to_mingus_notes(scale_notes: Iterable[str]):
    for note_str in scale_notes:
        yield containers.Note().from_shorthand(note_str)


@beartype
def scale_to_notenames(scale_notes: Iterable[str]):
    for mingus_note in scale_to_mingus_notes(scale_notes):
        yield mingus_note.name


@beartype
def generate_all_scales() -> typing.Generator[scales._Scale, None, None]:
    """
    """

    for key in scales.keys:
        for scale in scales._Scale.__subclasses__():
            if scale.type == "major":
                yield scale(key[0])

            elif scale.type == "minor":
                yield scale(scales.get_notes(key[1])[0])


@beartype
def find_scale_by_name(scale_name: str):
    for current_scale in generate_all_scales():
        if current_scale.name == scale_name:
            return current_scale


@beartype
def get_semitones_from_mingus_scale(mingus_scale: scales._Scale):
    ascending = mingus_scale.ascending()
    last = -1
    modifier = 0
    for note_str in ascending:
        if False:
            mingus_note = Note().from_shorthand(note_str)
        else:
            if len(note_str) < 1:
                raise NotImplementedError()

            mingus_note = Note().from_shorthand(note_str[:1])
            for note_decorator in note_str[1:]:
                if note_decorator == 'b':
                    mingus_note.diminish()
                elif note_decorator == '#':
                    mingus_note.augment()
                else:
                    raise NotImplementedError()
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
def get_semitones_from_mingus_scale_2(c_major_1):
    return TxMusicalMode(list(get_semitones_from_mingus_scale(c_major_1)))


@beartype
def find_scale_by_semitones(scale_interval_semitones: musical_mode_examples.TxMusicalMode):
    for current_scale in generate_all_scales():
        current_scale_semitones = get_semitones_from_mingus_scale_2(current_scale)
        if current_scale_semitones == scale_interval_semitones:
            yield current_scale
