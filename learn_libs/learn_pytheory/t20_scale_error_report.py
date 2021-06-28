# https://github.com/kennethreitz/pytheory
from pytheory import TonedScale

tsC4 = TonedScale(tonic='C4')
c4_major = tsC4['major']
c4_ionian = tsC4['ionian']
print('major: ' + str(c4_major))
print('ionian: ' + str(c4_ionian))
