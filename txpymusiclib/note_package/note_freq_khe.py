import numpy as np
from beartype import beartype

from txpymusiclib.note_package import txnote
from txpymusiclib.note_package.note_convert_mingus import note_name_str_2_mingus_note_int
from txpymusiclib.note_package.note_convert_khe import note_khe_to_sci


@beartype
def get_frequency(note: str, note_freq=txnote.note_A4.freq):
    notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

    octave = int(note[2]) if len(note) == 3 else int(note[1])

    key_number = notes.index(note[0:-1])

    off = 12 if (key_number < 3) else 0

    key_number = key_number + off + ((octave - 1) * 12) + 1

    return note_freq * 2 ** ((key_number - 49) / 12)


def _get_key_freq(n):
    base_freq = txnote.note_A4.freq  # Frequency of Note A4
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


@beartype
def get_piano_notes_khe() -> dict[str, float]:
    """
    Get the frequency in hertz for all keys on a standard piano.

    Returns
    -------
    note_freqs : dict
        Mapping between note name and corresponding frequency.

    """
    keys = _get_piano_keys()
    note_freqs = dict(zip(keys, [_get_key_freq(n) for n in range(len(keys))]))
    note_freqs[''] = 0.0  # stop
    return note_freqs


def get_piano_notes_sci():
    old_dict = get_piano_notes_khe()
    new_dict = {}
    for old_key in old_dict:
        if old_key == '':
            continue
        new_dict[note_khe_to_sci(old_key)] = old_dict[old_key]

    return new_dict


def get_piano_notes_mingus():
    old_dict = get_piano_notes_khe()
    new_dict1111 = {}
    for old_key in old_dict:
        if old_key == '':
            continue
        mingus_note_int = note_name_str_2_mingus_note_int(old_key)
        assert mingus_note_int not in new_dict1111
        new_dict1111[mingus_note_int] = old_dict[old_key]

    return new_dict1111
