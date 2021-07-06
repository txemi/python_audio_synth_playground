from mingus import containers as mingus_containers

from txpymusiclib.chords_package import chord_progression_examples


def aa():
    t = mingus_containers.Track(mingus_containers.Piano())
    b = mingus_containers.Bar()
    t + b
    t + "C-4"


def bb():
    t = mingus_containers.Track(mingus_containers.Piano()).from_chords(chord_progression_examples.NiceChordSeqExample)
    b = list(t.get_notes())
    print(1)


bb()
aa()
print(1)
