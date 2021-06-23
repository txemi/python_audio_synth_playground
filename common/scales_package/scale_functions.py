from beartype import beartype


@beartype
def semitones_scale_to_diffs(semitone_numbers: list[int]):
    prev = None
    for current in semitone_numbers:
        if prev is not None:
            yield current - prev
        prev = current


