from txpymusiclib.note_package import txnote_khe_wrap


class TxChord:
    class Type:
        major = 0, 4, 7
        minor = 0, 3, 7
        dim = 0, 3, 6
        aug = 0, 4, 8
        all = (major, minor, dim, aug)

    c3_major_chord_names = [txnote_khe_wrap.note_C3.khe_name, txnote_khe_wrap.note_E3.khe_name,
                            txnote_khe_wrap.note_G3.khe_name]

    C4_major_chord_freqs = [txnote_khe_wrap.note_C4.freq, txnote_khe_wrap.note_E4.freq,
                            txnote_khe_wrap.note_G4.freq]
    otro_chord_mingus = ["D-4", "F#-4", "A-4"]  # no pilla el #
