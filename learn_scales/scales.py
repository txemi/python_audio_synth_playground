import musthe
import pytheory
from mingus import core as mingus_core

import txpymusiclib.scales_package.txscales_examples
from txpymusiclib.note_package import note_names_and_freq_static
from txpymusiclib.play.from_syntetizer import play_scale_from_musthescale
from txpymusiclib.scales_package.scale_from_all_libs import scale_get_from_all_libs, detect_same_scales

# test scale (phrygian)
mingus_phrygian_c = mingus_core.scales.Phrygian("C")

pytheory_c4 = pytheory.TonedScale(tonic=note_names_and_freq_static.note_C4.name)
pytherory_phrygian_C4 = pytheory_c4[txpymusiclib.scales_package.txscales_examples.phrygian.name]

musthe_phrygian_C4 = musthe.Scale(musthe.Note(note_names_and_freq_static.note_C4.name),
                                  txpymusiclib.scales_package.txscales_examples.phrygian.name)
play_scale_from_musthescale(musthe_phrygian_C4)

# iterate all and cross find
found = scale_get_from_all_libs()
scales_merged = detect_same_scales()
scales_2 = set(scales_merged.map.values())
print(1)
