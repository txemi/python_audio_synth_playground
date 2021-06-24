from beartype import beartype
from musthe import Scale as MustheScale

from txpymusiclib.scales_package.scale_functions import semitones_scale_to_diffs


@beartype
def musthescale_notes(current_scale: MustheScale):
    semitones = [i.semitones for i in current_scale.intervals]
    semitone_diffs = list(semitones_scale_to_diffs(semitones))
    notes_in_scale = [current_scale[i].scientific_notation() for i in range(len(current_scale))]
    description = str(current_scale) + ":" + str(semitone_diffs) + ":" + str(notes_in_scale)
    return notes_in_scale, description