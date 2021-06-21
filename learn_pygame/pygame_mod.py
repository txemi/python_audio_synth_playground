import pygame.sndarray

from common.buildwave.pygame_wave import sine_wave, square_wave
from common.play.pygame_play import play_for
from common.sample_rates import sample_rate_2
from common.freq import TxTones
pygame.mixer.init(frequency=sample_rate_2, size=-16, channels=1, buffer=4096)
#pygame.mixer.Sound.set_volume(1.0)

# Play A (440Hz) for 1 second as a sine buildwave:
play_for(sine_wave(TxTones.A4_freq, 4096), 1000)

# Play A-440 for 1 second as a square buildwave:
play_for(square_wave(TxTones.A4_freq, 4096), 1000)
