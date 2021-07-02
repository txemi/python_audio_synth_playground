import os

import numpy as np
from beartype import beartype
from matplotlib import pyplot as plt
from scipy.io import wavfile

from txpymusiclib.interval_package import txintervals
from txpymusiclib.note_package import note_freq_khe
from txpymusiclib.play.from_pytheory import print_and_play_khe_tones_from_names
from txpymusiclib.synt_wave import from_numpy_khe
from txpymusiclib.synt_wave import sample_rates


@beartype
def synth_and_play_and_plot_and_writewav_khe_interval(consonant_interval_example: txintervals.TxKheIntervalExample):
    khe_note_name_2_freq_map = note_freq_khe.get_piano_note_to_freq_map_from_khe_names()
    plot_title1: str = consonant_interval_example.description
    plot_label1: str = consonant_interval_example.sort_description
    start_note_name = consonant_interval_example.start.khe_name
    end_note_name = consonant_interval_example.end.khe_name
    wave1 = from_numpy_khe.get_sine_wave(khe_note_name_2_freq_map[start_note_name], 2,
                                         amplitude=2048)  # Middle C
    wave2 = from_numpy_khe.get_sine_wave(khe_note_name_2_freq_map[end_note_name], 2,
                                         amplitude=2048)  # C one octave above
    print_and_play_khe_tones_from_names(start_note_name, end_note_name)
    filename = plot_label1.lower().replace(" ", "_")
    wavfile.write('data/' + filename + '.wav', rate=sample_rates.sample_rate_44100,
                  data=((wave1 + wave2) / 2).astype(np.int16))

    plt.figure(figsize=(12, 4))
    plt.plot(wave1[:2500], label=start_note_name)
    plt.plot(wave2[:2500], label=end_note_name)
    plt.plot((wave1 + wave2)[:2500], label=plot_label1)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title(plot_title1)
    plt.grid()
    plt.legend()
    plt.savefig('data/' + filename + '.jpg')
