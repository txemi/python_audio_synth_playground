# https://github.com/yuma-m/synthesizer
from common.note_package.note_names_and_freq_static import TxTones
from common.play.from_syntetizer import play_init, play_wave

player, synthesizer_instance = play_init()

play_wave(player, synthesizer_instance, TxTones.A4_freq, 1.0)


