import time

from beartype import beartype
from musthe import Scale as MustheScale

from txpymusiclib.play.play_txnote_in_synthetizer import play_sequence_notes
from txpymusiclib.scales_package.scale_musthe import musthescale_notes
from txpymusiclib.scales_package.txnotecontainer import TxNoteContainer


@beartype
def play_scale_from_musthescale(current_scale: MustheScale):
    notes_in_scale, description = musthescale_notes(current_scale)
    nc = TxNoteContainer(notes_in_scale)
    print(description)
    play_sequence_notes(nc, 0.5)
    time.sleep(1)