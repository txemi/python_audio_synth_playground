from beartype import beartype
from mingus.containers import NoteContainer as MingusNoteContainer


@beartype
def mingus_chord_to_note_container(current_chord_name: str) -> MingusNoteContainer:
    # , print_chords: bool
    mingus_note_container = MingusNoteContainer().from_chord_shorthand(current_chord_name)
    determined = mingus_note_container.determine()
    print(current_chord_name + " " + str(mingus_note_container) + " " + str(determined))
    # failed_libs fluidsynth.play_Note(mingus_chord[0] + '-4')
    return mingus_note_container


@beartype
def mingus_chords_to_note_containers(current_chord_names: list):
    for aaa in current_chord_names:
        yield mingus_chord_to_note_container(aaa)


@beartype
def mingus_progression_to_note_container(progression_name: str) -> MingusNoteContainer:
    mingus_note_container = MingusNoteContainer().from_progression_shorthand(progression_name)
    return mingus_note_container
