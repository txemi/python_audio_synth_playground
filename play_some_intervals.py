import pyaudio_test1
import pyaudio_test2

la = 440


def intervalo(semitonos):
    return (2 ** (semitonos / 12))


def octavas(nota):
    for nota in nota / 2, nota, nota * 2:
        pyaudio_test2.play(nota, 1)


def quinta(nota):
    pyaudio_test2.play(nota, 1)
    pyaudio_test2.play(nota * 3 / 2, 1)


def quinta2(nota):
    nuevanota = nota * intervalo(7.0)
    pyaudio_test2.play(nota, 1)
    pyaudio_test2.play(nuevanota, 1)


def probando_intervalos(la):
    octavas(la)
    quinta(la)
    quinta2(la)


if __name__ == "__main__":
    probando_intervalos(la)
