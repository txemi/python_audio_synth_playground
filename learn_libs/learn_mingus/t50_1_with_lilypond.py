# FAILS: does not find this import
import mingus.extra.LilyPond as LilyPond
from mingus.containers import Bar

b = Bar()
b + "C"
b + "E"
b + "G"
b + "B"
lllll = LilyPond.from_Bar(b)
print(lllll)
