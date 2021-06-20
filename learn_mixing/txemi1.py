from beartype import beartype
from tones.mixer import Mixer
from pytheory import TonedScale, Tone, Scale
import pytheory

import pygame


# Python to convert a string note (eg. "A4") to a frequency (eg. 440).
# Inspired by https://gist.github.com/stuartmemo/3766449
def getFrequency(note, A4=440):
    notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

    octave = int(note[2]) if len(note) == 3 else int(note[1])

    keyNumber = notes.index(note[0:-1])

    off = 12 if (keyNumber < 3) else 0

    keyNumber = keyNumber + off + ((octave - 1) * 12) + 1

    return A4 * 2 ** ((keyNumber - 49) / 12)


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


def play1(tone_or_chord):
    from pytheory.play import sine_wave, SAMPLE_RATE, _play_for

    synth = sine_wave
    t = 1_000
    temperament = 'equal'
    pygame.mixer.pre_init(SAMPLE_RATE, -16, 1)
    pygame.mixer.init()

    chord = [synth(getFrequency(tone_or_chord.full_name))]

    _play_for(sum(chord), ms=t)


c4_note_str = 'C4'


def play_with_tone():
    c4_tone = Tone.from_string(c4_note_str)
    c4_pitch_s = c4_tone.pitch(symbolic=True)
    met = dir(c4_pitch_s)
    c4_pitch = c4_pitch_s.evalf()

    pytheory.play(c4_tone)

    write_wav_for_note(c4_tone)

def print_and_play_tone(tone):
    print(tone)
    print("pytherory:" + str(tone.pitch()))
    print("getFrequency:" + str(getFrequency(tone.full_name)))
    if False:
        pytheory.play(tone)
    else:
        play1(tone)
def play_with_scale():
    ts = TonedScale(tonic=c4_note_str)
    c_minor = ts["major"]
    for tone in c_minor.tones:
        print_and_play_tone(tone)

    write_wav_for_toned_scale(c_minor)


play_with_scale()
print(1)
