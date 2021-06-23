from mingus.containers import Piano

p=Piano()
rr=p.range
loil=rr[0]

for c3_major_chord_mingus in rr:
    print(c3_major_chord_mingus)

loil.augment()