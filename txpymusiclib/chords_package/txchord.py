from txpymusiclib.note_package import note_names_and_freq_static


class TxChord:
    class Type:
        major = 0, 4, 7
        minor = 0, 3, 7
        dim = 0, 3, 6
        aug = 0, 4, 8
        all = (major, minor, dim, aug)

    c3_major_chord_names = [note_names_and_freq_static.note_C3.name, note_names_and_freq_static.note_E3.name,
                            note_names_and_freq_static.note_G3.name]

    C4_major_chord_freqs = [note_names_and_freq_static.note_C4.freq, note_names_and_freq_static.note_E4.freq,
                            note_names_and_freq_static.note_G4.freq]
    otro_chord_mingus = ["D-4", "F#-4", "A-4"]  # no pilla el #
