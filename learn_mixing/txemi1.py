from pytheory import TonedScale

from common.play.tx_pytheory_play import print_and_play_tone
from common.filewrite.txwavwrite import write_wav_for_toned_scale

c4_note_str = 'C4'


def play_with_scale():
    ts = TonedScale(tonic=c4_note_str)
    c_minor = ts["major"]
    for tone in c_minor.tones:
        print_and_play_tone(tone)

    write_wav_for_toned_scale(c_minor)


play_with_scale()
print(1)
