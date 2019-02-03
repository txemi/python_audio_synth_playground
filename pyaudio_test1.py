#!/usr/bin/env python
"""Play a fixed frequency sound."""
from __future__ import division

from stream_data import build_data
from stream_tone_play import play1


def sine_tone(frequency, duration, volume=1, sample_rate=22050):
    data, restframes = build_data(volume=volume, duration=duration, frequency=frequency, sample_rate=sample_rate)
    play1(data, restframes, sample_rate)


if __name__ == "__main__":
    sine_tone(
        # see http://www.phy.mtu.edu/~suits/notefreqs.html
        frequency=440.00,  # Hz, waves per second A4
        duration=3.21,  # seconds to play sound
        volume=.01,  # 0..1 how loud it is
        # see http://en.wikipedia.org/wiki/Bit_rate#Audio
        sample_rate=22050  # number of samples per second
    )
