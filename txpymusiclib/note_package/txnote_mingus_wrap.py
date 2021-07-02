from mingus.containers import Note as MingusNote

from txpymusiclib.note_package import note_freq_khe
from txpymusiclib.note_package.note_convert_khe import note_mingus_to_khe_name


class TxNoteMingusWrap:
    def __init__(self, mingusnote: MingusNote):
        self.mingusnote = mingusnote

    def get_freq(self):
        note2freq_mingus = note_freq_khe.get_piano_note_mingus_int_code_to_freq_map()
        freq_from_mingus = note2freq_mingus[int(self.mingusnote)]

        if False:
            # We disable this extra check, needs to implement bemols for khe table lookup, perhaps it does not worth it
            note_freqs_khe = note_freq_khe.get_piano_note_to_freq_map_from_khe_names()
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