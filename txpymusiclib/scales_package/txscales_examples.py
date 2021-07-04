from txpymusiclib.scales_package.txscales import TxScaleSt

# https://www.offtonic.com/theory/book/7-4.html

major = TxScaleSt(semitones=(2, 2, 1, 2, 2, 2, 1), names=('major', 'ionian'), mode=1, alt="natural")
dorian = TxScaleSt(names=("dorian",), mode=2, alt="#6")
phrygian = TxScaleSt(semitones=(1, 2, 2, 2, 1, 2, 2), names=('phrygian',), mode=3, alt="b2")
lydian = TxScaleSt(names=('lydian',), mode=4, alt="#2")
mixolydian = TxScaleSt(names=('mixolydian',), mode=5, alt="b7")
minor = TxScaleSt(semitones=(2, 1, 2, 2, 1, 2, 2), names=('minor', 'aeolian'), mode=6, alt="natural")
locrian = TxScaleSt(names=('locrian',), mode=7, alt="b2 b5")  # not used

blues = TxScaleSt(semitones=(3, 2, 1, 1, 3, 2), names=("blues",))
doble_armonica = TxScaleSt(semitones=(1, 3, 1, 2, 1, 3, 1), names=('doble_armonica',))
chromatic = TxScaleSt(semitones=(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), names=("chromatic",))

all = (major, dorian, phrygian, lydian, mixolydian, minor, locrian, blues, doble_armonica, chromatic)


def find_scale_by_name(scale_name: str):
    for current_scale in all:
        if scale_name in current_scale.names:
            yield current_scale


def single(mylist):
    assert len(mylist) == 1
    return mylist[0]


def find_scale_by_name_unique(scale_name: str) -> TxScaleSt:
    return single(list(find_scale_by_name(scale_name)))
