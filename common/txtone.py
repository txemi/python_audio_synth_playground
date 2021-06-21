import numpy as np
from beartype import beartype
from common import txintervals


# Python to convert a string note (eg. "A4") to a frequency (eg. 440).
# Inspired by https://gist.github.com/stuartmemo/3766449


class TxTones:
    A4_freq = 440.0 # Frequency of Note A4
    A4 = ["A4"]


@beartype
def getFrequency(note:str, A4=TxTones.A4_freq):
    notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

    octave = int(note[2]) if len(note) == 3 else int(note[1])

    keyNumber = notes.index(note[0:-1])

    off = 12 if (keyNumber < 3) else 0

    keyNumber = keyNumber + off + ((octave - 1) * 12) + 1

    return A4 * 2 ** ((keyNumber - 49) / 12)


@beartype
def katieshiqihe2pytheory(a: str):
    """ katie code use lowercase for black keys """
    return a.replace("a", "A#").replace("c", "C#").replace("d", "D#").replace("f", "F#").replace("g", "G#")


def _get_key_freq(n):
    base_freq = TxTones.A4_freq  # Frequency of Note A4
    return 2 ** ((n + 1 - 49) / 12) * base_freq


def _get_piano_keys():
    # White keys are in Uppercase and black keys (sharps) are in lowercase
    octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B']
    keys = np.array([x + str(y) for y in range(0, 9) for x in octave])
    # Trim to standard 88 keys
    start = np.where(keys == 'A0')[0][0]
    end = np.where(keys == 'C8')[0][0]
    keys = keys[start:end + 1]
    return keys


def get_piano_notes():
    '''
    Get the frequency in hertz for all keys on a standard piano.

    Returns
    -------
    note_freqs : dict
        Mapping between note name and corresponding frequency.

    '''
    keys = _get_piano_keys()
    note_freqs = dict(zip(keys, [_get_key_freq(n) for n in range(len(keys))]))
    note_freqs[''] = 0.0  # stop
    return note_freqs