from common import utils
from common.play.tx_pytheory_play import playKatiNote

note_freqs = utils.get_piano_notes()

for a in note_freqs:
    if not a:
        continue
    b=note_freqs[a]
    playKatiNote(a, b)
    pass
