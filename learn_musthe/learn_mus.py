# https://github.com/gciruelos/musthe

from musthe import *
from common.play import from_syntetizer


def play_scale(s):
    print(s)
    a = s[0]
    uuuuuuu = str(a)
    ioo = [s[i].scientific_notation() for i in range(len(s))]
    from_syntetizer.play_sequence_notes(ioo, 0.5)


s = Scale(Note('B'), 'major')
play_scale(s)

for s in Scale.all(include_greek_modes=True):
    print(s)
    play_scale(s)

s = Scale(Note('C4'), 'major')
s.notes
s.scales
s.intervals
c = Chord(Note('A'), 'M')
print(1)
