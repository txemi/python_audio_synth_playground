import musthe
import pytheory
from mingus import core as mingus_core

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


def mingus_scale_name(scale1):
    try:
        current_name = scale1.name.split()[1]
    except:
        raise
    return current_name


def hash_scale_name(to_find):
    to_find = to_find.lower()
    to_find=to_find.replace(" ", "_")
    return to_find


class ScaleFinder:
    pytheory_c4_scales = pytheory.TonedScale(tonic=note_names_and_freq_static.note_C4.name)._scales

    def __init__(self):
        self.map = {}

    def find(self, to_find: str):
        to_find = hash_scale_name(to_find)
        if "harm" in to_find:
            print(1)
        if to_find in self.map:
            return self.map[to_find]

        scale_merged = ScaleMergedFromLibs(to_find)

        try:
            scale_merged.pytheory = self.pytheory_c4_scales[to_find]
        except:
            pass

        musthe_scales = musthe.Scale.scales
        newwww = {}
        for a, b in musthe_scales.items():
            newwww[hash_scale_name(a)] = b

        if to_find in newwww:
            scale_merged.musthe = musthe_scales[to_find]
        else:
            scale_merged.musthe = None

        found_asdfadsf = []
        for mingus_current_scale in mingus_iterate_scales():
            current_name = hash_scale_name(mingus_scale_name(mingus_current_scale))
            if to_find == current_name:
                found_asdfadsf.append(mingus_current_scale)
        scale_merged.mingus = found_asdfadsf

        self.map[to_find] = scale_merged
        return scale_merged


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
