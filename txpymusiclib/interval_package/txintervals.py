from beartype import beartype

from txpymusiclib.note_package import txnote_khe_wrap


class TxIntervals:
    # TODO: this class is not needed, this methods do not need a class
    @staticmethod
    @beartype
    def interval_factor(half_steps: int) -> float:
        return 2 ** (half_steps / 12)

    fifth_factor_rational = 3 / 2

    @classmethod
    @beartype
    def get_fifth_factor_non_rational(cls):
        fifth_2 = cls.interval_factor(7.0)
        return fifth_2


@beartype
def do_interval_jump_to_freq(freq, interval_half_steps_count: int) -> float:
    return float(TxIntervals.interval_factor(interval_half_steps_count) * freq)


@beartype
def do_interval_jumps_to_freq(freq, half_steps_count_list: list[int]):
    """ gets freqs for chord, etc"""
    for half_steps_count in half_steps_count_list:
        yield do_interval_jump_to_freq(freq, half_steps_count)


@beartype
def get_note_freqs_for_intervals(base_freq: float, interval_half_steps_count_list: list[int]):
    accumulated = 0
    for current_half_step_count in (0,) + interval_half_steps_count_list:
        added = current_half_step_count + accumulated
        yield do_interval_jump_to_freq(base_freq, added)
        accumulated = added


class TxKheIntervalExample:
    @beartype
    def __init__(self, khe_note_from: txnote_khe_wrap.TxNoteKheWrap, khe_note_to: txnote_khe_wrap.TxNoteKheWrap, description: str,
                 sort_description: str):
        self.start = khe_note_from
        self.end = khe_note_to
        self.description = description
        self.sort_description = sort_description


interval_example_perfect_consonant_octave = TxKheIntervalExample(txnote_khe_wrap.note_C4,
                                                                 txnote_khe_wrap.note_C5, "Perfect Consonance (Octave)", "Octave")
interval_example_imperfect_consonance_major_third = TxKheIntervalExample(txnote_khe_wrap.note_C4,
                                                                         txnote_khe_wrap.note_E4,
                                                                      "Imperfect Consonance (Major Thirds)",
                                                                      'Major Thirds')
interval_example_dissonance_minor_seconds = TxKheIntervalExample(txnote_khe_wrap.note_C4,
                                                                 txnote_khe_wrap.note_c4, "Dissonance (Minor Seconds)",
                                                              'Minor Seconds')
