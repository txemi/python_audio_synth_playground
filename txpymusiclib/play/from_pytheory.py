import pygame
import pytheory
from beartype import beartype
from pytheory import Tone as PyTheoryTone

from txpymusiclib.note_package import note_freq_khe
from txpymusiclib.note_package.note_convert_khe import khe_2_pytheory
from txpymusiclib.note_package.note_freq_khe import get_frequency
from txpymusiclib.wavfile_write.from_tones_mixer import write_wav_for_note


@beartype
def play1(tone_or_chord: PyTheoryTone):
    from pytheory.play import sine_wave, SAMPLE_RATE, _play_for

    synth = sine_wave
    t = 1_000
    temperament = 'equal'
    pygame.mixer.pre_init(SAMPLE_RATE, -16, 1)
    pygame.mixer.init()

    chord = [synth(get_frequency(tone_or_chord.full_name))]

    _play_for(sum(chord), ms=t)


@beartype
def play_with_tone(note_str: str):
    c4_tone = PyTheoryTone.from_string(note_str)
    c4_pitch_s = c4_tone.pitch(symbolic=True)
    met = dir(c4_pitch_s)
    c4_pitch = c4_pitch_s.evalf()

    pytheory.play(c4_tone)

    write_wav_for_note(c4_tone)


@beartype
def print_and_play_tone(tone: PyTheoryTone):
    print(tone)
    print("pytherory:" + str(tone.pitch()))
    print("getFrequency:" + str(get_frequency(tone.full_name)))
    if False:
        pytheory.play(tone)
    else:
        play1(tone)


@beartype
def print_and_play_khe_tone_from_name_and_freq(kati_note_str: str, note_freq: float):
    print(kati_note_str + ":" + str(note_freq))
    ptnote = khe_2_pytheory(kati_note_str)
    tone = PyTheoryTone.from_string(ptnote)
    print_and_play_tone(tone)


@beartype
def print_and_play_khe_tone_from_name(note: str):
    note_freqs = note_freq_khe.get_piano_notes_khe()
    print_and_play_khe_tone_from_name_and_freq(note, note_freqs[note])


def print_and_play_khe_tones_from_names(*args):
    for arg in args:
        print_and_play_khe_tone_from_name(arg)
