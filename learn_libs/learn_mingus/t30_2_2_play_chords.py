import time

import txpymusiclib.play.play_mingus_in_synthesizer
from txpymusiclib.chords_package import chord_progression_examples

# from mingus.midi import fluidsynth

txpymusiclib.play.play_mingus_in_synthesizer.play_chords_loop_chord_notation(
    chord_progression_examples.NiceChordSeqExample, 3)
time.sleep(1)

txpymusiclib.play.play_mingus_in_synthesizer.play_chords_loop_chord_notation(chord_progression_examples.LordOfRings, 3)
time.sleep(1)

chord_progression_examples.chord_progression_example_1.progression_test()
time.sleep(1)

for current_progression in chord_progression_examples.chord_progression_examples:
    print(current_progression)
    current_progression.progression_test()
    print('\n')
    time.sleep(1)

print(1)
