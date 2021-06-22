from common.txintervals import TxIntervals


class TxChord:
    class Type:
        major = 0, 4, 7
        minor = 0, 3, 7
        dim = 0, 3, 6
        aug = 0, 4, 8
        all = (major, minor, dim, aug)

    @classmethod
    def freqs_mult(cls, freq, mults):
        for aa in mults:
            yield float(TxIntervals.interval_factor(aa) * freq)

    c3_major_chord_names = ["C3", "E3", "G3"]
    # C4 E4 G4
    C4_major_chord_freqs = [261.626, 329.628, 391.996]
    otro_chord_mingus = ["D-4", "F#-4", "A-4"]  # no pilla el #

    # la menor, do mayor , mi mayor, fa mayor
    NiceChordSeqExample = ('Am', 'CM', 'EM', 'FM')
