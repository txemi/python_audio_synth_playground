import pyaudio_test1
import pyaudio_test2

la = 440


def octavas():
    for nota in la / 2, la, la * 2:
        pyaudio_test2.play(nota, 1)


def quinta():
    pyaudio_test2.play(la, 1)
    pyaudio_test2.play(la * 3 / 2, 1)


def quinta2(aaa):
    uuu = aaa * (2 ** (7.0 / 12))
    pyaudio_test2.play(la, 1)
    pyaudio_test2.play(uuu, 1)


if __name__ == "__main__":
    quinta()
    quinta2(la)
