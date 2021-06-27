# https://github.com/eriknyquist/tones
from tones import SINE_WAVE, SAWTOOTH_WAVE
from tones.mixer import Mixer
from txpymusiclib.synt_wave.sample_rates import DEFAULTRATE
# Create mixer, set sample rate and amplitude
mixer = Mixer(DEFAULTRATE, 0.5)

# Create two monophonic tracks that will play simultaneously, and set
# initial values for note attack, decay and vibrato frequency (these can
# be changed again at any time, see documentation for tones.Mixer
mixer.create_track(0, SAWTOOTH_WAVE, vibrato_frequency=7.0, vibrato_variance=30.0, attack=0.01, decay=0.1)
mixer.create_track(1, SINE_WAVE, attack=0.01, decay=0.1)

# Add a 1-second tone on track 0, slide pitch from c# to f#)
mixer.add_note(0, note='c#', octave=5, duration=1.0, endnote='f#')

# Add a 1-second tone on track 1, slide pitch from f# to g#)
mixer.add_note(1, note='f#', octave=5, duration=1.0, endnote='g#')

# Mix all tracks into a single list of samples and write to .wav file
mixer.write_wav('tones.wav')

# Mix all tracks into a single list of samples scaled from 0.0 to 1.0, and
# return the sample list
samples = mixer.mix()
print(1)
