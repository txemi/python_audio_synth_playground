from beartype import beartype
from fluentcheck import Check


class TxScaleSt:
    @beartype
    def __init__(self, semitones=None, names=None, mode: int = None, alt: str = None):
        try:
            assert isinstance(semitones, (list, tuple, type(None)))
        except:
            raise
        try:
            if names is not None:
                assert isinstance(names, (list, tuple))
                assert len(names) > 0
                try:
                    assert len(names[0]) > 2
                except:
                    raise
        except:
            raise
        Check(semitones is not None or names is not None).is_true()

        if semitones is not None:
            if sum(semitones) != 12:
                raise Exception()
        self.semitones = semitones
        self.names = names
        self.mode = mode
        self.alt = alt

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, TxScaleSt):
            return list(self.semitones) == list(other.semitones)
        return False

    @property
    def name(self):
        return self.names[0]
