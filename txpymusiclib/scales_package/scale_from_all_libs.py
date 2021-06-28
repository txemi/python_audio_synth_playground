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


def mergemingus(m1, m2):
    if m1 is None or len(m1) == 0:
        return (True, m2)
    if m2 is None:
        return (True, m1)
    if m1 != m2:
        return (False, None)
    return (True, m1)


def mergemusthe(s1, s2):
    if s1 is None:
        return (True, s2)
    if s2 is None:
        return (True, s1)
    if s1.root != s2.root:
        return (False, None)
    if s1.notes != s2.notes:
        return (False, None)
    return (True, s1)


def pytheory_merge(s1, s2):
    if s1 == s2:
        return (True, s1)
    if s1.tones == s2.tones:
        return (True, s1)
    raise NotImplementedError()


class ScaleMergedFromLibs:
    def __init__(self, name: str = None):
        self.names = set()
        if name is not None:
            self.names.add(name)
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
            musthe_semitones.name = list(self.names)[0]
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
            # FIXME: disabled due to ionian not working
            if current_semitones_func is self._get_from_pytheory or 'pytheory' in str(current_semitones_func):
                continue
            current_semitones = current_semitones_func()
            if last_semitones is not None:
                if current_semitones is not None:
                    if current_semitones != last_semitones:
                        uuuu = current_semitones_func()
                        u3 = self._get_from_musthe()
                        u4 = self._get_from_mingus()
                        u5 = self._get_from_pytheory()
                        raise NotImplementedError()
            if current_semitones is not None:
                last_semitones = current_semitones

    def __repr__(self):
        return "ScaleMergedFromLibs(" + ",".join(self.names) + ")"

    @beartype
    def tx_compare(self, s2):
        assert isinstance(s2, ScaleMergedFromLibs)
        s1 = self
        st1 = s1.get_semitones()
        st2 = s2.get_semitones()
        if st1 != st2:
            return

        newone = ScaleMergedFromLibs()
        newone.names.update(s1.names)
        newone.names.update(s2.names)

        mingusresult = mergemingus(s1.mingus, s2.mingus)
        if mingusresult[0] == False:
            return
        else:
            newone.mingus = mingusresult[1]

        musthe_merge_result = mergemusthe(s1.musthe, s2.musthe)
        if musthe_merge_result[0] == False:
            return
        else:
            newone.musthe = musthe_merge_result[1]

        pyt_result = pytheory_merge(s1.pytheory, s2.pytheory)
        if pyt_result[0] == False:
            return
        else:
            newone.pytheory = pyt_result[1]
        return newone


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
        if "ionian" in name.lower():
            # FIXME: ionian should not have # ??????
            pass
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
            merged = s1.tx_compare(s2)
            if merged is None:
                continue
            scales.map[s1name] = scales.map[s2name] = merged
    return scales
