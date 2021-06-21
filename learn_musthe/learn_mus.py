# https://github.com/gciruelos/musthe

from musthe import *
for s in Scale.all():
    print (s)
s = Scale(Note('C4'), 'major')
s.notes
s.scales
s.intervals
c= Chord(Note('A'), 'M')
print(1)