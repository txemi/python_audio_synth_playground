
import mingus.core.chords as chords
from mingus.midi import fluidsynth
# la menor, do mayor, mi mayor, fa mayor
for current_chord_name in ('Am', 'CM', 'EM', 'FM'):
    mingus_chord=chords.from_shorthand(current_chord_name)
    d=chords.determine(mingus_chord)
    print(current_chord_name + " " + str(mingus_chord) + " " + str(d))
    fluidsynth.play_Note(mingus_chord[0] + '-4')

print(1)