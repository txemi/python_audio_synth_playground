import time

from txpymusiclib.interval_package.txintervals import TxIntervals
from txpymusiclib.note_package import note_names_and_freq_static
from txpymusiclib.play import synt_with_math_and_play_with_pyaudio


def octave_play(tone_freq):
    for tone_freq in tone_freq / 2, tone_freq, tone_freq * 2:
        synt_with_math_and_play_with_pyaudio.sin_tone_play_2(tone_freq, 1)


def scale1_fifth_play(nota):
    synt_with_math_and_play_with_pyaudio.sin_tone_play_2(nota, 1)
    synt_with_math_and_play_with_pyaudio.sin_tone_play_2(nota * TxIntervals.fifth_factor_rational, 1)


def scale2_fifth_play(tone_freq):
    new_tone_freq = tone_freq * TxIntervals.get_fifth_factor_non_rational()
    synt_with_math_and_play_with_pyaudio.sin_tone_play_2(tone_freq, 1)
    synt_with_math_and_play_with_pyaudio.sin_tone_play_2(new_tone_freq, 1)


def compare_fifth():
    a = TxIntervals.get_fifth_factor_non_rational()
    b = TxIntervals.fifth_factor_rational
    print(1)


def play_intervals(tone_freq):
    compare_fifth()
    octave_play(tone_freq)
    time.sleep(1)
    scale1_fifth_play(tone_freq)
    time.sleep(1)
    scale2_fifth_play(tone_freq)


if __name__ == "__main__":
    play_intervals(note_names_and_freq_static.note_A4.freq)
