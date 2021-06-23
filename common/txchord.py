from beartype import beartype
from mingus.core import chords as chords

from common.tonepackage.note_names_and_freq_static import note_C4_freq, note_E4_freq, note_G4_freq


class TxChord:
    class Type:
        major = 0, 4, 7
        minor = 0, 3, 7
        dim = 0, 3, 6
        aug = 0, 4, 8
        all = (major, minor, dim, aug)

    c3_major_chord_names = ["C3", "E3", "G3"]

    C4_major_chord_freqs = [note_C4_freq, note_E4_freq, note_G4_freq]
    otro_chord_mingus = ["D-4", "F#-4", "A-4"]  # no pilla el #


class TxChords:
    # la menor, do mayor , mi mayor, fa mayor
    NiceChordSeqExample = ('Am', 'CM', 'EM', 'FM')
    LordOfRings = ('CM', 'Em', 'FM', 'CM', 'FM', 'GM', 'CM', 'GM')


@beartype
def mingusChord2Notes(current_chord_name: str):
    mingus_chord = chords.from_shorthand(current_chord_name)
    d = chords.determine(mingus_chord)
    print(current_chord_name + " " + str(mingus_chord) + " " + str(d))
    # fails fluidsynth.play_Note(mingus_chord[0] + '-4')
    chord_notes = [x + "4" for x in mingus_chord]
    return chord_notes
