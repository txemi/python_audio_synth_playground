# https://github.com/luvsound/pippi

from pippi import tune

# Get a list of frequencies from a list of scale degrees
frequencies = tune.degrees([1,3,5,9], octave=3, root='a', scale=tune.MINOR, ratios=tune.JUST)

# Get a list of frequencies from a chord symbol using a tuning system devised by Terry Riley
frequencies = tune.chord('ii69', key='g#', octave=5, ratios=tune.TERRY)

# Convert MIDI note to frequency
freq = tune.mtof(60)

# Convert frequency to MIDI note
note = tune.ftom(440.0)

# Convert a pitch to a frequency
freq = tune.ntf('C#3')
