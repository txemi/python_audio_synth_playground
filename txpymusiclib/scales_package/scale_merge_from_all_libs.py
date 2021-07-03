from typing import Optional

import musthe
import pytheory
from assertpy import assert_that
from beartype import beartype
from mingus import core as mingus_core
from musthe import Scale as MustheScale

import txpymusiclib.play.play_musthe_in_synthetizer
from txpymusiclib.note_package import txnote_khe_wrap
from txpymusiclib.play.play_mingus_in_synthesizer import mingus_play
from txpymusiclib.play.play_txnote_in_synthetizer import play_txscale
from txpymusiclib.scales_package import txscales_examples
from txpymusiclib.scales_package.scale_mingus import get_semitones_from_mingus_scale, mingus_iterate_scales
from txpymusiclib.scales_package.scale_musthe import musthescale_semitones
from txpymusiclib.scales_package.scale_pytheory import scale_pytheory2txscale
from txpymusiclib.scales_package.txscales import TxScaleSt


@beartype
def merge_mingus(m1, m2):
    if m1 is None or len(m1) == 0:
        return (True, m2)
    if m2 is None:
        return (True, m1)
    if m1 != m2:
        return (False, None)
    return (True, m1)


@beartype
def merge_musthe(s1, s2):
    if s1 is None:
        return (True, s2)
    if s2 is None:
        return (True, s1)
    if s1.root != s2.root:
        return (False, None)
    if s1.notes != s2.notes:
        return (False, None)
    return (True, s1)


@beartype
def merge_pytheory(s1, s2):
    if s2 is None:
        return (True, s1)
    assert isinstance(s1, pytheory.Scale)
    if s1 == s2:
        return (True, s1)
    if s1.tones == s2.tones:
        return (True, s1)
    return (False, None)


def merge_txscale(s1, s2):
    if s2 is None:
        return (True, s1)
    if s1.semitones == s2.semitones:
        return (True, s1)
    raise NotImplementedError()


class ScaleMergedFromLibs:

    @beartype
    def __init__(self, name: str = None):
        self.names = set()
        if name is not None:
            self.names.add(name)
        self.pytheory: pytheory.Scale = None
        self.musthe = None
        self.__mingus: list[mingus_core.scales._Scale] = None
        self.txscale = None

    @property
    @beartype
    def mingus(self) -> list[mingus_core.scales._Scale]:
        return self.__mingus

    @mingus.setter
    @beartype
    def mingus(self, var: list[mingus_core.scales._Scale]):
        assert isinstance(var, list)
        self.__mingus = var

    @beartype
    def get_semitones(self) -> Optional[TxScaleSt]:
        self.check_integrity()
        # FIXME: disabled due to note numbering not working self._get_TxScaleSt_from_pytheory
        for semitone_builder in self._get_TxScaleSt_from_musthe, self._get_TxScaleSt_from_mingus, self._get_TxScaleSt_from_txscale:
            semitones = semitone_builder()
            if semitones is not None:
                return semitones

        raise NotImplementedError()

    @beartype
    def _get_TxScaleSt_from_mingus(self) -> Optional[TxScaleSt]:
        if self.mingus is not None and len(self.mingus) > 0:
            assert_that(self.mingus).is_length(1)
            return get_semitones_from_mingus_scale(self.mingus[0])
        return None

    @beartype
    def _get_TxScaleSt_from_musthe(self) -> Optional[TxScaleSt]:
        if self.musthe is not None:
            musthe_semitones = musthescale_semitones(self.musthe)
            musthe_semitones.khe_name = list(self.names)[0]
            return musthe_semitones
        return None

    @beartype
    def _get_TxScaleSt_from_pytheory(self) -> Optional[TxScaleSt]:
        if self.pytheory is not None:
            assert isinstance(self.pytheory, pytheory.Scale)
            return scale_pytheory2txscale(self.pytheory)
        return None

    @beartype
    def _get_TxScaleSt_from_txscale(self) -> Optional[TxScaleSt]:
        return self.txscale

    @beartype
    def check_integrity(self):
        last_semitones = None
        for current_semitones_func in self._get_TxScaleSt_from_pytheory, self._get_TxScaleSt_from_musthe, self._get_TxScaleSt_from_mingus:
            # FIXME: disabled due to ionian not working
            if current_semitones_func is self._get_TxScaleSt_from_pytheory or 'pytheory' in str(current_semitones_func):
                continue
            current_semitones = current_semitones_func()
            if last_semitones is not None:
                if current_semitones is not None:
                    if current_semitones != last_semitones:
                        uuuu = current_semitones_func()
                        u3 = self._get_TxScaleSt_from_musthe()
                        u4 = self._get_TxScaleSt_from_mingus()
                        u5 = self._get_TxScaleSt_from_pytheory()
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

        new_merged_scale = ScaleMergedFromLibs()
        new_merged_scale.names.update(s1.names)
        new_merged_scale.names.update(s2.names)

        mingus_result = merge_mingus(s1.mingus, s2.mingus)
        if mingus_result[0] == False:
            return
        else:
            new_merged_scale.mingus = mingus_result[1]

        musthe_merge_result = merge_musthe(s1.musthe, s2.musthe)
        if musthe_merge_result[0] == False:
            return
        else:
            new_merged_scale.musthe = musthe_merge_result[1]

        pyt_result = merge_pytheory(s1.pytheory, s2.pytheory)
        if pyt_result[0] == False:
            return
        else:
            new_merged_scale.pytheory = pyt_result[1]

        txscales_merged = merge_txscale(s1.txscale, s2.txscale)
        if txscales_merged[0] is False:
            return
        else:
            new_merged_scale.txscale = txscales_merged[1]

        return new_merged_scale

    def format(self):
        formatted = "-----------" + str(self.names) + "\n"
        if self.txscale is not None:
            formatted = formatted + " txscale:" + str(self.txscale.semitones) + "\n"
        if len(self.mingus) > 0:
            formatted = formatted + " mingus:" + str(self.mingus) + "\n"
        if self.musthe is not None:
            formatted = formatted + " musthe:" + str(self.musthe).replace("\n", "") + "\n"
        if self.pytheory is not None:
            formatted = formatted + " pytheory:" + str(self.pytheory).replace("\n", "") + "\n"
        return formatted

    def play(self):
        duration_secs=0.5
        if self.musthe is not None:
            txpymusiclib.play.play_musthe_in_synthetizer.play_scale_from_musthescale(self.musthe,duration_secs=duration_secs)
            return
        if self.mingus is not None and len(self.mingus) > 0:
            assert len(self.mingus) == 1
            try:
                # assert isinstance(self.mingus, mingus_core.scales._Scale)
                mingus_play(self.mingus[0],duration_secs=duration_secs)
            except:
                raise
            return
        if self.txscale is not None:
            play_txscale(self.txscale,duration_secs=duration_secs)
            return

        raise NotImplementedError()


@beartype
def mingus_scale_name(scale1):
    try:
        current_name = '_'.join(scale1.name.split()[1:])
    except:
        raise
    return current_name


@beartype
def hash_scale_name(to_find):
    to_find = to_find.lower()
    to_find = to_find.replace(" ", "_")
    return to_find


@beartype
def musthe_get_scales_key_hashed():
    musthe_scales = musthe.Scale.scales
    musthe_scales_translated_key = {}
    for a, b in musthe_scales.items():
        musthe_scales_translated_key[hash_scale_name(a)] = MustheScale(name=a,
                                                                       root=txnote_khe_wrap.note_C4.khe_name)
    return musthe_scales_translated_key


class ScaleFinder:
    pytheory_c4_scales = pytheory.TonedScale(tonic=txnote_khe_wrap.note_C4.khe_name)._scales

    def __init__(self):
        self.map = {}

    @beartype
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

        mingus_scales_found = []
        for mingus_current_scale in mingus_iterate_scales():
            current_name = hash_scale_name(mingus_scale_name(mingus_current_scale))
            if scale_to_find_name == current_name:
                mingus_scales_found.append(mingus_current_scale)
                assert_that(len(mingus_scales_found)).is_less_than(2)
        assert_that(len(mingus_scales_found)).is_less_than(2)
        scale_merged.mingus = mingus_scales_found

        for a in txscales_examples.all:
            if a.name == scale_to_find_name:
                scale_merged.txscale = a

        self.map[scale_to_find_name] = scale_merged
        return scale_merged


@beartype
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

    for a in txscales_examples.all:
        finder.find(a.name)

    return finder


@beartype
def scales_merge_and_detect_same():
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
