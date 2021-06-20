import pygame.sndarray

from common.wave.pygame_wave import sine_wave, square_wave
from common.play.pygame_play import play_for

pygame.mixer.init(frequency=22050, size=-16, channels=1, buffer=4096)
#pygame.mixer.Sound.set_volume(1.0)

# Play A (440Hz) for 1 second as a sine wave:
play_for(sine_wave(440, 4096), 1000)

# Play A-440 for 1 second as a square wave:
play_for(square_wave(440, 4096), 1000)
