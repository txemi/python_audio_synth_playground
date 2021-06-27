#!/usr/bin/env python
"""Play a fixed frequency sound."""
from __future__ import division

from txpymusiclib.play.synt_with_math_and_play_with_pyaudio import sine_tone_play1
from txpymusiclib.note_package import note_names_and_freq_static
from txpymusiclib.synt_wave.sample_rates import sample_rate_22050

if __name__ == "__main__":
    sine_tone_play1(
        # see http://www.phy.mtu.edu/~suits/notefreqs.html
        frequency=note_names_and_freq_static.note_A4.freq,  # Hz, waves per second A4
        duration=3.21,  # seconds to play sound
        volume=.01,  # 0..1 how loud it is
        # see http://en.wikipedia.org/wiki/Bit_rate#Audio
        sample_rate=sample_rate_22050  # number of samples per second
    )
