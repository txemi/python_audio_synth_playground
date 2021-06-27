import musthe
from mingus import core as mingus_core

from learn_scales.scales import pytheory_c4
from txpymusiclib.note_package import note_names_and_freq_static


class ScaleMergedFromLibs:
    def __init__(self, name):
        self.name = name
        self.pytheory = None
        self.musthe = None
        self.mingus = None


def mingus_iterate_scales():
    for bbb in mingus_core.scales._Scale.__subclasses__():
        if bbb is mingus_core.scales.Diatonic:
            continue

        try:
            uuu = bbb(note_names_and_freq_static.note_C4.name)
        except:
            uuu = bbb(note_names_and_freq_static.note_C4.name[0])
        yield uuu


def mingus_scale_name(uuu):
    try:
        current_name = uuu.name.split()[1]
    except:
        raise
    return current_name


class ScaleFinder:
    pytheory_c4_scales = pytheory_c4._scales

    def __init__(self):
        self.map = {}
        pass

    def find(self, to_find: str):
        if to_find in self.map:
            return self.map[to_find]

        scale_merted = ScaleMergedFromLibs(to_find)

        try:
            scale_merted.pytheory = self.pytheory_c4_scales[to_find]
        except:
            pass

        musthe_scales = musthe.Scale.scales
        if to_find in musthe_scales:
            scale_merted.musthe = musthe_scales[to_find]
        else:
            scale_merted.musthe = None

        found_asdfadsf = []
        for uuu in mingus_iterate_scales():

            current_name = mingus_scale_name(uuu)
            if to_find == current_name:
                found_asdfadsf.append(uuu)
        scale_merted.mingus = found_asdfadsf
        self.map[to_find] = scale_merted
        return scale_merted


def scale_get_from_all_libs() -> ScaleFinder:
    finder = ScaleFinder()
    for a in ScaleFinder.pytheory_c4_scales.items():
        name = a[0]
        pyt_scale = a[1]
        finder.find(name)

    for aaa in musthe.Scale.scales:
        finder.find(aaa)

    for bbb in mingus_iterate_scales():
        cur_name = mingus_scale_name(bbb)
        finder.find(cur_name)
    return finder
