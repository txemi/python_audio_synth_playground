import numpy as np
from beartype import beartype
from matplotlib import pyplot as plt
from scipy.io import wavfile

import common.synt_wave
from common.play.from_pytheory import playKatiNotes
from common.synt_wave import from_numpy_khe

@beartype
def synt_and_play_and_plot_and_writewav_interval(note_freqs, consonant_interval_example, plot_title1: str,
                                                 plot_label1: str):
    wave1 = from_numpy_khe.get_sine_wave(note_freqs[consonant_interval_example[0]], 2,
                                                          amplitude=2048)  # Middle C
    wave2 = from_numpy_khe.get_sine_wave(note_freqs[consonant_interval_example[1]], 2,
                                                          amplitude=2048)  # C one octave above
    playKatiNotes(consonant_interval_example[0], consonant_interval_example[1])
    filename = plot_label1.lower().replace(" ", "_")
    wavfile.write('data/' + filename + '.wav', rate=44100, data=((wave1 + wave2) / 2).astype(np.int16))

    plt.figure(figsize=(12, 4))
    plt.plot(wave1[:2500], label=consonant_interval_example[1])
    plt.plot(wave2[:2500], label=consonant_interval_example[1])
    plt.plot((wave1 + wave2)[:2500], label=plot_label1)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title(plot_title1)
    plt.grid()
    plt.legend()
    plt.savefig('data/' + filename + '.jpg')
