import txpymusiclib

c_major_scale = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']
# TODO: use object when possible
c_major_scale_notes = list(txpymusiclib.scales_package.scale_mingus.mingus_names_to_notes(
    txpymusiclib.scales_package.scale_static_examples_from_note_names.c_major_scale))
