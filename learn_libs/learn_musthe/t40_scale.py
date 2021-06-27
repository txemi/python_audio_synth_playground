# https://github.com/gciruelos/musthe
import musthe

from txpymusiclib.play.from_syntetizer import play_scale_from_musthescale

scale_C4_major = musthe.Scale(musthe.Note('C4'), 'major')
play_scale_from_musthescale(scale_C4_major)

scale_B_major = musthe.Scale(musthe.Note('B'), 'major')
play_scale_from_musthescale(scale_B_major)

for scale3 in musthe.Scale.all(include_greek_modes=True):
    play_scale_from_musthescale(scale3)
