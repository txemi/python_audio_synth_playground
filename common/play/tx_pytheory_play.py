import pygame
import pytheory
from pytheory import Tone

from common import utils
from common.freq import getFrequency
from common.filewrite.txwavwrite import write_wav_for_note
from common.txtones import katieshiqihe2pytheory

from beartype import beartype


@beartype
def play1(tone_or_chord: Tone):
    from pytheory.play import sine_wave, SAMPLE_RATE, _play_for

    synth = sine_wave
    t = 1_000
    temperament = 'equal'
    pygame.mixer.pre_init(SAMPLE_RATE, -16, 1)
    pygame.mixer.init()

    chord = [synth(getFrequency(tone_or_chord.full_name))]

    _play_for(sum(chord), ms=t)


@beartype
def play_with_tone(note_str: str):
    c4_tone = Tone.from_string(note_str)
    c4_pitch_s = c4_tone.pitch(symbolic=True)
    met = dir(c4_pitch_s)
    c4_pitch = c4_pitch_s.evalf()

    pytheory.play(c4_tone)

    write_wav_for_note(c4_tone)


@beartype
def print_and_play_tone(tone: Tone):
    print(tone)
    print("pytherory:" + str(tone.pitch()))
    print("getFrequency:" + str(getFrequency(tone.full_name)))
    if False:
        pytheory.play(tone)
    else:
        play1(tone)


@beartype
def playKatiNote(a: str, b: float):
    print(a + ":" + str(b))
    e = katieshiqihe2pytheory(a)
    c = Tone.from_string(e)
    print_and_play_tone(c)


def playKatiNote2(note:str):
    note_freqs = utils.get_piano_notes()
    playKatiNote(note, note_freqs[note])


def playKatiNote3(*args):
    for arg in args:
        playKatiNote2(arg)