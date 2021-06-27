import musthe
import pytheory
from mingus import core as mingus_core

from txpymusiclib.note_package import note_names_and_freq_static
from txpymusiclib.scales_package.scale_mingus import get_semitones_from_mingus_scale
from assertpy import assert_that

class ScaleMergedFromLibs:
    def __init__(self, name):
        self.name = name
        self.pytheory = None
        self.musthe = None
        self.mingus = None

    def get_semitones(self):
        if self.mingus is not None:
            assert_that(self.mingus).is_length(1)
            return get_semitones_from_mingus_scale(self.mingus[0])
        raise NotImplementedError()


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
    to_find = to_find.replace(" ", "_")
    return to_find


def musthe_get_scales_key_hashed():
    musthe_scales = musthe.Scale.scales
    musthe_scales_translated_key = {}
    for a, b in musthe_scales.items():
        musthe_scales_translated_key[hash_scale_name(a)] = b
    return musthe_scales_translated_key


class ScaleFinder:
    pytheory_c4_scales = pytheory.TonedScale(tonic=note_names_and_freq_static.note_C4.name)._scales

    def __init__(self):
        self.map = {}

    def find(self, scale_to_find_name: str):
        scale_to_find_name = hash_scale_name(scale_to_find_name)
        if scale_to_find_name in self.map:
            return self.map[scale_to_find_name]

        scale_merged = ScaleMergedFromLibs(scale_to_find_name)

        try:
            scale_merged.pytheory = self.pytheory_c4_scales[scale_to_find_name]
        except:
            pass

        musthe_scales = musthe_get_scales_key_hashed()
        if scale_to_find_name in musthe_scales:
            scale_merged.musthe = musthe_scales[scale_to_find_name]
        else:
            scale_merged.musthe = None

        found_asdfadsf = []
        for mingus_current_scale in mingus_iterate_scales():
            current_name = hash_scale_name(mingus_scale_name(mingus_current_scale))
            if scale_to_find_name == current_name:
                found_asdfadsf.append(mingus_current_scale)
        scale_merged.mingus = found_asdfadsf

        self.map[scale_to_find_name] = scale_merged
        return scale_merged


def scale_get_from_all_libs() -> ScaleFinder:
    finder = ScaleFinder()
    for current_pytheory in ScaleFinder.pytheory_c4_scales.items():
        name = current_pytheory[0]
        pyt_scale = current_pytheory[1]
        finder.find(name)

    for current_musthe in musthe.Scale.scales:
        finder.find(current_musthe)

    for current_mingus in mingus_iterate_scales():
        cur_name = mingus_scale_name(current_mingus)
        finder.find(cur_name)

    return finder


def detect_same_scales():
    scales = scale_get_from_all_libs()
    for s1name in scales.map:
        for s2name in scales.map:
            if s1name is s2name:
                continue
            if s1name == s2name:
                continue
            s1 = scales.map[s1name]
            s2 = scales.map[s2name]
            st1 = s1.get_semitones()
            st2 = s2.get_semitones()
            raise NotImplementedError()
