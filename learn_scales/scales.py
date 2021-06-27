import musthe
import pytheory
from mingus import core as mingus_core

import txpymusiclib.scales_package.txscales_examples
from txpymusiclib.note_package import note_names_and_freq_static
from txpymusiclib.play.from_syntetizer import play_scale_from_musthescale

mingus_phrygian_c = mingus_core.scales.Phrygian("C")

pytheory_c4 = pytheory.TonedScale(tonic=note_names_and_freq_static.note_C4.name)
pytherory_phrygian_C4 = pytheory_c4[txpymusiclib.scales_package.txscales_examples.phrygian.name]

musthe_phrygian_C4 = musthe.Scale(musthe.Note(note_names_and_freq_static.note_C4.name), txpymusiclib.scales_package.txscales_examples.phrygian.name)
play_scale_from_musthescale(musthe_phrygian_C4)

print(1)
