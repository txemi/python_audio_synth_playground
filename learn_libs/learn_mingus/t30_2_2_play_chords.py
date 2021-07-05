import txpymusiclib.play.play_mingus_in_synthesizer
from txpymusiclib.chords_package import chord_progression_examples

# from mingus.midi import fluidsynth
# la menor, do mayor, mi mayor, fa mayor

for a in chord_progression_examples.Examples3:
    print(a)
    txpymusiclib.play.play_mingus_in_synthesizer.play_progressions(a)
    print('\n')

txpymusiclib.play.play_mingus_in_synthesizer.play_progressions(chord_progression_examples.Example2)

txpymusiclib.play.play_mingus_in_synthesizer.play_chords_loop_chord_notation(chord_progression_examples.LordOfRings, 3)

txpymusiclib.play.play_mingus_in_synthesizer.play_chords_loop_chord_notation(
    chord_progression_examples.NiceChordSeqExample, 3)

print(1)
