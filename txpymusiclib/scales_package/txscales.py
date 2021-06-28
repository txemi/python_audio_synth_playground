from fluentcheck import Check


class TxScaleSt:
    def __init__(self, semitones=None, name=None):
        Check(semitones is not None or name is not None).is_true()
        if semitones is not None:
            if sum(semitones) != 12:
                raise Exception()
        self.semitones = semitones
        self.name = name

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, TxScaleSt):
            return list(self.semitones) == list(other.semitones)
        return False
