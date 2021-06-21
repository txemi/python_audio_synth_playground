from pytheory import Tone
from common import utils
from common.play import tx_pytheory_play
from common.txtones import katieshiqihe2pytheory

note_freqs = utils.get_piano_notes()

for a in note_freqs:
    if not a:
        continue
    b=note_freqs[a]
    print(a+":"+str(b))
    e= katieshiqihe2pytheory(a)
    c=Tone.from_string(e)
    tx_pytheory_play.print_and_play_tone(c)
    pass
