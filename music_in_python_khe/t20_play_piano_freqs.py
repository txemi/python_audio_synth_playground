from txpymusiclib.note_package import note_freq_funcs
from txpymusiclib.play.from_pytheory import playKatiNoteFromNameAndStr

note_freqs = note_freq_funcs.get_piano_notes_khe()

for note in note_freqs:
    if not note:
        continue
    freq = note_freqs[note]
    playKatiNoteFromNameAndStr(note, freq)
    pass
