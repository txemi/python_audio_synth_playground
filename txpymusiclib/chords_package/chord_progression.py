import time
from typing import Union

import mingus.containers.note_container
from beartype import beartype
from mingus.core import progressions
from mingus.core import progressions as mingus_progressions

from txpymusiclib.chords_package import chord_conversion
from txpymusiclib.play import play_mingus_in_synthesizer


def culo1(chord):
    assert isinstance(chord, mingus.containers.note_container.NoteContainer)
    uuu = chord.get_note_names()
    aaaa3 = mingus_progressions.determine(uuu, key='C', shorthand=True)
    return aaaa3


def culo(chords):
    aaa11 = list(chord_conversion.mingus_chords_to_note_containers(list(chords)))
    for uu in aaa11:
        yield culo1(uu)


class TxChordPogression:
    def __init__(self):
        self.__roman = None
        self.__name = None
        self.__chords = None

    @beartype
    def from_roman(self, lala: Union[list, tuple]):
        self.__roman = lala
        return self

    @beartype
    def from_chords(self, lala):
        self.__chords = lala
        return self

    @beartype
    def with_name(self, name):
        self.__name = name
        return self

    @beartype
    def progression_test(self):
        if self.__name is not None:
            print(self.__name)
        if self.__roman is None:
            print(self.__chords)
            play_mingus_in_synthesizer.play_chords_loop_chord_notation(self.__chords, times=1)
            aaa = list(culo(self.__chords))
            print(aaa)
        else:
            print(self.__roman)
            key = "C"
            chords1 = progressions.to_chords(self.__roman, key=key)

            print(chords1)
            back_to_progression = progressions.determine(chords1, key=key, shorthand=True)
            print(back_to_progression)
            back_to_progression_shorthand = progressions.determine(chords1, key=key, shorthand=False)
            print(back_to_progression_shorthand)
            subtitution = progressions.substitute(self.__roman, 0)

            play_mingus_in_synthesizer.play_progressions_roman(self.__roman)
            time.sleep(1.0)
            play_mingus_in_synthesizer.play_progressions_roman(back_to_progression)
            time.sleep(1.0)
        print('\n')
