#!/usr/bin/env python
"""Play a fixed frequency sound."""
from __future__ import division

from learn_pyaudio.pyaudio_tone_play import sine_tone_play1
from learn_pyaudio.stream_data_for_freq import A_note_frec

if __name__ == "__main__":
    sine_tone_play1(
        # see http://www.phy.mtu.edu/~suits/notefreqs.html
        frequency=A_note_frec,  # Hz, waves per second A4
        duration=3.21,  # seconds to play sound
        volume=.01,  # 0..1 how loud it is
        # see http://en.wikipedia.org/wiki/Bit_rate#Audio
        sample_rate=22050  # number of samples per second
    )
