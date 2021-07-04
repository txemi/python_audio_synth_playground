from beartype import beartype

from txpymusiclib.interval_package import txintervals
from txpymusiclib.note_package.txnote_khe_wrap import TxNoteKheWrap
from txpymusiclib.play.play_floatfreqs_in_syntetizer import play_sequence_freqs
from txpymusiclib.play.play_mode import ScalePlayMode
from txpymusiclib.scales_package.txnotecontainer import TxNoteContainer
from txpymusiclib.scales_package.txscales import TxScaleSt


@beartype
def play_sequence_txnotes(tx_note_container: TxNoteContainer, duration_secs: float = 1.0):
    note_freqs = [note.get_freq() for note in tx_note_container.get_txnotes()]
    play_sequence_freqs(note_freqs, duration_secs)


@beartype
def play_scale_from_freq(base_freq: float, scale_semitone_intervals: TxScaleSt, duration_seconds: float,
                         mode: ScalePlayMode):
    note_freqs = list(txintervals.get_note_freqs_for_intervals(base_freq=base_freq,
                                                               interval_half_steps_count_list=scale_semitone_intervals.semitones,
                                                               mode=mode))
    if mode is ScalePlayMode.octave_and_return:
        tail = list(reversed(note_freqs))[1:]
    else:
        tail = []
    play_sequence_freqs(note_freqs + tail, duration_seconds)


@beartype
def play_txscale(base_note: TxNoteKheWrap, txscale: TxScaleSt, mode: ScalePlayMode, duration_secs: float = 0.1):
    play_scale_from_freq(base_freq=base_note.freq, scale_semitone_intervals=txscale, duration_seconds=duration_secs,
                         mode=mode)
