# https://github.com/yuma-m/synthesizer
from common.note_package import note_names_and_freq_static
from common.play import from_syntetizer

player, synthesizer_instance = from_syntetizer.play_init()
from_syntetizer.play_wave(player, synthesizer_instance, note_names_and_freq_static.note_A4.freq, 1.0)
