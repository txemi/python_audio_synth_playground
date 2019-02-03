import math


try:
    from itertools import izip
except ImportError: # Pyt   hon 3
    izip = zip
    xrange = range


def build_data(frequency, duration, volume, sample_rate):
    n_samples = int(sample_rate * duration)
    restframes = n_samples % sample_rate
    s = lambda t: volume * math.sin(2 * math.pi * frequency * t / sample_rate)
    samples = (int(s(t) * 0x7f + 0x80) for t in xrange(n_samples))
    return izip(*[samples] * sample_rate), restframes