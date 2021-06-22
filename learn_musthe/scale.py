# https://github.com/gciruelos/musthe
import time

from musthe import *

from common.play import from_syntetizer


def semitones_scale_to_diffs(la):
    prev = None
    for a in la:
        if prev is not None:
            yield a - prev
        prev = a


def play_scale(current_scale):
    semitones = [i.semitones for i in current_scale.intervals]
    sem2 = list(semitones_scale_to_diffs(semitones))
    print(str(current_scale) + ":" + str(sem2))
    ioo = [current_scale[i].scientific_notation() for i in range(len(current_scale))]
    from_syntetizer.play_sequence_notes(ioo, 0.5)
    time.sleep(1)


scale4 = Scale(Note('C4'), 'major')
play_scale(scale4)

scale1 = Scale(Note('B'), 'major')
play_scale(scale1)

for scale3 in Scale.all(include_greek_modes=True):
    play_scale(scale3)
