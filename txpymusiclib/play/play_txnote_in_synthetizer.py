from beartype import beartype

from txpymusiclib.interval_package import txintervals
from txpymusiclib.note_package import note_names_and_freq_static
from txpymusiclib.play.play_floatfreqs_in_syntetizer import play_sequence_freqs
from txpymusiclib.scales_package.txnotecontainer import TxNoteContainer
from txpymusiclib.scales_package.txscales import TxScaleSt


@beartype
def play_sequence_txnotes(notes: TxNoteContainer, duration_secs: float = 1.0):
    freqs = [note.get_freq() for note in notes.get_txnotes()]
    play_sequence_freqs(freqs, duration_secs)


@beartype
def play_scale_from_freq(freq: float, scale_semitone_intervals: TxScaleSt, duration_secons: float):
    freqs = list(txintervals.freqs_mult_accumulate(freq, scale_semitone_intervals.semitones))
    tail = list(reversed(freqs))[1:]
    play_sequence_freqs(freqs + tail, duration_secons)


@beartype
def play_txscale(txscale: TxScaleSt):
    base = note_names_and_freq_static.note_C4
    play_scale_from_freq(base.freq, txscale, 1.0)
