import time
from typing import Union

from beartype import beartype
from mingus.core import progressions

from txpymusiclib.play import play_mingus_in_synthesizer


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
