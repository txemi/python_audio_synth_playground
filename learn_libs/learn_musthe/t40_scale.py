# https://github.com/gciruelos/musthe
import musthe

from txpymusiclib.note_package import note_names_and_freq_static
from txpymusiclib.play.from_syntetizer import play_scale_from_musthescale
from txpymusiclib.scales_package import txscales_examples

scale_C4_major = musthe.Scale(musthe.Note(note_names_and_freq_static.note_C4.name), txscales_examples.major.name)
play_scale_from_musthescale(scale_C4_major)

scale_B_major = musthe.Scale(musthe.Note('B'), txscales_examples.major.name)
play_scale_from_musthescale(scale_B_major)

for current_scale in musthe.Scale.all(include_greek_modes=True):
    play_scale_from_musthescale(current_scale)
