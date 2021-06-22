from common.synt_wave.from_numpy import sine_wave, square_wave
from common.sample_rates import sample_rate_4096
from common.play.from_pygame import play_for, pygame_mixer_init
from common.txtone import TxTones

pygame_mixer_init()

# Play A (440Hz) for 1 second as a sine wave:
play_for(sine_wave(TxTones.A4_freq, sample_rate_4096), 1000)

# Play A-440 for 1 second as a square wave:
play_for(square_wave(TxTones.A4_freq, sample_rate_4096), 1000)
