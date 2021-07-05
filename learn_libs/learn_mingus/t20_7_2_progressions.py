from mingus.core import progressions

a = progressions.to_chords(["I", "bIV", "VIIdim7"])
b = progressions.determine(a, "C", True)
b2 = progressions.determine(a, "C", False)
b3 = progressions.substitute(["I", "IV", "V", "I"], 0)
print(1)
