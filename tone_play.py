from stream_data_for_freq import DEFAULTRATE
from stream_data_for_freq import build_data_for_freq_1, build_data_for_freq_2
from stream_data_pyaudio_play import play1, play2


def sine_tone_play1(frequency, duration, volume=1, sample_rate=22050):
    data, restframes = build_data_for_freq_1(volume=volume, duration=duration, frequency=frequency,
                                             sample_rate=sample_rate)
    play1(data, restframes, sample_rate)


def sin_tone_play_2(frequency: float, time: float):
    """
    play a frequency for a fixed time!
    """

    rate = DEFAULTRATE

    frames = build_data_for_freq_2(frequency, time=time, rate=rate)
    play2(frames, rate=rate)
