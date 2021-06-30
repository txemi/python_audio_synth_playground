from typing import Generator

from beartype import beartype
from mingus.containers import Note as MingusNote
from mingus.containers.note_container import NoteContainer

from txpymusiclib.note_package import note_freq_khe
from txpymusiclib.scales_package import scale_mingus
from txpymusiclib.scales_package.scale_mingus import mingus_names_to_mingusnotes


@beartype
def note_mingus_to_khe_name(mingus_name: str):
    if len(mingus_name) == 1:
        return mingus_name
    if len(mingus_name) == 2:
        if mingus_name[1] == '#':
            return mingus_name[0].lower()
    raise NotImplementedError()


class TxNote2:
    def __init__(self, mingusnote: MingusNote):
        self.mingusnote = mingusnote

    def get_freq(self):
        note2freq_mingus = note_freq_khe.get_piano_notes_mingus()
        freq_from_mingus = note2freq_mingus[int(self.mingusnote)]

        if False:
            # We disable this extra check, needs to implement bemols for khe table lookup, perhaps it does not worht
            note_freqs_khe = note_freq_khe.get_piano_notes_khe()
            mingusnote1 = self.mingusnote
            note_mingus_to_khe_name(mingusnote1.name)
            khe_fullname = note_mingus_to_khe_name(mingusnote1.name) + str(mingusnote1.octave)
            try:
                freq_from_khe = note_freqs_khe[khe_fullname]
            except:
                raise

            if freq_from_khe != freq_from_mingus:
                raise Exception()
        return freq_from_mingus


class TxNoteContainer:
    @beartype
    def __init__(self):
        self.build_from_mingus_notes_str(None)

    @beartype
    def build_from_mingus_notes_str(self, notes):
        if notes is not None:
            self.__notes = mingus_names_to_mingusnotes(notes)
            out = self.get_original()
            if not out == list(notes):
                raise Exception()
        else:
            self.__notes = NoteContainer()
        return self

    @beartype
    def get_original(self) -> list:
        out = [x.name + str(x.octave) for x in self.__notes.notes]
        return out

    @beartype
    def get_txnotes(self) -> Generator[TxNote2, None, None]:
        for a in self.__notes:
            yield TxNote2(a)

    @property
    def notes(self):
        if not isinstance(self.__notes, NoteContainer):
            print(1)
        assert isinstance(self.__notes, NoteContainer)
        return self.__notes

    @notes.setter
    def notes(self, var):
        if not isinstance(var, NoteContainer):
            print(1)
        assert isinstance(var, NoteContainer)
        self.__notes = var

    @beartype
    def append(self, a: MingusNote):
        self.__notes.add_note(a)

    def build_from_mingus_scale(self, mingus_tal):
        bbb = scale_mingus.mingus_scale_to_notes(mingus_tal)
        for aaa in bbb:
            raise NotImplementedError()
        self.__notes = bbb
        return self
