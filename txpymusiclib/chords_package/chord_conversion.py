from beartype import beartype
from mingus.containers import NoteContainer as MingusNoteContainer


@beartype
def mingus_chord_to_notes(current_chord_name: str) -> MingusNoteContainer:
    nc = MingusNoteContainer().from_chord_shorthand(current_chord_name)
    determined = nc.determine()
    print(current_chord_name + " " + str(nc) + " " + str(determined))
    # failed_libs fluidsynth.play_Note(mingus_chord[0] + '-4')
    return nc


def mingus_progression_to_notes(aaa: str) -> MingusNoteContainer:
    nc = MingusNoteContainer().from_progression_shorthand(aaa)
    return nc
