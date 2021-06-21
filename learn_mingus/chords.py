
import mingus.core.chords as chords
from mingus.midi import fluidsynth
# la menor, do mayor, mi mayor, fa mayor
for lala in ('Am','CM','EM','FM'):
    Am=chords.from_shorthand(lala)
    d=chords.determine(Am)
    print(lala + " "+ str(Am) + " "+ str(d))
    fluidsynth.play_Note(Am[0]+'-4')

print(1)