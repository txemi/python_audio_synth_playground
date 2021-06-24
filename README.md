# txpymusiclib playground

https://github.com/txemi/txpymusiclib

Playground and library for music theory and synthesis.

This code is WORK IN PROGRESS.  No released yet.

I wanted to learn about how to play with tones, frecuencies, intervals, chords, scales, etc with python and learn the maths behind, so I made this compilation of libraries and examples in order to know about diferent libraries related to music in python.

You will find a lot of packages whose name stars with learn_* meaning reference to the library tested inside.

I also move common functionality to txpymusiclib package in order to merge and build a biggest framework in witch you can find different ways to achieve the same objective and choose wich one fit best.

Different libraries use different naming conventions for notes so I plan to make converters when needed.

I assume using python3 to take advantage of new features as type checking and also use often absolute route to packages so you often need to configure your IDE or start python on top level folder. These decisions are taken in order to focus on audio and music, not on python troubleshooting.

A requirements.txt that worked for me is provided to make easy to start using this code inside a new virtualenv with requirements installed.

I am using pycharm as IDE as it allows to debug inside dependent libraries what is useful for understanding how do they work inside.

I plan to license GPL with the exception of previously licensed borrowed code that I will agree with mainstream authors.

Now I mention  libraries I tried in order of my actual preference, it could change:

For music theory:
- mingus: Very complete, I use this one if I can
- pytheory: less complete than mingus, but uses symbolic maths, what makes it very interesting for expressing roots and understanding where non rational numbers come from.
- musthe: less complete than mingus, mingus preferred
- pychord: less complete than mingus, mingus preferred
- pytuning: not used very much

For audio playing:  
- synthesizer: for audio playing
- pygame: used just for audio playing, but it can do a lot of things
- pyaudio: for audio playing

Other:
- music_in_python_kde: I learnt a lot with this code from katiehe and I used some parts in txpymusiclib. it builds some songs from scratch, generating tones. Thanks a lot.
- tones: wav writing

Libraries that did not work for me:
- pippi
- pyaudiere
- sonic

You can also look for the functionality you need in txpymusiclib and use it, it will automatically use one of previous libraries as I am moving common functionality there.

For future I would like to play with lilypond code or musicxml not to store scripts in python arrays and use a better language representation.

TODO: 
- scale examples revisit (more code in txpymusiclib, better wrapping)
- jupyter revisit
- lilypond or musicxml integration

