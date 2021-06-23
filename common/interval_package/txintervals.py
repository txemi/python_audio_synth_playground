from common.note_package.note_names_and_freq_static import note_C4_name, note_C5, note_E4_name, note_c4_name


class TxIntervals:
    @staticmethod
    def interval_factor(half_steps):
        return 2 ** (half_steps / 12)

    fifth_1 = 3 / 2

    @classmethod
    def get_fifth_factor_2(cls):
        fifth_2 = cls.interval_factor(7.0)
        return fifth_2


def freq_mult(freq, mult):
    return float(TxIntervals.interval_factor(mult) * freq)


def freqs_mult(freq, mults):
    for mult in mults:
        yield freq_mult(freq, mult)


def freqs_mult_accumulate(freq, mults):
    accumulated = 0
    for mult in mults:
        added = mult + accumulated
        yield freq_mult(freq, added)
        accumulated = added


interval_example_perfect_consonant_octave = (note_C4_name, note_C5)  # Perfect Consonance (Octave)
interval_example_imperfect_consonance_major_third = (note_C4_name, note_E4_name)  # Imperfect Consonance (Major Thirds)
interval_example_dissonance_minor_seconds = (note_C4_name, note_c4_name)  # Dissonance (Minor Seconds)