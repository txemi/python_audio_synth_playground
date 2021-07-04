import time
from typing import Optional

import musthe
from beartype import beartype
from musthe import Scale as MustheScale

from txpymusiclib.note_package.txnote_khe_wrap import TxNoteKheWrap
from txpymusiclib.play.play_mode import ScalePlayMode
from txpymusiclib.play.play_txnote_in_synthetizer import play_txscale
from txpymusiclib.scales_package.scale_musthe import musthescale_semitones
from txpymusiclib.scales_package.txnotecontainer import TxNoteContainer
from txpymusiclib.scales_package.txscales import TxScaleSt


class TxMustheScaleWrapper:
    wrapped_lib_name = "musthe"

    @beartype
    def __init__(self, scale_name: str, base_note: Optional[TxNoteKheWrap], octaves: int = 1,
                 musthe_scale: MustheScale = None):
        if musthe_scale is not None:
            self.__musthe_scale = musthe_scale
        else:
            self.__musthe_scale: MustheScale = musthe.Scale(musthe.Note(base_note.khe_name),
                                                            scale_name)
        self.__base_note = base_note

    @beartype
    def play(self, scale_play_mode: ScalePlayMode, duration_secs_per_note: float):
        notes_in_scale = self.get_notes_in_scale()
        nc = TxNoteContainer().build_from_mingus_notes_str(notes_in_scale)
        play_txscale(self.__base_note, self.get_diffs(), duration_secs=duration_secs_per_note,
                     mode=scale_play_mode)
        time.sleep(1)

    @beartype
    def get_diffs(self) -> TxScaleSt:
        semitone_diffs = musthescale_semitones(self.__musthe_scale)
        return semitone_diffs

    @beartype
    def get_notes_in_scale(self):
        notes_in_scale = [self.__musthe_scale[i].scientific_notation() for i in range(len(self.__musthe_scale))]
        return notes_in_scale

    @beartype
    def get_description(self):
        description = str(self.__musthe_scale) + ":" + str(self.get_diffs().semitones) + ":" + str(
            self.get_notes_in_scale())
        return description
