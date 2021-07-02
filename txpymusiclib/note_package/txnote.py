class TxNote:
    """ For simple list of hardcoded notes and freqs"""

    def __init__(self, khe_name, freq=None):
        self.freq = freq
        self.name = khe_name


note_C3 = TxNote('C3')
note_E3 = TxNote('E3')
note_G3 = TxNote('G3')

note_A = TxNote('A') # default scale
note_A4 = TxNote('A4', 440.0)  # Frequency of Note A4
note_C4 = TxNote('C4', 261.626)  # Middle C
note_G4 = TxNote('G4', 391.996)
note_E4 = TxNote('E4', 329.628)
note_c4 = TxNote('c4')

note_C5 = TxNote('C5')  # C one octave above
