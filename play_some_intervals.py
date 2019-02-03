import tone_play
from stream_data_for_freq import la_note_frec


def intervalo(semitonos):
    return (2 ** (semitonos / 12))


def octavas(nota):
    for nota in nota / 2, nota, nota * 2:
        tone_play.sin_tone_play_2(nota, 1)


def quinta(nota):
    tone_play.sin_tone_play_2(nota, 1)
    tone_play.sin_tone_play_2(nota * 3 / 2, 1)


def quinta2(tone_freq):
    new_tone_freq = tone_freq * intervalo(7.0)
    tone_play.sin_tone_play_2(tone_freq, 1)
    tone_play.sin_tone_play_2(new_tone_freq, 1)


def probando_intervalos(tone_freq):
    octavas(tone_freq)
    quinta(tone_freq)
    quinta2(tone_freq)


if __name__ == "__main__":
    probando_intervalos(la_note_frec)
