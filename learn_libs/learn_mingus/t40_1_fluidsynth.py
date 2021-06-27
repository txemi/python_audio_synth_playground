# failed_libs
from mingus.containers import Note
from mingus.midi import fluidsynth

#   fluidsynth.init("soundfont.SF2")
fluidsynth.init("soundfont.SF2", "alsa")
fluidsynth.play_Note(Note("C-5"))
print(1)
