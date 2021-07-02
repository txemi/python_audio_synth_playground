# https://github.com/gciruelos/musthe
import musthe

from txpymusiclib.note_package import txnote_khe_wrap
from txpymusiclib.play.play_musthe_in_synthetizer import play_scale_from_musthescale
from txpymusiclib.scales_package import txscales_examples

scale_C4_major = musthe.Scale(musthe.Note(txnote_khe_wrap.note_C4.khe_name), txscales_examples.major.khe_name)
play_scale_from_musthescale(scale_C4_major)

scale_B_major = musthe.Scale(musthe.Note('B'), txscales_examples.major.khe_name)
play_scale_from_musthescale(scale_B_major)

for current_scale in musthe.Scale.all(include_greek_modes=True):
    play_scale_from_musthescale(current_scale)
