from common.play import synt_with_math_and_play_with_pyaudio
from common.txtone import TxTones
from common.txintervals import TxIntervals

import time
def octave_play(tone_freq):
    for tone_freq in tone_freq / 2, tone_freq, tone_freq * 2:
        synt_with_math_and_play_with_pyaudio.sin_tone_play_2(tone_freq, 1)


def scale1_fifth_play(nota):
    synt_with_math_and_play_with_pyaudio.sin_tone_play_2(nota, 1)
    synt_with_math_and_play_with_pyaudio.sin_tone_play_2(nota * TxIntervals.fifth_1, 1)


def scale2_fifth_play(tone_freq):
    new_tone_freq = tone_freq * TxIntervals.get_fifth_factor_2()
    synt_with_math_and_play_with_pyaudio.sin_tone_play_2(tone_freq, 1)
    synt_with_math_and_play_with_pyaudio.sin_tone_play_2(new_tone_freq, 1)


def play_intervals(tone_freq):
    octave_play(tone_freq)
    time.sleep(1)
    scale1_fifth_play(tone_freq)
    time.sleep(1)
    scale2_fifth_play(tone_freq)


if __name__ == "__main__":
    play_intervals(TxTones.A4_freq)
