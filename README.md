# python_audio_synth_playground

https://github.com/txemi/python_audio_synth_playground

Playground for chord and tone synth.

I wanted to learn about how to play with tones, frecuencies, intervals, chords, scales, etc with python and learn the maths behind, so I made this compilation of libraries and examples in order to know about diferent libraries related to music in python.

You will find a lot of packages whose name stars with learn_* meaning reference to the library tested inside.

I also move common functionality to common package in order to merge and build a biggest framework in witch you can find different ways to achieve the same objective.

Different libraries use different naming conventions for notes so I plan to make converters when needed.

I assume using python3 to take advantage of new features as typing and also use often absolute route to packages so you often need to configure your IDE or start python on top level folder.

A requirements.txt that worked for me is provided to make easy to start using this code inside a new virtualenv with requirements installed.

I am using pycharm as IDE as it allows to debug inside dependent libraries what is useful for understanding how do they work inside.

If you just want to play notes and chords you could start directly with synthesizer python library. It is very easy.
Pytheory is interesting as it uses simpy for calculations so you avoid losing precision and understand better where non rational numbers come from.
Music_in_python from katiehe is very interesting; it builds some songs from scratch, generating tones.
For future I would like to play with lilypond code not to store scripts in python arrays and use a better language representation.

I plan to license GPL with the exception of previously licensed borrowed code that I will agree with mainstream author.


