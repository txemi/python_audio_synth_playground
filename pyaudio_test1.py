#!/usr/bin/env python
"""Play a fixed frequency sound."""
from __future__ import division

from tone_play import sine_tone_play1
from stream_data_for_freq import la_note_frec

if __name__ == "__main__":
    sine_tone_play1(
        # see http://www.phy.mtu.edu/~suits/notefreqs.html
        frequency=la_note_frec,  # Hz, waves per second A4
        duration=3.21,  # seconds to play sound
        volume=.01,  # 0..1 how loud it is
        # see http://en.wikipedia.org/wiki/Bit_rate#Audio
        sample_rate=22050  # number of samples per second
    )
