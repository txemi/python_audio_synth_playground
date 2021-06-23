from beartype import beartype
from pytheory import Tone, Scale
from tones.mixer import Mixer


@beartype
def write_wav_for_note(tone: Tone):
    mixer = Mixer()
    mixer.create_track(0)
    mixer.add_note(0, note=tone.name, octave=tone.octave, duration=1.0)
    mixer.write_wav('tones.wav')


@beartype
def write_wav_for_toned_scale(scale: Scale):
    mixer = Mixer()
    mixer.create_track(0)
    # el cambio de octava suena mal
    for tone in scale.tones:
        if False:
            mixer.add_note(0, note=tone.name, octave=tone.octave, duration=1.0)
        else:
            mixer.add_tone(0, frequency=tone.pitch())
    mixer.write_wav('tones.wav')