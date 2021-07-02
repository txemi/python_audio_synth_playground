from txpymusiclib.note_package import note_freq_khe
from txpymusiclib.play.from_pytheory import print_and_play_khe_tone_from_name_and_freq

note_freqs = note_freq_khe.get_piano_note_to_freq_map_from_khe_names()

for note in note_freqs:
    if not note:
        continue
    freq = note_freqs[note]
    print_and_play_khe_tone_from_name_and_freq(note, freq)
    pass
