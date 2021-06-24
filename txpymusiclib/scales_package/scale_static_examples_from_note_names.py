from mingus.containers.note import Note

from txpymusiclib.note_package import note_freq_funcs
from txpymusiclib.note_package.note_freq_funcs import get_piano_notes_khe
from txpymusiclib.scales_package.scale_mingus import mingus_names_to_notes


class TxNote2:
    def __init__(self, mingusnote: Note):
        self.mingusnote = mingusnote

    def get_freq(self):
        note_freqs = get_piano_notes_khe()
        x = self.mingusnote
        nameeeee = x.name + str(x.octave)
        frequencies = note_freqs[nameeeee]

        note2freq = note_freq_funcs.get_piano_notes_mingus()
        freqs = note2freq[int(self.mingusnote)]

        if frequencies != freqs:
            raise Exception()
        return freqs


class TxNoteContainer:
    def __init__(self, notes: list[str, ...]):
        self.notes = mingus_names_to_notes(notes)
        out = self.get_original()
        if not out == notes:
            raise Exception()

    def get_original(self):
        out = [x.name + str(x.octave) for x in self.notes.notes]
        return out

    def get_txnotes(self):
        for a in self.notes:
            yield TxNote2(a)


c_major_scale_notes_2 = TxNoteContainer('C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5')
