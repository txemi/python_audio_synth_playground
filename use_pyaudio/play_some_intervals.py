from use_pyaudio import pyaudio_tone_play
from use_pyaudio.stream_data_for_freq import A_note_frec
from common.tones import fifth_1, fifth_2


def octave_play(tone_freq):
    for tone_freq in tone_freq / 2, tone_freq, tone_freq * 2:
        pyaudio_tone_play.sin_tone_play_2(tone_freq, 1)


def scale1_fifth_play(nota):
    pyaudio_tone_play.sin_tone_play_2(nota, 1)
    pyaudio_tone_play.sin_tone_play_2(nota * fifth_1, 1)


def scale2_fifth_play(tone_freq):
    new_tone_freq = tone_freq * fifth_2
    pyaudio_tone_play.sin_tone_play_2(tone_freq, 1)
    pyaudio_tone_play.sin_tone_play_2(new_tone_freq, 1)


def play_intervals(tone_freq):
    octave_play(tone_freq)
    scale1_fifth_play(tone_freq)
    scale2_fifth_play(tone_freq)


if __name__ == "__main__":
    play_intervals(A_note_frec)
