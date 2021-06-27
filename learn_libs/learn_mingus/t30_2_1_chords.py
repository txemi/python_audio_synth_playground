# https://wiki.python.org/moin/PythonInMusic
# http://bspaans.github.io/python-mingus/doc/wiki/tutorialCore
import mingus.core.chords as chords
from mingus.containers import Note
from mingus.containers import NoteContainer

from txpymusiclib.chords_package.txchord import TxChord
from txpymusiclib.note_package.note_convert_mingus import note_names_2_mingus_note_names

c_chord = chords.major_triad("C")
print(c_chord)

c3_major_chord_mingus = list(note_names_2_mingus_note_names(TxChord.c3_major_chord_names))
# falla cc = chords.determine(uuu)

c3_major_container = NoteContainer(c3_major_chord_mingus)
deter1 = c3_major_container.determine()
is_conson = c3_major_container.is_consonant()
note = c3_major_container.notes[0]
assert isinstance(note, Note)

chord_container = NoteContainer(list(TxChord.otro_chord_mingus))
chord_container.determine()

print(c3_major_container)
