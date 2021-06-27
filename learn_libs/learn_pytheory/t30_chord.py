
from pytheory import Tone, Fretboard, CHARTS

tones = (
     Tone.from_string("F2"),
     Tone.from_string("C3"),
     Tone.from_string("G3"),
     Tone.from_string("D4"),
     Tone.from_string("A5"),
     Tone.from_string("E5")
 )

fretboard = Fretboard(tones=tones)

c_chord = CHARTS['western']["C"]

print(c_chord.fingering(fretboard=fretboard))