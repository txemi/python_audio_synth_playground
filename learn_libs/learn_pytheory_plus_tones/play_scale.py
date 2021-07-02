from pytheory import TonedScale

from txpymusiclib.note_package import txnote
from txpymusiclib.play.from_pytheory import print_and_play_tone
from txpymusiclib.wavfile_write.from_tones_mixer import write_wav_for_toned_scale


def play_with_scale(note_str):
    ts = TonedScale(tonic=note_str)
    c_minor = ts["major"]
    for tone in c_minor.tones:
        print_and_play_tone(tone)

    write_wav_for_toned_scale(c_minor)


play_with_scale(txnote.note_C4.name)
print(1)
