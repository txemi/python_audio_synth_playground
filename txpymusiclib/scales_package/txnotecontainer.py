from typing import Generator

from beartype import beartype
from mingus import core as mingus_core
from mingus.containers import Note as MingusNote
from mingus.containers.note_container import NoteContainer

from txpymusiclib.note_package.txnote_mingus_wrap import TxNoteMingusWrap
from txpymusiclib.scales_package.scale_mingus import mingus_names_to_mingusnotes, mingus_scale_to_container


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
        out = [x.khe_name + str(x.octave) for x in self.__notes.notes]
        return out

    @beartype
    def get_txnotes(self) -> Generator[TxNoteMingusWrap, None, None]:
        for a in self.__notes:
            yield TxNoteMingusWrap(a)

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

    @beartype
    def build_from_mingus_scale(self, mingus_tal: mingus_core.scales._Scale):
        container = mingus_scale_to_container(mingus_tal)
        self.__notes = container
        return self
