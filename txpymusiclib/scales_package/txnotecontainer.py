from typing import Generator

from beartype import beartype
from mingus.containers import Note as MingusNote

from txpymusiclib.note_package import note_freq_khe
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
    def __init__(self, notes: list[str, ...] = None):
        if notes is not None:
            self.notes = mingus_names_to_mingusnotes(notes)
            out = self.get_original()
            if not out == list(notes):
                raise Exception()
        else:
            self.notes = []

    def get_original(self):
        out = [x.name + str(x.octave) for x in self.notes.notes]
        return out

    @beartype
    def get_txnotes(self) -> Generator[TxNote2, None, None]:
        for a in self.notes:
            yield TxNote2(a)
