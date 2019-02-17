def interval_factor(half_steps):
    return 2 ** (half_steps / 12)


fifth_1 = 3 / 2
fifth_2 = interval_factor(7.0)
A4_freq=440.0
C_major_chord = [261.626,  329.628, 391.996]