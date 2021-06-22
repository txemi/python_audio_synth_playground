# https://github.com/gciruelos/musthe

from musthe import *
from common.play import from_syntetizer


def play_scale(scale2):
    print(scale2)
    a = scale2[0]
    uuuuuuu = str(a)
    ioo = [scale2[i].scientific_notation() for i in range(len(scale2))]
    from_syntetizer.play_sequence_notes(ioo, 0.5)


scale1 = Scale(Note('B'), 'major')
play_scale(scale1)

for scale3 in Scale.all(include_greek_modes=True):
    print(scale3)
    play_scale(scale3)

scale4 = Scale(Note('C4'), 'major')
scale4.notes
scale4.scales
scale4.intervals

c = Chord(Note('A'), 'M')
print(1)
