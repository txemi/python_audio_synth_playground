import pyaudio_tone_play
from stream_data_for_freq import A_note_frec


def interval_factor(half_steps):
    return 2 ** (half_steps / 12)


def octave_play(tone_freq):
    for tone_freq in tone_freq / 2, tone_freq, tone_freq * 2:
        pyaudio_tone_play.sin_tone_play_2(tone_freq, 1)


def scale1_fifth_play(nota):
    pyaudio_tone_play.sin_tone_play_2(nota, 1)
    pyaudio_tone_play.sin_tone_play_2(nota * 3 / 2, 1)


def scale2_fifth_play(tone_freq):
    new_tone_freq = tone_freq * interval_factor(7.0)
    pyaudio_tone_play.sin_tone_play_2(tone_freq, 1)
    pyaudio_tone_play.sin_tone_play_2(new_tone_freq, 1)


def play_intervals(tone_freq):
    octave_play(tone_freq)
    scale1_fifth_play(tone_freq)
    scale2_fifth_play(tone_freq)


if __name__ == "__main__":
    play_intervals(A_note_frec)
