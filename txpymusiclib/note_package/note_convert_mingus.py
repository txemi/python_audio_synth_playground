from beartype import beartype
from mingus.containers import Note as MingusNote

from txpymusiclib.note_package.convert_khe_pytheory import khe_2_pytheory


@beartype
def note_name_2_mingus_note_name(note: str) -> str:
    return note[:1] + "-" + note[-1:]


@beartype
def note_names_2_mingus_note_names(chord_notes):
    for note in chord_notes:
        yield note_name_2_mingus_note_name(note)


@beartype
def note_name_str_2_mingus_note(notestr: str) -> MingusNote:
    digits = "".join([x for x in notestr if x.isdigit()])
    non_digits = "".join([x for x in notestr if not x.isdigit()])
    mingus_note = MingusNote(name=khe_2_pytheory(non_digits), octave=int(digits))
    return mingus_note


@beartype
def note_name_str_2_mingus_note_int(old_key: str) -> int:
    mingus_note = note_name_str_2_mingus_note(old_key)
    mingus_note_int = int(mingus_note)
    return mingus_note_int
