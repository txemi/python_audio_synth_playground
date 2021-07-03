import musthe
import pytheory
from mingus import core as mingus_core

import txpymusiclib.scales_package.txscales_examples
from txpymusiclib.note_package import txnote_khe_wrap
from txpymusiclib.play.play_mingus_in_synthesizer import mingus_play
from txpymusiclib.play.play_musthe_in_synthetizer import play_scale_from_musthescale
from txpymusiclib.play.play_txnote_in_synthetizer import play_txscale
from txpymusiclib.scales_package.scale_merge_from_all_libs import ScaleMergedFromLibs
from txpymusiclib.scales_package.scale_merge_from_all_libs import scales_merge_and_detect_same
from txpymusiclib.scales_package.txscales_examples import phrygian

duration_secs_per_note = 0.3


def test_playing_phrygian():
    base_note = txnote_khe_wrap.note_C4
    octaves = 1
    scale_name = txpymusiclib.scales_package.txscales_examples.phrygian.name

    # test scale (phrygian) mingus
    mingus_phrygian_c = mingus_core.scales.Phrygian("C", octaves=octaves)
    mingus_phrygian_c.octaves = octaves
    mingus_play(mingus_phrygian_c, duration_secs=duration_secs_per_note, octave=base_note.get_octave())

    # pytherory
    pytheory_c4 = pytheory.TonedScale(tonic=base_note.khe_name)
    pytherory_phrygian_C4 = pytheory_c4[scale_name]

    # musthe
    musthe_phrygian_C4 = musthe.Scale(musthe.Note(base_note.khe_name),
                                      scale_name)
    play_scale_from_musthescale(musthe_phrygian_C4, duration_secs_per_note=duration_secs_per_note)

    # txscale
    play_txscale(base_note, phrygian, duration_secs=duration_secs_per_note)


test_playing_phrygian()


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
