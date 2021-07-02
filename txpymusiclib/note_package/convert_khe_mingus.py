from beartype import beartype


@beartype
def note_mingus_to_khe_name(mingus_name: str):
    if len(mingus_name) == 1:
        return mingus_name
    if len(mingus_name) == 2:
        if mingus_name[1] == '#':
            return mingus_name[0].lower()
    raise NotImplementedError()