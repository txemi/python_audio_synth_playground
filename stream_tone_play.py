import pyaudio
from pyaudio import PyAudio


def play1(data, restframes, sample_rate):
    p = PyAudio()
    stream = p.open(format=p.get_format_from_width(1),  # 8bit
                    channels=1,  # mono
                    rate=sample_rate,
                    output=True)
    for buf in data:  # write several samples at a time
        stream.write(bytes(bytearray(buf)))

    # fill remainder of frameset with silence
    stream.write(b'\x80' * restframes)

    stream.stop_stream()
    stream.close()
    p.terminate()


def play2(frames, RATE):
    FORMAT = pyaudio.paInt16
    CHANNELS = 2

    p: PyAudio = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True)
    stream.write(frames)
    stream.stop_stream()
    stream.close()