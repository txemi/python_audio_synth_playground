class TxNoteKheWrap:
    """ For simple list of hardcoded notes and freqs"""

    def __init__(self, khe_name, freq=None):
        self.freq = freq
        self.khe_name = khe_name

    def get_octave(self):
        return int(self.khe_name[-1:])


note_C3 = TxNoteKheWrap('C3')
note_E3 = TxNoteKheWrap('E3')
note_G3 = TxNoteKheWrap('G3')

note_A = TxNoteKheWrap('A') # default scale
note_A4 = TxNoteKheWrap('A4', 440.0)  # Frequency of Note A4
note_C4 = TxNoteKheWrap('C4', 261.626)  # Middle C
note_G4 = TxNoteKheWrap('G4', 391.996)
note_E4 = TxNoteKheWrap('E4', 329.628)
note_c4 = TxNoteKheWrap('c4')

note_C5 = TxNoteKheWrap('C5')  # C one octave above
