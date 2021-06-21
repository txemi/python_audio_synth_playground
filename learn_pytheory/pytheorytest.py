# https://github.com/kennethreitz/pytheory
from pytheory import TonedScale, Tone
c4_tone = Tone.from_string('C4')
c4_pitch_s=c4_tone.pitch(symbolic=True)
met=dir(c4_pitch_s)
c4_pitch=c4_pitch_s.evalf()

c5_tone = Tone.from_string('C5')
c5_pitch_s=c5_tone.pitch(symbolic=True)
c5_pitch_n=c5_pitch_s.evalf()

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
