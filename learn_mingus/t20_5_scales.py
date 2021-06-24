from mingus.core import scales

import txpymusiclib.scales_package.scale_static_examples_from_note_names
from txpymusiclib.scales_package import scale_static_examples
from txpymusiclib.scales_package.scale_mingus import scale_to_notenames, find_scale_by_name, get_semitones_from_mingus_scale, \
    find_scale_by_semitones

determine_example = scales.determine(['A', 'Bb', 'E', 'F#', 'G'])

c_major_determined = scales.determine(list(scale_to_notenames(
    txpymusiclib.scales_package.scale_static_examples_from_note_names.c_major_scale)))


def find_hardcoded_scales():
    found = {}
    for current in scale_static_examples.all:
        if sum(current) != 12:
            raise Exception()
        found[current] = list(find_scale_by_semitones(current))
    return found


hardcoded_scales_found = find_hardcoded_scales()


def check_hardcoded_scale():
    hardcoded_semitones = scale_static_examples.major

    c_major_1 = find_scale_by_name('C major')
    c_major_2 = scales.Major('C')

    c_major_2_ascending = c_major_2.ascending()
    c_major_2_degree_3 = c_major_2.degree(3)

    calculated_semitones = list(get_semitones_from_mingus_scale(c_major_1))
    if calculated_semitones != list(hardcoded_semitones):
        raise Exception()


check_hardcoded_scale()

# MingusNoteContainer().from_
# a1 = scales.Diatonic("C")
a2 = scales.Aeolian("A")
a3 = scales.MelodicMinor("A")
a4 = scales.Chromatic("C")
a5 = scales.HarmonicMajor("C")
a6 = scales.Ionian("C")
a9 = scales.Phrygian("C")
print(1)
