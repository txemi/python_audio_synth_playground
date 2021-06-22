# https://wiki.python.org/moin/PythonInMusic
# http://bspaans.github.io/python-mingus/doc/wiki/tutorialCore
import mingus.core.chords as chords
import mingus.core.notes as notes
from common.txchord import TxChord
from mingus.containers import NoteContainer
from mingus.containers import Note

from common.txtone import note2mingus

c_is_valid = notes.is_valid_note("C")
print(c_is_valid)

c_chord = chords.major_triad("C")
print(c_chord)

c3_major_chord_mingus = list(note2mingus(TxChord.c3_major_chord_names))
# falla cc = chords.determine(uuu)

c3_major_container = NoteContainer(c3_major_chord_mingus)
ua=c3_major_container.determine()
ic=c3_major_container.is_consonant()
note=c3_major_container.notes[0]
assert isinstance(note,Note)

chord_container=NoteContainer(list(TxChord.otro_chord_mingus))
chord_container.determine()

print(c3_major_container)




