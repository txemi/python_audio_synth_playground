from txpymusiclib.note_package import txnote


class TxChord:
    class Type:
        major = 0, 4, 7
        minor = 0, 3, 7
        dim = 0, 3, 6
        aug = 0, 4, 8
        all = (major, minor, dim, aug)

    c3_major_chord_names = [txnote.note_C3.name, txnote.note_E3.name,
                            txnote.note_G3.name]

    C4_major_chord_freqs = [txnote.note_C4.freq, txnote.note_E4.freq,
                            txnote.note_G4.freq]
    otro_chord_mingus = ["D-4", "F#-4", "A-4"]  # no pilla el #
