import pychord
from pychord import Chord

# https://github.com/yuma-m/pychord

chord_am7 = Chord("Am7")
chord_am7_info = chord_am7.info()

chord_am7_comp = chord_am7.components()

bbb = pychord.note_to_chord(["C", "E", "G"])
ccc = pychord.note_to_chord(["F", "G", "C"])

cp = pychord.ChordProgression(["C", "G/B", "Am"])

uuu = pychord.Chord.from_note_index(note=1, quality="", scale="Cmaj")
print(chord_am7_info)
