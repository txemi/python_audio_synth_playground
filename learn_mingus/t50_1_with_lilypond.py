p.name
from mingus.containers import Bar
import mingus.extra.LilyPond as LilyPond

b = Bar()
b + "C"
b + "E"
b + "G"
b + "B"
lllll=LilyPond.from_Bar(b)
print(lllll)