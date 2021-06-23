from mingus import containers

from txpymusiclib.chords_package import chord_examples


def aa():
    t = containers.Track(containers.Piano())
    b = containers.Bar()
    t + b
    t + "C-4"


def bb():
    t = containers.Track(containers.Piano()).from_chords(chord_examples.NiceChordSeqExample)
    b = list(t.get_notes())
    print(1)


bb()
aa()
print(1)
