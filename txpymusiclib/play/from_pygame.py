import pygame
import pygame.mixer

from txpymusiclib.synt_wave.sample_rates import sample_rate_22050

on_sec_in_ms = 1_000


def pygame_mixer_init():
    pygame.mixer.init(frequency=sample_rate_22050, size=-16, channels=1, buffer=4096)
    # pygame.mixer.Sound.set_volume(1.0)


def play_for(sample_wave, ms: int):
    """Play the given NumPy array, as a sound, for ms milliseconds."""
    sound = pygame.sndarray.make_sound(sample_wave)
    sound.play(-1)
    pygame.time.delay(ms)
    sound.stop()
