# https://wiki.python.org/moin/PythonInMusic
# http://bspaans.github.io/python-mingus/doc/wiki/tutorialCore
import mingus.core.chords as chords
import mingus.core.notes as notes
from common.txintervals import TxChord
from mingus.containers import NoteContainer
from mingus.containers.instrument import Instrument, Piano, Guitar

aa = notes.is_valid_note("C")
print(aa)

bb = chords.major_triad("C")
print(bb)


def bla2mingus(a):
    for b in a:
        yield b[:1] + "-" + b[-1:]


uuu = list(bla2mingus(TxChord.c3_major_chord_names))
# falla cc = chords.determine(uuu)

cc = NoteContainer(uuu)
ua=cc.determine()
print(cc)

p=Piano()
rr=p.range
for uuu in rr:
    print(uuu)

loil=rr[0]
loil.augment()
p.name
from mingus.containers import Bar
import mingus.extra.LilyPond as LilyPond

b = Bar()
b + "C"
b + "E"
b + "G"
b + "B"
lllll=LilyPond.from_Bar(b)
print(lllll)

