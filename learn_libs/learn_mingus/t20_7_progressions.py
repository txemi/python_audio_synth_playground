from mingus.core import progressions

a = progressions.to_chords(["I", "bIV", "VIIdim7"])
progressions.determine(a, "C", True)
