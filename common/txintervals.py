class TxIntervals:
    @staticmethod
    def interval_factor(half_steps):
        return 2 ** (half_steps / 12)

    fifth_1 = 3 / 2

    @classmethod
    def get_fifth_factor_2(cls):
        fifth_2 = cls.interval_factor(7.0)
        return fifth_2


class TxChord:
    class Type:
        major = 1, 4, 7
        minor = 1, 3, 7
        dim = 1, 3, 6
        aug = 1, 4, 8
        all = (major, minor, dim, aug)

    @classmethod
    def freqs_mult(cls, freq, mults):
        return [float(freq) * mults[0],
                float(TxIntervals.interval_factor(mults[1]) * freq),
                float(TxIntervals.interval_factor(mults[2]) * freq)]

    c3_major_chord_names = ["C3", "E3", "G3"]
    # C4 E4 G4
    C4_major_chord_freqs = [261.626, 329.628, 391.996]
