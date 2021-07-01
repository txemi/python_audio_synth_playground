import pytheory
from beartype import beartype

from txpymusiclib.note_package.note_convert_mingus import note_name_str_2_mingus_note
from txpymusiclib.scales_package.scale_mingus import _get_semitones_from_mingus_notes_2
from txpymusiclib.scales_package.txnotecontainer import TxNoteContainer
from txpymusiclib.scales_package.txscales import TxScaleSt


@beartype
def scale_pytheory2txnote(pyt: pytheory.Scale) -> TxNoteContainer:
    txnotes = TxNoteContainer()
    for tone in pyt.tones:
        mingus_note = note_name_str_2_mingus_note(tone.full_name)
        txnotes.append(mingus_note)
    return txnotes


@beartype
def scale_pytheory2txscale(pyt: pytheory.Scale) -> TxScaleSt:
    semitones = list(_get_semitones_from_mingus_notes_2(scale_pytheory2txnote(pyt).notes))
    return TxScaleSt(semitones)