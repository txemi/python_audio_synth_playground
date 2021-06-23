import common.note_package.note_freq_funcs
import common.note_package.note_conversions
from common.play.from_pytheory import playKatiNoteFromNameAndStr

note_freqs = common.tonepackage.note_freq_funcs.get_piano_notes_khe()

for note in note_freqs:
    if not note:
        continue
    freq = note_freqs[note]
    playKatiNoteFromNameAndStr(note, freq)
    pass
