from typing import Union

from beartype import beartype

from txpymusiclib.play.from_pyaudio import play_1channel_8bit, play_2channels_16_bit
from txpymusiclib.synt_wave import sample_rates
from txpymusiclib.synt_wave.from_math import build_sin_data_for_freq_1, build_sin_data_for_freq_2
from txpymusiclib.synt_wave.sample_rates import DEFAULTRATE


@beartype
def sine_tone_play1(frequency, duration, volume=1, sample_rate=sample_rates.sample_rate_22050):
    data, restframes = build_sin_data_for_freq_1(volume=volume, duration=duration, frequency=frequency,
                                                 sample_rate=sample_rate)
    play_1channel_8bit(data, restframes, sample_rate)


@beartype
def sin_tone_play_2(frequency: Union[float, int], time: Union[float, int]):
    """
    play a frequency for a fixed time!
    """

    rate = DEFAULTRATE

    frames = build_sin_data_for_freq_2(frequency, time=time, rate=rate)
    play_2channels_16_bit(frames, rate=rate)
