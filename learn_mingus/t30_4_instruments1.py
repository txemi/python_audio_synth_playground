from mingus.containers import Piano

piano = Piano()
piano_range = piano.range
piano_range_init = piano_range[0]

for c3_major_chord_mingus in piano_range:
    print(c3_major_chord_mingus)

piano_range_init.augment()
