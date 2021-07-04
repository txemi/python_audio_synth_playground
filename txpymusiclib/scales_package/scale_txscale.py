from beartype import beartype

from txpymusiclib.play.play_mode import ScalePlayMode
from txpymusiclib.play.play_txnote_in_synthetizer import play_txscale
from txpymusiclib.scales_package.txscales_examples import find_scale_by_name_unique


class TxTxScaleWrapper:
    wrapped_lib_name = "txscale"

    @beartype
    def __init__(self, scale_name: str, base_note, octaves: int):
        self.__txscale = find_scale_by_name_unique(scale_name)
        self.__base_note = base_note

    @beartype
    def play(self, scale_play_mode: ScalePlayMode, duration_secs_per_note: float):
        play_txscale(self.__base_note, self.__txscale, duration_secs=duration_secs_per_note,
                     mode=scale_play_mode)
