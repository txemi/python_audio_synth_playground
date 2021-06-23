# https://github.com/gciruelos/musthe

from musthe import *

from common.play.from_syntetizer import play_scale_from_musthescale

scale4 = Scale(Note('C4'), 'major')
play_scale_from_musthescale(scale4)

scale1 = Scale(Note('B'), 'major')
play_scale_from_musthescale(scale1)

for scale3 in Scale.all(include_greek_modes=True):
    play_scale_from_musthescale(scale3)
