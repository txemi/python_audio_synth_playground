# https://github.com/gciruelos/musthe

from musthe import *
from common.play import from_syntetizer


def play_scale(current_scale):
    print(current_scale)
    a = current_scale[0]
    uuuuuuu = str(a)
    current_scale.notes
    current_scale.scales
    current_scale.intervals
    ioo = [current_scale[i].scientific_notation() for i in range(len(current_scale))]
    from_syntetizer.play_sequence_notes(ioo, 0.5)


scale1 = Scale(Note('B'), 'major')
play_scale(scale1)

scale4 = Scale(Note('C4'), 'major')
play_scale(scale4)

for scale3 in Scale.all(include_greek_modes=True):
    print(scale3)
    play_scale(scale3)




c = Chord(Note('A'), 'M')
print(1)
