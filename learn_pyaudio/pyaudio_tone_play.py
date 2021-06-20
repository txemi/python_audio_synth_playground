from learn_pyaudio.stream_data_for_freq import DEFAULTRATE
from learn_pyaudio.stream_data_for_freq import build_data_for_freq_1, build_data_for_freq_2
from learn_pyaudio.stream_data_pyaudio_play import play_1channel_8bit, play_2channels_16_bit


def sine_tone_play1(frequency, duration, volume=1, sample_rate=22050):
    data, restframes = build_data_for_freq_1(volume=volume, duration=duration, frequency=frequency,
                                             sample_rate=sample_rate)
    play_1channel_8bit(data, restframes, sample_rate)


def sin_tone_play_2(frequency: float, time: float):
    """
    play a frequency for a fixed time!
    """

    rate = DEFAULTRATE

    frames = build_data_for_freq_2(frequency, time=time, rate=rate)
    play_2channels_16_bit(frames, rate=rate)
