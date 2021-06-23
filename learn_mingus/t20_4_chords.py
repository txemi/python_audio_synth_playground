from mingus.core import chords
from mingus.core import keys

a3 = keys.get_notes()
a4 = keys.get_notes("D")
a = chords.triads("C")
a2 = chords.triads("C#")
a5 = chords.augmented_minor_seventh("C")
a6 = chords.from_shorthand("Cm")
a7 = chords.I("C")
a8 = chords.determine(["C", "E", "G"])
a9 = chords.determine(["C", "E", "G"], True)
print(1)
