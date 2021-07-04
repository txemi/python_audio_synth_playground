from typing import Generator

from beartype import beartype
from mingus import core as mingus_core
from mingus.containers import Note as MingusNote
from mingus.containers.note_container import NoteContainer

from txpymusiclib.note_package.txnote_mingus_wrap import TxNoteMingusWrap
from txpymusiclib.scales_package.scale_mingus import mingus_scale_to_container, _mingus_names_to_notes


class TxNoteContainer:
    # FIXME: no me sirve Mingus NoteContainer ya que las ordena y no es lo que quiero
    @beartype
    def __init__(self):
        self.build_from_mingus_notes_str(None)

    @beartype
    def build_from_mingus_notes_str(self, notes):
        if notes is not None:
            self.__notes = list(_mingus_names_to_notes(notes))
            out = self.get_original()
            if not out == list(notes):
                raise Exception()
        else:
            self.__notes = []
        return self

    @beartype
    def build_from_mingus_notes(self, notes):
        self.__notes = []
        for note in notes:
            assert isinstance(note, MingusNote)
            self.__notes.append(note)
        return self

    @beartype
    def get_original(self) -> list:
        out = [x.name + str(x.octave) for x in self.__notes]
        return out

    @beartype
    def get_txnotes(self) -> Generator[TxNoteMingusWrap, None, None]:
        for a in self.__notes:
            yield TxNoteMingusWrap(a)

    @property
    def notes(self):
        raise NotImplementedError("ya no funciona, no usamos notecontainer porque ordenaba")
        if not isinstance(self.__notes, NoteContainer):
            print(1)
        assert isinstance(self.__notes, NoteContainer)
        return self.__notes

    def get_mingus_note_list(self):
        return self.__notes

    @notes.setter
    def notes(self, var):
        raise NotImplementedError("ya no funciona, no usamos notecontainer porque ordenaba")
        if not isinstance(var, NoteContainer):
            print(1)
        assert isinstance(var, NoteContainer)
        self.__notes = var

    @beartype
    def append(self, mingus_note: MingusNote):
        self.__notes.append(mingus_note)

    def append_all(self, mingus_notes: list[MingusNote]):
        self.__notes.extend(mingus_notes)

    @beartype
    def build_from_mingus_scale(self, mingus_scale: mingus_core.scales._Scale, octave: int):
        container = mingus_scale_to_container(mingus_scale, octave=octave)
        self.__notes = container.notes
        return self
