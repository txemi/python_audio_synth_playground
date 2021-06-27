# https://github.com/kennethreitz/pytheory
from pytheory import Tone

from txpymusiclib.note_package import note_names_and_freq_static

c4_tone = Tone.from_string(note_names_and_freq_static.note_C4.name)
c4_pitch_s = c4_tone.pitch(symbolic=True)
met = dir(c4_pitch_s)
c4_pitch = c4_pitch_s.evalf()

c5_tone = Tone.from_string(note_names_and_freq_static.note_C5.name)
c5_pitch_s = c5_tone.pitch(symbolic=True)
c5_pitch_n = c5_pitch_s.evalf()
