# https://github.com/kennethreitz/pytheory
from pytheory import TonedScale

import txpymusiclib.scales_package.txscales_examples
from txpymusiclib.note_package import txnote_khe_wrap

# From scale
tsC4 = TonedScale(tonic=txnote_khe_wrap.note_C4.khe_name)
c4_minor = tsC4['minor']
# c_minor
first = c4_minor[0]
first_pitch = first.pitch()
g1 = c4_minor["I"]
g1pitch = g1.pitch(symbolic=True)

tsC4p = tsC4[txpymusiclib.scales_package.txscales_examples.phrygian.khe_name]


tsC4i = tsC4[txpymusiclib.scales_package.txscales_examples.ionian.khe_name]

if False:
    ttt = c_minor["tonic"]
    eee = ttt.pitch(temperament='pythagorean', symbolic=True)
print(1)
