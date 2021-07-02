# https://github.com/kennethreitz/pytheory
from pytheory import Tone

from txpymusiclib.note_package import txnote_khe_wrap

c4_tone = Tone.from_string(txnote_khe_wrap.note_C4.khe_name)
c4_pitch_s = c4_tone.pitch(symbolic=True)
met = dir(c4_pitch_s)
c4_pitch = c4_pitch_s.evalf()

c5_tone = Tone.from_string(txnote_khe_wrap.note_C5.khe_name)
c5_pitch_s = c5_tone.pitch(symbolic=True)
c5_pitch_n = c5_pitch_s.evalf()
