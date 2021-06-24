from mingus.core import scales

from txpymusiclib.scales_package import musical_mode_examples
from txpymusiclib.scales_package.scale_mingus import find_scale_by_name, \
    get_semitones_from_mingus_scale, \
    find_scale_by_semitones

determine_example = scales.determine(['A', 'Bb', 'E', 'F#', 'G'])


def find_hardcoded_scales():
    found = {}
    for current in musical_mode_examples.all:
        found[current.semitones] = find_scale_by_semitones(current)
    return found


hardcoded_scales_found = find_hardcoded_scales()


def check_hardcoded_scale():
    hardcoded_semitones = musical_mode_examples.major

    c_major_1 = find_scale_by_name('C major')
    c_major_2 = scales.Major('C')

    c_major_2_ascending = c_major_2.ascending()
    c_major_2_degree_3 = c_major_2.degree(3)

    calculated_semitones = get_semitones_from_mingus_scale(c_major_1)
    if calculated_semitones != hardcoded_semitones:
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
