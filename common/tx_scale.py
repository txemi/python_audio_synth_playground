from beartype import beartype
from musthe import Scale as MustheScale

blues = (0, 3, 2, 1, 1, 3, 2)
doble_armonica = (0, 1, 3, 1, 2, 1, 3, 1)
c_major_scale = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']
mayor = (0, 2, 2, 1, 2, 2, 2, 1)
menor = (0, 2, 1, 2, 2, 1, 2, 2)
frigia = (0, 1, 2, 2, 2, 1, 2, 2)
cromatica = (0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)


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
