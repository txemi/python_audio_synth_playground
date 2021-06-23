from mingus.core import scales

from common.scales_package import scale_static_examples
from common.scales_package.scale_mingus import scale_to_notenames, find_scale_by_name, get_semitones_from_mingus_scale,find_scale_by_semitones


find_scale_by_semitones(scale_static_examples.blues)

a8 = scales.determine(list(scale_to_notenames(scale_static_examples.c_major_scale)))

a10 = scales.determine(['A', 'Bb', 'E', 'F#', 'G'])


def check_semitones_scale():
    hardcoded = scale_static_examples.mayor

    c_major_1 = find_scale_by_name('C major')
    c_major_2 = scales.Major('C')

    c_major_2_ascending = c_major_2.ascending()
    c_major_2_degree_3 = c_major_2.degree(3)

    uauaua = list(get_semitones_from_mingus_scale(c_major_1))
    if uauaua != list(hardcoded):
        raise Exception()

check_semitones_scale()


# MingusNoteContainer().from_
# a1 = scales.Diatonic("C")
a2 = scales.Aeolian("A")
a3 = scales.MelodicMinor("A")
a4 = scales.Chromatic("C")
a5 = scales.HarmonicMajor("C")
a6 = scales.Ionian("C")
a9 = scales.Phrygian("C")
print(1)
