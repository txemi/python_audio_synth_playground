from txpymusiclib.scales_package.txscales import TxScaleSt

blues = TxScaleSt(semitones=(3, 2, 1, 1, 3, 2))
doble_armonica = TxScaleSt((1, 3, 1, 2, 1, 3, 1))
major = TxScaleSt((2, 2, 1, 2, 2, 2, 1), name='major')
minor = TxScaleSt((2, 1, 2, 2, 1, 2, 2), name='minor')
phrygian = TxScaleSt((1, 2, 2, 2, 1, 2, 2), name='phrygian')
chromatic = TxScaleSt((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1))
ionian = TxScaleSt(name='ionian')

all = (blues, doble_armonica, major, minor, phrygian, chromatic)
