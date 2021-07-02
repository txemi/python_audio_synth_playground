from txpymusiclib.note_package import txnote
from txpymusiclib.play.from_pygame import play_for, pygame_mixer_init, on_sec_in_ms
from txpymusiclib.synt_wave.from_numpy import sine_wave, square_wave
from txpymusiclib.synt_wave.sample_rates import sample_rate_4096

pygame_mixer_init()
# Play A (440Hz) for 1 second as a sine wave:
play_for(sine_wave(txnote.note_A4.freq, sample_rate_4096), on_sec_in_ms)

# Play A-440 for 1 second as a square wave:
play_for(square_wave(txnote.note_A4.freq, sample_rate_4096), on_sec_in_ms)
