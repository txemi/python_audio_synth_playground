import time

import musthe
import pytheory

import txpymusiclib.scales_package.txscales_examples
from txpymusiclib.note_package import txnote_khe_wrap
from txpymusiclib.play.play_mingus_in_synthesizer import mingus_play
from txpymusiclib.play.play_mode import ScalePlayMode
from txpymusiclib.play.play_musthe_in_synthetizer import play_scale_from_musthescale
from txpymusiclib.play.play_txnote_in_synthetizer import play_txscale
from txpymusiclib.scales_package.scale_merge_from_all_libs import ScaleMergedFromLibs
from txpymusiclib.scales_package.scale_merge_from_all_libs import scales_merge_and_detect_same
from txpymusiclib.scales_package.scale_mingus import mingus_scale_build_from_name
from txpymusiclib.scales_package.txscales_examples import find_scale_by_name_unique

duration_secs_per_note = 0.5


def test_playing_phrygian(scale_name, base_note):
    octaves = 1
    scale_play_mode = ScalePlayMode.octave_and_return
    time_to_wait=5
    print("txscale")
    play_txscale(base_note, find_scale_by_name_unique(scale_name), duration_secs=duration_secs_per_note,
                 mode=scale_play_mode)
    time.sleep(time_to_wait)

    print("mingus")
    mingus_phrygian_c = mingus_scale_build_from_name(scale_name, base_note=base_note.khe_name[0], octaves=octaves)
    mingus_play(mingus_phrygian_c, duration_secs=duration_secs_per_note, octave=base_note.get_octave(),
                mode=scale_play_mode)
    time.sleep(time_to_wait)

    print("pytherory")
    pytheory_c4 = pytheory.TonedScale(tonic=base_note.khe_name)
    pytherory_phrygian_C4 = pytheory_c4[scale_name]

    print("musthe")
    musthe_phrygian_C4 = musthe.Scale(musthe.Note(base_note.khe_name),
                                      scale_name)
    play_scale_from_musthescale(musthe_phrygian_C4, duration_secs_per_note=duration_secs_per_note)
    time.sleep(time_to_wait)


test_playing_phrygian(scale_name=txpymusiclib.scales_package.txscales_examples.major.name,
                      base_note=txnote_khe_wrap.note_C4)

test_playing_phrygian(scale_name=txpymusiclib.scales_package.txscales_examples.phrygian.name,
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
