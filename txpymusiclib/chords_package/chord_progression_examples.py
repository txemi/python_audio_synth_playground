from txpymusiclib.chords_package.chord_progression import TxChordPogression

# la menor, do mayor , mi mayor, fa mayor


NiceChordSeqExample = ('Am', 'CM', 'EM', 'FM')  # la menor, do mayor, mi mayor, fa mayor
LordOfRings = ('CM', 'Em', 'FM', 'CM', 'FM', 'GM', 'CM', 'GM')

chord_progression_example_1 = TxChordPogression().from_roman(("I", 'V', 'I'))
chord_progression_examples = (
    TxChordPogression().from_chords(NiceChordSeqExample).with_name("NiceChordSeqExample"),
    TxChordPogression().from_chords(LordOfRings).with_name("LordOfRings"),
    chord_progression_example_1,
    TxChordPogression().from_roman(("VI", "III", "IV", "V")),
    TxChordPogression().from_roman(["I", "bIV", "VIIdim7"]).with_name("bad example"),
    TxChordPogression().from_roman(["I", "IV", "V", "I"]),
    TxChordPogression().from_roman(("VI", "IV", "I", "V")),
    TxChordPogression().from_roman(("I", "V", "VI", "IV")),
    TxChordPogression().from_roman(("IV", "VI", "I", "V")),
    TxChordPogression().from_roman(("IV", "V", "VI", "V")),
    TxChordPogression().from_roman(("IV", "V", "VI", "I")),
    TxChordPogression().from_roman(("IV", "V", "VI", "III")),
    TxChordPogression().from_roman(("VI", "III", "IV", "V")),
    TxChordPogression().from_roman(("VI", "III", "I", "V")),
    TxChordPogression().from_roman(("I", "II", "VI", "IV")),
    TxChordPogression().from_roman(("VI", "II", "IV", "V")))
