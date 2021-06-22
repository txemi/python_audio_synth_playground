#!/usr/bin/env python
"""Play a fixed frequency sound."""
from __future__ import division

from common.play.synt_with_math_and_play_with_pyaudio import sine_tone_play1
from common.txtone import TxTones
from common.sample_rates import sample_rate_22050

if __name__ == "__main__":
    sine_tone_play1(
        # see http://www.phy.mtu.edu/~suits/notefreqs.html
        frequency=TxTones.A4_freq,  # Hz, waves per second A4
        duration=3.21,  # seconds to play sound
        volume=.01,  # 0..1 how loud it is
        # see http://en.wikipedia.org/wiki/Bit_rate#Audio
        sample_rate=sample_rate_22050  # number of samples per second
    )
