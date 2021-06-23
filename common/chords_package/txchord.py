from common.note_package.note_names_and_freq_static import note_C4_freq, note_E4_freq, note_G4_freq


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


