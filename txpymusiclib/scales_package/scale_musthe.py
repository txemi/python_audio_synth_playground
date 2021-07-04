from beartype import beartype
from musthe import Scale as MustheScale

from txpymusiclib.scales_package.scale_functions import semitones_scale_to_diffs
from txpymusiclib.scales_package.txscales import TxScaleSt


@beartype
def musthescale_semitones(current_scale: MustheScale) -> TxScaleSt:
    semitones = [i.semitones for i in current_scale.intervals]
    semitone_diffs = list(semitones_scale_to_diffs(semitones))
    semitone_diffs.append(12 - semitones[-1])
    return TxScaleSt(semitone_diffs)
