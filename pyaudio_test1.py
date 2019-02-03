#!/usr/bin/env python
"""Play a fixed frequency sound."""
from __future__ import division

from pyaudio import PyAudio  # sudo apt-get install python{,3}-pyaudio

from stream_data import build_data


def sine_tone(frequency, duration, volume=1, sample_rate=22050):
    p = PyAudio()
    stream = p.open(format=p.get_format_from_width(1),  # 8bit
                    channels=1,  # mono
                    rate=sample_rate,
                    output=True)
    data, restframes = build_data(volume=volume, duration=duration, frequency=frequency, sample_rate=sample_rate)
    for buf in data:  # write several samples at a time
        stream.write(bytes(bytearray(buf)))

    # fill remainder of frameset with silence
    stream.write(b'\x80' * restframes)

    stream.stop_stream()
    stream.close()
    p.terminate()


if __name__ == "__main__":
    sine_tone(
        # see http://www.phy.mtu.edu/~suits/notefreqs.html
        frequency=440.00,  # Hz, waves per second A4
        duration=3.21,  # seconds to play sound
        volume=.01,  # 0..1 how loud it is
        # see http://en.wikipedia.org/wiki/Bit_rate#Audio
        sample_rate=22050  # number of samples per second
    )
