from txpymusiclib.play.play_mingus_in_synthesizer import mingus_play
from txpymusiclib.play.play_mode import ScalePlayMode
from txpymusiclib.scales_package.scale_mingus import mingus_scale_build_from_name


class TxMingusScaleWrapper:
    wrapped_lib_name = "mingus"

    def __init__(self, scale_name: str, base_note, octaves: int):
        self.__scale_name = scale_name
        self.__base_note = base_note
        self.__mingus_scale = mingus_scale_build_from_name(self.__scale_name, base_note=self.__base_note.khe_name[0],
                                                           octaves=octaves)

    def play(self, scale_play_mode: ScalePlayMode, duration_secs_per_note: float):
        mingus_play(self.__mingus_scale, duration_secs=duration_secs_per_note, octave=self.__base_note.get_octave(),
                    mode=scale_play_mode)

    pass