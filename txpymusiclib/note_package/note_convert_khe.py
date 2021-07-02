from beartype import beartype


@beartype
def note_khe_name_to_sci(note: str) -> str:
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
def note_sci_to_khe(note: str) -> str:
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


