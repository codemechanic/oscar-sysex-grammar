# OSCar MIDI System Exclusive (Sysex) Grammar

![OSCar screenshot](https://github.com/codemechanic/oscar-sysex-grammar/blob/main/images/oscar.jpg?raw=true)

This grammar file maps the structure of the MIDI System Exclusive File Format for the [OSCar synthesizer](https://en.wikipedia.org/wiki/OSC_OSCar), and is based on the generic [MIDI System Exclusive (Sysex) Grammar](https://github.com/codemechanic/midi-sysex-grammar).

The OSCar synthesizer was designed by [Chris Huggett](https://en.wikipedia.org/wiki/Chris_Huggett), [Paul Wiffen](http://www.electricityclub.co.uk/synth-guru-interview/), and Anthony Harris-Griffin, and was manufactured by the [Oxford Synthesiser Company](https://en.wikipedia.org/wiki/Oxford_Synthesiser_Company) from 1983 to 1985. The OSCar was ahead of its time in several ways and was one of the few mono-synths of its time to have MIDI.

Grammars are stored as XML and support both Python and Lua scripting languages. They are powerful in that they can export to C structs as well as inherit structures from object oriented languages. Grammars are used in conjunction with the hex and binary file analysis tools [Synalize It!](https://www.synalysis.net) on macOS and [Hexinator](https://hexinator.com) on Windows.

This grammar is intended to be used with Non Real Time Universal System Exclusive Messages.


## Useage
1. Download and open the <a href="https://github.com/codemechanic/oscar-sysex-grammar/blob/main/grammar/oscar_sysex.grammar?raw=true">oscar_sysex.grammar</a> with either Synalize It! or Hexinator.
2. Open an OSCar MIDI Sysex file.
3. Apply the MIDI Sysex grammar to the Sysex file.


![OSCar screenshot](https://github.com/codemechanic/oscar-sysex-grammar/blob/main/images/screenshot.gif?raw=true)


## Todo:
1. Improve definition of the Sequence Data Block