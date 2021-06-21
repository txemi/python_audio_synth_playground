from common import utils
from common.play.from_pytheory import playKatiNote

note_freqs = utils.get_piano_notes()

for note in note_freqs:
    if not note:
        continue
    freq = note_freqs[note]
    playKatiNote(note, freq)
    pass
