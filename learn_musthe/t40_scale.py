# https://github.com/gciruelos/musthe

from musthe import *

from common.play.from_syntetizer import play_scale_from_musthescale

scale_C4_major = Scale(Note('C4'), 'major')
play_scale_from_musthescale(scale_C4_major)

scale_B_major = Scale(Note('B'), 'major')
play_scale_from_musthescale(scale_B_major)

for scale3 in Scale.all(include_greek_modes=True):
    play_scale_from_musthescale(scale3)
