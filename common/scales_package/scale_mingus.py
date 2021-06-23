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
        if current_scale.name == scale_name:
            return current_scale


def get_semitones_from_mingus_scale(mingus_scale):
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
            for aaaaa in note_str[1:]:
                if aaaaa == 'b':
                    mingus_note.diminish()
                elif aaaaa == '#':
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


def find_scale_by_semitones(scale_interval_semitones):
    for current_scale in generate_all_scales():
        current_scale_semitones = list(get_semitones_from_mingus_scale(current_scale))
        if current_scale_semitones == list(scale_interval_semitones):
            yield current_scale
