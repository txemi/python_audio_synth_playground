from beartype import beartype
from musthe import Scale as MustheScale


@beartype
def semitones_scale_to_diffs(semitone_numbers: list[int]):
    prev = None
    for current in semitone_numbers:
        if prev is not None:
            yield current - prev
        prev = current


@beartype
def musthescale_notes(current_scale: MustheScale):
    semitones = [i.semitones for i in current_scale.intervals]
    sem2 = list(semitones_scale_to_diffs(semitones))
    notes_in_scale = [current_scale[i].scientific_notation() for i in range(len(current_scale))]
    description = str(current_scale) + ":" + str(sem2) + ":" + str(notes_in_scale)
    return notes_in_scale, description