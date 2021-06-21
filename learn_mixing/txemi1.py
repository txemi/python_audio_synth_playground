from pytheory import TonedScale

from common.play.tx_pytheory_play import print_and_play_tone
from common.filewrite.txwavwrite import write_wav_for_toned_scale


def play_with_scale(note_str):
    ts = TonedScale(tonic=note_str)
    c_minor = ts["major"]
    for tone in c_minor.tones:
        print_and_play_tone(tone)

    write_wav_for_toned_scale(c_minor)


play_with_scale('C4')
print(1)
