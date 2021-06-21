import numpy as np
from beartype import beartype

from common import sample_rates


@beartype
def get_sine_wave(frequency: float, duration, sample_rate=sample_rates.sample_rate_44100, amplitude=4096):
    '''
    Get pure sine buildwave.

    Parameters
    ----------
    frequency : float
        Frequency in hertz.
    duration : float
        Time in seconds.
    sample_rate : int, optional
        Wav file sample rate. The default is 44100.
    amplitude : int, optional
        Peak Amplitude. The default is 4096.

    Returns
    -------
    buildwave : TYPE
        DESCRIPTION.

    '''
    t = np.linspace(0, duration, int(sample_rate * duration))
    wave = amplitude * np.sin(2 * np.pi * frequency * t)
    return wave