# https://wiki.python.org/moin/PythonInMusic
# http://bspaans.github.io/python-mingus/doc/wiki/tutorialCore
import mingus.core.chords as chords
import mingus.core.notes as notes
from common.txchord import TxChord
from mingus.containers import NoteContainer
from mingus.containers.instrument import Instrument, Piano, Guitar
from mingus.containers import Note
aa = notes.is_valid_note("C")
print(aa)

bb = chords.major_triad("C")
print(bb)


def note2mingus(a):
    for b in a:
        yield b[:1] + "-" + b[-1:]


uuu = list(note2mingus(TxChord.c3_major_chord_names))
# falla cc = chords.determine(uuu)

cc = NoteContainer(uuu)
ua=cc.determine()
ic=cc.is_consonant()
note=cc.notes[0]
assert isinstance(note,Note)

asdf=NoteContainer(list(note2mingus(TxChord.otro_chord_mingus)))
asdf.determine()

print(cc)

p=Piano()
rr=p.range
for uuu in rr:
    print(uuu)

loil=rr[0]
loil.augment()


