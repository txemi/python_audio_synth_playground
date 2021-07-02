import musthe
import pytheory
from mingus import core as mingus_core

import txpymusiclib.scales_package.txscales_examples
from txpymusiclib.note_package import txnote_khe_wrap
from txpymusiclib.play.play_musthe_in_synthetizer import play_scale_from_musthescale
from txpymusiclib.scales_package.scale_merge_from_all_libs import ScaleMergedFromLibs
from txpymusiclib.scales_package.scale_merge_from_all_libs import scales_merge_and_detect_same

# test scale (phrygian)
mingus_phrygian_c = mingus_core.scales.Phrygian("C")

pytheory_c4 = pytheory.TonedScale(tonic=txnote_khe_wrap.note_C4.khe_name)
pytherory_phrygian_C4 = pytheory_c4[txpymusiclib.scales_package.txscales_examples.phrygian.khe_name]

musthe_phrygian_C4 = musthe.Scale(musthe.Note(txnote_khe_wrap.note_C4.khe_name),
                                  txpymusiclib.scales_package.txscales_examples.phrygian.khe_name)
play_scale_from_musthescale(musthe_phrygian_C4)

# iterate all and cross find
scales_merged = scales_merge_and_detect_same()
scales_set = set(scales_merged.map.values())

for current_scale in scales_set:
    assert isinstance(current_scale, ScaleMergedFromLibs)
    print("<" + current_scale.format() + ">")
    current_scale.play()
    print("\n")

print(1)
