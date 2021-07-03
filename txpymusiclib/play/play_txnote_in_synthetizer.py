from beartype import beartype

from txpymusiclib.interval_package import txintervals
from txpymusiclib.note_package import txnote_khe_wrap
from txpymusiclib.play.play_floatfreqs_in_syntetizer import play_sequence_freqs
from txpymusiclib.scales_package.txnotecontainer import TxNoteContainer
from txpymusiclib.scales_package.txscales import TxScaleSt


@beartype
def play_sequence_txnotes(tx_note_container: TxNoteContainer, duration_secs: float = 1.0):
    note_freqs = [note.get_freq() for note in tx_note_container.get_txnotes()]
    play_sequence_freqs(note_freqs, duration_secs)


@beartype
def play_scale_from_freq(freq: float, scale_semitone_intervals: TxScaleSt, duration_secons: float):
    note_freqs = list(txintervals.get_note_freqs_for_intervals(freq, scale_semitone_intervals.semitones))
    tail = list(reversed(note_freqs))[1:]
    play_sequence_freqs(note_freqs + tail, duration_secons)


@beartype
def play_txscale(txscale: TxScaleSt, duration_secs: float = 0.1):
    base = txnote_khe_wrap.note_C4
    play_scale_from_freq(base.freq, txscale, duration_secs)
