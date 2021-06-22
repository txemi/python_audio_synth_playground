import math
import struct
from beartype import beartype

from common.sample_rates import DEFAULTRATE
from typing import Union

try:
    from itertools import izip
except ImportError:  # Python 3
    izip = zip
    xrange = range


@beartype
def build_sin_data_for_freq_1(frequency, duration, volume, sample_rate):
    n_samples = int(sample_rate * duration)
    restframes = n_samples % sample_rate
    s = lambda t: volume * math.sin(2 * math.pi * frequency * t / sample_rate)
    samples = (int(s(t) * 0x7f + 0x80) for t in xrange(n_samples))
    return izip(*[samples] * sample_rate), restframes


@beartype
def build_sin_data_for_freq_2(frequency: Union[float, int], time: Union[float, int] = None, rate=DEFAULTRATE):
    """get frames for a fixed frequency for a specified time or
    number of frames, if frame_count is specified, the specified
    time is ignored"""
    frame_count = int(rate * time)

    remainder_frames = frame_count % rate
    wavedata = []

    for i in range(frame_count):
        a = rate / frequency  # number of frames per wave
        b = i / a
        # explanation for b
        # considering one wave, what part of the wave should this be
        # if we graph the sine wave in a
        # displacement vs i graph for the particle
        # where 0 is the beginning of the sine wave and
        # 1 the end of the sine wave
        # which part is "i" is denoted by b
        # for clarity you might use
        # though this is redundant since math.sin is a looping function
        # b = b - int(b)

        c = b * (2 * math.pi)
        # explanation for c
        # now we map b to between 0 and 2*math.PI
        # since 0 - 2*PI, 2*PI - 4*PI, ...
        # are the repeating domains of the sin wave (so the decimal values will
        # also be mapped accordingly,
        # and the integral values will be multiplied
        # by 2*PI and since sin(n*2*PI) is zero where n is an integer)
        d = math.sin(c) * 32767
        e = int(d)
        wavedata.append(e)

    for i in range(remainder_frames):
        wavedata.append(0)

    number_of_bytes = str(len(wavedata))
    wavedata = struct.pack(number_of_bytes + 'h', *wavedata)

    return wavedata
