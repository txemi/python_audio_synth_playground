#!/usr/bin/env python3
import pyaudio

from pyaudio import PyAudio

from stream_data import data_for_freq

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

p: PyAudio = pyaudio.PyAudio()


def play(frequency: float, time: float):
    """
    play a frequency for a fixed time!
    """
    frames = data_for_freq(frequency, time=time, RATE=RATE)
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True)
    stream.write(frames)
    stream.stop_stream()
    stream.close()


if __name__ == "__main__":
    play(400, 1)