class TxScaleSt:
    def __init__(self, semitones, name=None):
        if sum(semitones) != 12:
            raise Exception()
        self.semitones = semitones
        self.name = name

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, TxScaleSt):
            return list(self.semitones) == list(other.semitones)
        return False
