from beartype import beartype
from musthe import Scale as MustheScale

from txpymusiclib.scales_package.scale_functions import semitones_scale_to_diffs
from txpymusiclib.scales_package.txscales import TxScaleSt


@beartype
def musthescale_semitones(current_scale: MustheScale):
    semitones = [i.semitones for i in current_scale.intervals]
    semitone_diffs = list(semitones_scale_to_diffs(semitones))
    semitone_diffs.append(12 - semitones[-1])
    return TxScaleSt(semitone_diffs)


@beartype
def musthescale_notes(current_scale: MustheScale):
    semitone_diffs = musthescale_semitones(current_scale)
    notes_in_scale = [current_scale[i].scientific_notation() for i in range(len(current_scale))]
    description = str(current_scale) + ":" + str(semitone_diffs.semitones) + ":" + str(notes_in_scale)
    return notes_in_scale, description
