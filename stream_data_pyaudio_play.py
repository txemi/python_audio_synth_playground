import pyaudio
from pyaudio import PyAudio


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


def play_2channels_16_bit(frames, rate):
    audio_format = pyaudio.paInt16
    channels = 2
    pyaudio_object: PyAudio = pyaudio.PyAudio()
    stream = pyaudio_object.open(format=audio_format, channels=channels, rate=rate, output=True)
    stream.write(frames)
    stream.stop_stream()
    stream.close()
