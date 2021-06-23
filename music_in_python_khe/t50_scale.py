#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
C major scale with and without sustain. 

@author: khe
"""
import numpy as np
from scipy.io import wavfile
from common.synt_wave import synt_song_khe

# Define scale and piano characteristics
from common.scales_package.scale_static_examples import c_major_scale

note_values = [0.5]*8
factor = [0.68, 0.26, 0.03, 0.  , 0.03]
length = [0.01, 0.6, 0.29, 0.1]
decay = [0.05,0.02,0.005,0.1]
sustain_level = 0.1

# Without sustain (each note in separate bar)
scale_plain = synt_song_khe.get_song_data(c_major_scale, note_values, bar_value=0.5,
                                          factor=factor, length=length, decay=decay,
                                          sustain_level=sustain_level)
scale_plain = scale_plain * (4096/np.max(scale_plain))
wavfile.write('data/scale_plain.wav', 44100, scale_plain.astype(np.int16))

# With sustain (all note in one bar)
scale_sustain = synt_song_khe.get_song_data(c_major_scale, note_values, bar_value=4,
                                            factor=factor, length=length, decay=decay,
                                            sustain_level=sustain_level)
scale_sustain = scale_sustain * (4096/np.max(scale_sustain))
wavfile.write('data/scale_sustain.wav', 44100, scale_sustain.astype(np.int16))