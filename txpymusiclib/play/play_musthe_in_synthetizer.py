import time

from beartype import beartype
from musthe import Scale as MustheScale

from txpymusiclib.play.play_txnote_in_synthetizer import play_sequence_txnotes
from txpymusiclib.scales_package.scale_musthe import musthescale_notes
from txpymusiclib.scales_package.txnotecontainer import TxNoteContainer


@beartype
def play_scale_from_musthescale(current_scale: MustheScale):
    notes_in_scale, description = musthescale_notes(current_scale)
    nc = TxNoteContainer().build_from_mingus_notes_str(notes_in_scale)
    play_sequence_txnotes(tx_note_container=nc, duration_secs=0.5)
    time.sleep(1)
