from mingus.core import progressions

chords = progressions.to_chords(["I", "bIV", "VIIdim7"])
progression1 = progressions.determine(chords, "C", True)
progression2 = progressions.determine(chords, "C", False)
subst = progressions.substitute(["I", "IV", "V", "I"], 0)
print(1)
