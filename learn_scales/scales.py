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

# test scale (phrygian) mingus
mingus_phrygian_c = mingus_core.scales.Phrygian("C", octaves=1)
mingus_phrygian_c.octaves = 1
mingus_play(mingus_phrygian_c, octave=4)

# pytherory
pytheory_c4 = pytheory.TonedScale(tonic=txnote_khe_wrap.note_C4.khe_name)
pytherory_phrygian_C4 = pytheory_c4[txpymusiclib.scales_package.txscales_examples.phrygian.name]

# musthe
musthe_phrygian_C4 = musthe.Scale(musthe.Note(txnote_khe_wrap.note_C4.khe_name),
                                  txpymusiclib.scales_package.txscales_examples.phrygian.name)
play_scale_from_musthescale(musthe_phrygian_C4)

# txscale
play_txscale(phrygian)


def play_all_scales_found_in_libs():
    # iterate all and cross find
    scales_merged = scales_merge_and_detect_same()
    scales_set = set(scales_merged.map.values())

    for current_scale in scales_set:
        assert isinstance(current_scale, ScaleMergedFromLibs)
        print("<" + current_scale.format() + ">")
        current_scale.play()
        print("\n")


play_all_scales_found_in_libs()
print(1)
