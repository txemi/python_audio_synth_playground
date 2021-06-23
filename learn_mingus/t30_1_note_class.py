# https://wiki.python.org/moin/PythonInMusic
# http://bspaans.github.io/python-mingus/doc/wiki/tutorialCore
import mingus.core.notes as notes
from mingus.containers import Note

c_is_valid = notes.is_valid_note("C")
print(c_is_valid)

note1 = Note("Cb", 4)
print(note1)
print(int(note1))
note2 = Note("C#", 4)
print(str(int(note2)) + note2.remove_redundant_accidentals())
note3 = Note("Db", 4)
print(int(note3)+note3.remove_redundant_accidentals())
# equal111 = (note3 == note2)

mapa = {}
mapa[note1] = 1
mapa[note2] = 2
mapa[note3] = 3
print(1)
