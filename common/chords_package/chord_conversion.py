from beartype import beartype
from mingus.core import chords as chords


@beartype
def mingusChord2Notes(current_chord_name: str):
    mingus_chord = chords.from_shorthand(current_chord_name)
    d = chords.determine(mingus_chord)
    print(current_chord_name + " " + str(mingus_chord) + " " + str(d))
    # fails fluidsynth.play_Note(mingus_chord[0] + '-4')
    chord_notes = [x + "4" for x in mingus_chord]
    return chord_notes