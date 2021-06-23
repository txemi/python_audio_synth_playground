import typing

from mingus import containers
from mingus.containers import Note
from mingus.core import scales


def scale_to_mingus_notes(scale_notes: tuple[str]):
    for note_str in scale_notes:
        yield containers.Note().from_shorthand(note_str)


def scale_to_notenames(scale_notes: tuple[str]):
    for mingus_note in scale_to_mingus_notes(scale_notes):
        yield mingus_note.name


def generate_all_scales() -> typing.Generator[int, None, None]:
    """
    """

    for key in scales.keys:
        for scale in scales._Scale.__subclasses__():
            if scale.type == "major":
                yield scale(key[0])

            elif scale.type == "minor":
                yield scale(scales.get_notes(key[1])[0])


def find_scale_by_name(scale_name):
    for current_scale in generate_all_scales():
        scale_dir = dir(current_scale)
        if current_scale.name == scale_name:
            return current_scale


def get_semitones_from_mingus_scale(mingus_scale):
    ascending = mingus_scale.ascending()
    last = -1
    for note_str in ascending:
        uu = Note().from_shorthand(note_str)
        cur = int(uu)
        if last != -1:
            diff = cur - last
            yield diff
        last = cur