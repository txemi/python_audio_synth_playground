import time

import musthe
from beartype import beartype
from musthe import Scale as MustheScale

from txpymusiclib.note_package.txnote_khe_wrap import TxNoteKheWrap
from txpymusiclib.play.play_txnote_in_synthetizer import play_sequence_txnotes
from txpymusiclib.scales_package.scale_musthe import musthescale_semitones
from txpymusiclib.scales_package.txnotecontainer import TxNoteContainer


class TxMustheScaleWrapper:
    wrapped_lib_name = "musthe"

    @beartype
    def __init__(self, scale_name: str, base_note: TxNoteKheWrap, octaves: int):
        self.__musthe_scale: MustheScale = musthe.Scale(musthe.Note(base_note.khe_name),
                                                        scale_name)

    @beartype
    def play(self, scale_play_mode, duration_secs_per_note: float):
        notes_in_scale = self.get_notes_in_scale()
        nc = TxNoteContainer().build_from_mingus_notes_str(notes_in_scale)
        play_sequence_txnotes(tx_note_container=nc, duration_secs=duration_secs_per_note)
        time.sleep(1)

    def get_diffs(self):
        semitone_diffs = musthescale_semitones(self.__musthe_scale)
        return semitone_diffs

    def get_notes_in_scale(self):
        notes_in_scale = [self.__musthe_scale[i].scientific_notation() for i in range(len(self.__musthe_scale))]
        return notes_in_scale

    def get_description(self):
        description = str(self.__musthe_scale) + ":" + str(self.get_diffs().semitones) + ":" + str(
            self.get_notes_in_scale())
        return description
