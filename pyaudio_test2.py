#!/usr/bin/env python3

from stream_data import data_for_freq
from stream_tone_play import play2


def play(frequency: float, time: float):
    """
    play a frequency for a fixed time!
    """

    RATE = 44100

    frames = data_for_freq(frequency, time=time, RATE=RATE)
    play2(frames, RATE=RATE)


if __name__ == "__main__":
    play(400, 1)
