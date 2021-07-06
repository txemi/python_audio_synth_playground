import txpymusiclib.play.play_mingus_in_synthesizer
from txpymusiclib.chords_package import chord_progression_examples

# from mingus.midi import fluidsynth


for a in chord_progression_examples.chord_progression_examples:
    print(a)
    txpymusiclib.play.play_mingus_in_synthesizer.play_progressions_roman(a)
    print('\n')

txpymusiclib.play.play_mingus_in_synthesizer.play_progressions_roman(
    chord_progression_examples.chord_progression_example_1)

txpymusiclib.play.play_mingus_in_synthesizer.play_chords_loop_chord_notation(chord_progression_examples.LordOfRings, 3)

txpymusiclib.play.play_mingus_in_synthesizer.play_chords_loop_chord_notation(
    chord_progression_examples.NiceChordSeqExample, 3)

print(1)
