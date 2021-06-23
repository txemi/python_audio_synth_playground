from beartype import beartype

from mingus.containers import Note as MingusNote


# Python to convert a string note (eg. "A4") to a frequency (eg. 440).
# Inspired by https://gist.github.com/stuartmemo/3766449


@beartype
def katieshiqihe2pytheory(note_name: str):
    """ katie code use lowercase for black keys """
    return note_name.replace("a", "A#").replace("c", "C#").replace("d", "D#").replace("f", "F#").replace("g", "G#")


def note2mingus(note):
    return note[:1] + "-" + note[-1:]


def notes2mingus(chord_notes):
    for note in chord_notes:
        yield note2mingus(note)


@beartype
def notestr2mingus2(notestr: str):
    digits = "".join([x for x in notestr if x.isdigit()])
    nondigits = "".join([x for x in notestr if not x.isdigit()])
    mingusNote = MingusNote(name=katieshiqihe2pytheory(nondigits), octave=int(digits))
    return mingusNote
@beartype
def notestr2mingus_int(old_key):
    mingus_note = notestr2mingus2(old_key)
    mingus_note_int = int(mingus_note)
    return mingus_note_int
@beartype
def note_khe_to_sci(note: str):
    if len(note) != 2:
        raise ValueError()
    if not note[1].isdigit():
        raise ValueError()
    if not note[0].isascii():
        raise ValueError()

    letter = note[0]
    if letter.islower():
        return letter.upper() + '#' + note[1]
    return note


@beartype
def note_sci_to_khe(note: str):
    if len(note) < 2 or len(note) > 3:
        raise ValueError()
    if not note[-1].isdigit():
        raise ValueError()
    if not note[0].isascii():
        raise ValueError()
    if len(note) == 3 and note[1] != "#":
        raise ValueError()

    middle = note[1]
    if middle == "#":
        return note[0].lower() + note[2]
    return note


