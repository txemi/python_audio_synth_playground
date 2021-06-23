# https://github.com/yuma-m/synthesizer
from common.note_package import note_names_and_freq_static
from common.play.from_syntetizer import play_init, play_wave

player, synthesizer_instance = play_init()

play_wave(player, synthesizer_instance, note_names_and_freq_static.note_A4.freq, 1.0)


