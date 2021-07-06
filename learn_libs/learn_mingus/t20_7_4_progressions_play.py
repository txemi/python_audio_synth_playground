from txpymusiclib.chords_package import chord_progression_examples

# from mingus.midi import fluidsynth


# la menor, do mayor, mi mayor, fa mayor

for current_progression in chord_progression_examples.chord_progression_examples:
    current_progression.progression_test()

print(1)
