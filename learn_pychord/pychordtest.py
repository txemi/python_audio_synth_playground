from pychord import Chord
import pychord

chord_am7 = Chord("Am7")
chord_am7_info = chord_am7.info()

chord_am7_comp = chord_am7.components()

bbb = pychord.note_to_chord(["C", "E", "G"])
print(chord_am7_info)
