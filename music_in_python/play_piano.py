import common.txtone
from common import utils_khe
from common.play.from_pytheory import playKatiNote

note_freqs = common.txtone.get_piano_notes()

for note in note_freqs:
    if not note:
        continue
    freq = note_freqs[note]
    playKatiNote(note, freq)
    pass
