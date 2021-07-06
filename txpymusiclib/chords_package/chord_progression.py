import time
from typing import Union

from beartype import beartype
from mingus.core import progressions

import txpymusiclib.play
from txpymusiclib.play import play_mingus_in_synthesizer


class TxChordPogression:
    def __init__(self):
        self.__roman = None
        self.__name = None

    @beartype
    def from_roman(self, lala: Union[list, tuple]):
        self.__roman = lala
        return self

    def with_name(self, name):
        self.__name = name
        return self

    @beartype
    def progression_test(self):
        progression1 = self.__roman
        print(progression1)
        key = "C"
        chords1 = progressions.to_chords(progression1, key=key)
        if self.__name is not None:
            print(self.__name)
        print(chords1)
        back_to_progression = progressions.determine(chords1, key=key, shorthand=True)
        print(back_to_progression)
        back_to_progression_shorthand = progressions.determine(chords1, key=key, shorthand=False)
        print(back_to_progression_shorthand)
        subtitution = progressions.substitute(progression1, 0)

        play_mingus_in_synthesizer.play_progressions(self.__roman)
        time.sleep(1.0)
        txpymusiclib.play.play_mingus_in_synthesizer.play_progressions(back_to_progression)
        time.sleep(1.0)
        print('\n')