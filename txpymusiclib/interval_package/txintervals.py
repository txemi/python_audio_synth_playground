from txpymusiclib.note_package import note_names_and_freq_static


class TxIntervals:
    # TODO: this class is not needed
    @staticmethod
    def interval_factor(half_steps):
        return 2 ** (half_steps / 12)

    fifth_factor_rational = 3 / 2

    @classmethod
    def get_fifth_factor_non_rational(cls):
        fifth_2 = cls.interval_factor(7.0)
        return fifth_2


def freq_mult(freq, mult):
    return float(TxIntervals.interval_factor(mult) * freq)


def freqs_mult(freq, mults):
    for mult in mults:
        yield freq_mult(freq, mult)


def freqs_mult_accumulate(freq, mults):
    accumulated = 0
    for mult in (0,) + mults:
        added = mult + accumulated
        yield freq_mult(freq, added)
        accumulated = added


class TxInterval:
    def __init__(self, khe_note_from: str, khe_note_to: str):
        self.start = khe_note_from
        self.end = khe_note_to


interval_example_perfect_consonant_octave = TxInterval(note_names_and_freq_static.note_C4,
                                                       note_names_and_freq_static.note_C5)  # Perfect Consonance (Octave)
interval_example_imperfect_consonance_major_third = TxInterval(note_names_and_freq_static.note_C4,
                                                               note_names_and_freq_static.note_E4)  # Imperfect Consonance (Major Thirds)
interval_example_dissonance_minor_seconds = TxInterval(note_names_and_freq_static.note_C4,
                                                       note_names_and_freq_static.note_c4)  # Dissonance (Minor Seconds)
