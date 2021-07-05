import time

from beartype import beartype
from mingus.core import progressions

import txpymusiclib.play.play_mingus_in_synthesizer
from txpymusiclib.chords_package import chord_progression_examples


@beartype
def progression_test(progression1: list[str]):
    print(progression1)
    key = "C"
    txpymusiclib.play.play_mingus_in_synthesizer.play_progressions(progression1)
    chords1 = progressions.to_chords(progression1, key=key)
    print(chords1)
    back_to_progression = progressions.determine(chords1, key=key, shorthand=True)
    back_to_progression_shorthand = progressions.determine(chords1, key=key, shorthand=False)
    subtitution = progressions.substitute(progression1, 0)
    print('\n')
    time.sleep(1.0)


progression_test(["I", "bIV", "VIIdim7"])
progression_test(["I", "IV", "V", "I"])
# from mingus.midi import fluidsynth
# la menor, do mayor, mi mayor, fa mayor

for current_progression in chord_progression_examples.Examples3:
    progression_test(list(current_progression))

print(1)
