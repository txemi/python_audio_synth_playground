# https://github.com/kennethreitz/pytheory
from pytheory import TonedScale

from txpymusiclib.note_package import note_names_and_freq_static

# From scale
ts = TonedScale(tonic=note_names_and_freq_static.note_C4.name)
c_minor = ts['minor']
# c_minor
first = c_minor[0]
first_pitch = first.pitch()
g1 = c_minor["I"]
g1pitch = g1.pitch(symbolic=True)
if False:
    ttt = c_minor["tonic"]
    eee = ttt.pitch(temperament='pythagorean', symbolic=True)
print(1)
