def musthe_note_to_txkhenote(aaa):
    assert len(aaa.letter.name) == 1
    new_name = aaa.letter.name + str(aaa.octave)
    return new_name