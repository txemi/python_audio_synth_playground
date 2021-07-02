from beartype import beartype


@beartype
def khe_2_pytheory(note_name: str):
    """ katie code use lowercase for black keys """
    return note_name.replace("a", "A#").replace("c", "C#").replace("d", "D#").replace("f", "F#").replace("g", "G#")