import time

import txpymusiclib.scales_package.txscales_examples
from txpymusiclib.note_package import txnote_khe_wrap
from txpymusiclib.play.play_mode import ScalePlayMode
from txpymusiclib.scales_package.scale_merge_from_all_libs import ScaleMergedFromLibs
from txpymusiclib.scales_package.scale_merge_from_all_libs import scales_merge_and_detect_same
from txpymusiclib.scales_package.scale_mingus_wrap import TxMingusScaleWrapper
from txpymusiclib.scales_package.scale_musthe_wrap import TxMustheScaleWrapper
from txpymusiclib.scales_package.scale_pytheory import TxPytheoryScaleWrapper
from txpymusiclib.scales_package.scale_txscale import TxTxScaleWrapper

duration_secs_per_note = 0.5


def test_playing_scale_by_name(scale_name, base_note):
    octaves = 1
    scale_play_mode = ScalePlayMode.octave_and_return
    time_to_wait_in_seconds = 5

    for current_scale_builder in (
            TxTxScaleWrapper, TxMingusScaleWrapper,
            TxPytheoryScaleWrapper, TxMustheScaleWrapper,):
        print(current_scale_builder.wrapped_lib_name)
        scale = current_scale_builder(scale_name=scale_name, base_note=base_note, octaves=octaves)
        scale.play(scale_play_mode=scale_play_mode, duration_secs_per_note=duration_secs_per_note)
        time.sleep(time_to_wait_in_seconds)


test_playing_scale_by_name(scale_name=txpymusiclib.scales_package.txscales_examples.major.name,
                           base_note=txnote_khe_wrap.note_C4)

test_playing_scale_by_name(scale_name=txpymusiclib.scales_package.txscales_examples.phrygian.name,
                           base_note=txnote_khe_wrap.note_C4)


def play_all_scales_found_in_libs():
    # iterate all and cross find
    scales_merged = scales_merge_and_detect_same()
    scales_set = set(scales_merged.map.values())

    for current_scale in scales_set:
        assert isinstance(current_scale, ScaleMergedFromLibs)
        print("<" + current_scale.format() + ">")
        current_scale.play(duration_secs=duration_secs_per_note)
        print("\n")


play_all_scales_found_in_libs()
print(1)
