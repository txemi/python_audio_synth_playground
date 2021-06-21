from beartype import beartype
from common import txintervals


# Python to convert a string note (eg. "A4") to a frequency (eg. 440).
# Inspired by https://gist.github.com/stuartmemo/3766449


class TxTones:
    A4_freq = 440.0 # Frequency of Note A4


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
    return a.replace("a", "A#").replace("c", "C#").replace("d", "D#").replace("f", "F#").replace("g", "G#")