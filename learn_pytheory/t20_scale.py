# https://github.com/kennethreitz/pytheory
from pytheory import TonedScale, Tone


# From scale
ts=TonedScale(tonic='C4')
c_minor = ts['minor']
#c_minor
first=c_minor[0]
pitch=first.pitch()
aaa=c_minor["I"]
bbb=aaa.pitch(symbolic=True)
if False:
    ttt=c_minor["tonic"]
    eee=ttt.pitch(temperament='pythagorean', symbolic=True)
print(1)
