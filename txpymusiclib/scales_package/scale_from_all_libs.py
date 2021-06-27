import musthe
import pytheory
from assertpy import assert_that
from beartype import beartype
from mingus import core as mingus_core
from musthe import Scale as MustheScale

from txpymusiclib.note_package import note_names_and_freq_static
from txpymusiclib.note_package.note_convert_mingus import note_name_str_2_mingus_note
from txpymusiclib.scales_package.scale_mingus import get_semitones_from_mingus_scale, _get_semitones_from_mingus_notes_2
from txpymusiclib.scales_package.scale_musthe import musthescale_semitones
from txpymusiclib.scales_package.txnotecontainer import TxNoteContainer
from txpymusiclib.scales_package.txscales import TxScaleSt


@beartype
def scale_pytheory2mingus(pyt: pytheory.Scale):
    txnotes = TxNoteContainer()
    txnotes.notes = []
    for tone in pyt.tones:
        mingus_note = note_name_str_2_mingus_note(tone.full_name)
        txnotes.notes.append(mingus_note)

    semitones = list(_get_semitones_from_mingus_notes_2(txnotes.notes))
    return TxScaleSt(semitones)


class ScaleMergedFromLibs:
    def __init__(self, name):
        self.name = name
        self.pytheory = None
        self.musthe = None
        self.mingus = None

    def get_semitones(self):
        self.check_integrity()
        for aa1 in self._get_from_pytheory, self._get_from_musthe, self._get_from_mingus:
            aa = aa1()
            if aa is not None:
                return aa

        raise NotImplementedError()

    def _get_from_mingus(self):
        if self.mingus is not None and len(self.mingus) > 0:
            assert_that(self.mingus).is_length(1)
            return get_semitones_from_mingus_scale(self.mingus[0])
        return None

    def _get_from_musthe(self):
        if self.musthe is not None:
            musthe_semitones = musthescale_semitones(self.musthe)
            musthe_semitones.name = self.name
            return musthe_semitones
        return None

    def _get_from_pytheory(self):
        if self.pytheory is not None:
            assert isinstance(self.pytheory, pytheory.Scale)
            return scale_pytheory2mingus(self.pytheory)
        return None

    def check_integrity(self):
        last_semitones = None
        for current_semitones_func in self._get_from_pytheory, self._get_from_musthe, self._get_from_mingus:
            current_semitones = current_semitones_func()
            if last_semitones is not None:
                if current_semitones is not None:
                    if current_semitones != last_semitones:
                        raise NotImplementedError()
            if current_semitones is not None:
                last_semitones = current_semitones


def mingus_iterate_scales():
    for MingusScaleSubclass in mingus_core.scales._Scale.__subclasses__():
        if MingusScaleSubclass is mingus_core.scales.Diatonic:
            continue

        try:
            mingus_scale_instance = MingusScaleSubclass(note_names_and_freq_static.note_C4.name[0])
        except:
            mingus_scale_instance = MingusScaleSubclass(note_names_and_freq_static.note_C4.name)
        yield mingus_scale_instance


def mingus_scale_name(scale1):
    try:
        current_name = '_'.join(scale1.name.split()[1:])
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
        musthe_scales_translated_key[hash_scale_name(a)] = MustheScale(name=a,
                                                                       root=note_names_and_freq_static.note_C4.name)
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
                assert_that(len(found_asdfadsf)).is_less_than(2)

        assert_that(len(found_asdfadsf)).is_less_than(2)
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
            if st1 != st2:
                continue
            s2.get_semitones()
            raise NotImplementedError()
