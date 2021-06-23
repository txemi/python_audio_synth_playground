import math

import pyaudio
from pyaudio import PyAudio

from common.synt_wave.sample_rates import sample_rate_16000


def play_1channel_8bit(data, restframes, rate):
    pyaudio_object = PyAudio()
    stream = pyaudio_object.open(format=pyaudio_object.get_format_from_width(1),  # 8bit
                                 channels=1,  # mono
                                 rate=rate,
                                 output=True)
    for buf in data:  # write several samples at a time
        stream.write(bytes(bytearray(buf)))

    # fill remainder of frameset with silence
    stream.write(b'\x80' * restframes)

    stream.stop_stream()
    stream.close()
    pyaudio_object.terminate()


def play_1channel_8bit_bis(FREQUENCY):
    PyAudio = pyaudio.PyAudio  # initialize pyaudio

    # See https://en.wikipedia.org/wiki/Bit_rate#Audio
    BITRATE = sample_rate_16000  # number of frames per second/frameset.

    LENGTH = 1  # seconds to play sound

    if FREQUENCY > BITRATE:
        BITRATE = FREQUENCY + 100

    NUMBEROFFRAMES = int(BITRATE * LENGTH)
    RESTFRAMES = NUMBEROFFRAMES % BITRATE
    WAVEDATA = ''

    # generating wawes
    for x in range(NUMBEROFFRAMES):
        WAVEDATA = WAVEDATA + chr(int(math.sin(x / ((BITRATE / FREQUENCY) / math.pi)) * 127 + 128))

    for x in range(RESTFRAMES):
        WAVEDATA = WAVEDATA + chr(128)

    p = PyAudio()
    stream = p.open(format=p.get_format_from_width(1),
                    channels=1,
                    rate=BITRATE,
                    output=True)

    stream.write(WAVEDATA)
    stream.stop_stream()
    stream.close()
    p.terminate()


def play_2channels_16_bit(frames, rate):
    audio_format = pyaudio.paInt16
    channels = 2
    pyaudio_object: PyAudio = pyaudio.PyAudio()
    stream = pyaudio_object.open(format=audio_format, channels=channels, rate=rate, output=True)
    stream.write(frames)
    stream.stop_stream()
    stream.close()
