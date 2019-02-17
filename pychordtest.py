from pychord import Chord
import pychord

c = Chord("Am7")
aa = c.info()

ccc = c.components()

bbb = pychord.note_to_chord(["C", "E", "G"])
print(aa)
