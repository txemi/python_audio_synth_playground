# https://github.com/kennethreitz/pytheory
from pytheory import TonedScale

from txpymusiclib.note_package import note_names_and_freq_static

# From scale
ts = TonedScale(tonic=note_names_and_freq_static.note_C4.name)
c_minor = ts['minor']
# c_minor
first = c_minor[0]
pitch = first.pitch()
aaa = c_minor["I"]
bbb = aaa.pitch(symbolic=True)
if False:
    ttt = c_minor["tonic"]
    eee = ttt.pitch(temperament='pythagorean', symbolic=True)
print(1)
