class TxMusicalMode:
    def __init__(self, semitones):
        if sum(semitones) != 12:
            raise Exception()
        self.semitones = semitones

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, TxMusicalMode):
            return list(self.semitones) == list(other.semitones)
        return False


blues = TxMusicalMode((3, 2, 1, 1, 3, 2))
doble_armonica = TxMusicalMode((1, 3, 1, 2, 1, 3, 1))
major = TxMusicalMode((2, 2, 1, 2, 2, 2, 1))
minor = TxMusicalMode((2, 1, 2, 2, 1, 2, 2))
phrygian = TxMusicalMode((1, 2, 2, 2, 1, 2, 2))
chromatic = TxMusicalMode((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1))

all = (blues, doble_armonica, major, minor, phrygian, chromatic)
