# OSCar MIDI System Exclusive (Sysex) Grammar

![OSCar screenshot](https://github.com/codemechanic/oscar-sysex-grammar/blob/main/images/oscar.jpg?raw=true)

This grammar file maps the structure of the MIDI System Exclusive File Format for the [OSCar synthesizer](https://en.wikipedia.org/wiki/OSC_OSCar), and is based on the generic [MIDI System Exclusive (Sysex) Grammar](https://github.com/codemechanic/midi-sysex-grammar).

The OSCar synthesizer was designed by [Chris Huggett](https://en.wikipedia.org/wiki/Chris_Huggett), [Paul Wiffen](http://www.electricityclub.co.uk/synth-guru-interview/), and Anthony Harris-Griffin, and was manufactured by the [Oxford Synthesiser Company](https://en.wikipedia.org/wiki/Oxford_Synthesiser_Company) from 1983 to 1985. The OSCar was ahead of its time in many ways and was one of the few mono-synths of its time to have MIDI.

Grammar files provide an interface for editing and translating human readable values to and from the binary file, and are used in conjunction with the hex and binary file analysis tools [Synalize It!](https://www.synalysis.net) on macOS and [Hexinator](https://hexinator.com) on Windows. Grammars are stored as XML, support both Python and Lua scripting languages, and can export to C structs as well as inherit structures from object oriented languages.

This grammar is intended to be used with Non Real Time Universal System Exclusive Messages.


## Useage
1. Download and open the [oscar_sysex.grammar](https://github.com/codemechanic/oscar-sysex-grammar/blob/main/grammar/oscar_sysex.grammar?raw=true) with either Synalize It! or Hexinator.
2. Open an OSCar MIDI Sysex file. If you don't have one available you can download the [factory OSCar Sysex file](https://github.com/codemechanic/oscar-sysex-grammar/blob/main/sysex/factory/FactoryPatch_Wavetable.syx?raw=true) that is provided as a part of this repository.
3. Apply the MIDI Sysex grammar to the Sysex file.


![OSCar screenshot](https://github.com/codemechanic/oscar-sysex-grammar/blob/main/images/screenshot.gif?raw=true)


## OSCar Factory Patch and Wavetable sysex and Patch Names
The [factory Patch and Wavetable sysex](https://github.com/codemechanic/oscar-sysex-grammar/blob/main/sysex/factory/FactoryPatch_Wavetable.syx?raw=true) is available in the sysex folder. The OSCar sysex file does not contain the factory Patch names. The [list of patch names](https://github.com/codemechanic/oscar-sysex-grammar/blob/main/sysex/factory/FactoryPatchNames.txt?raw=true) can be found in the sysex folder, and are also provided below:

| Number | Name |
|-|-|
| -12 | Hollow Bass |
| -11 | HumanLeague |
| -10 | DigitalFuzz |
| -9 | FrogCroak |
| -8 | OnTheLeash |
| -7 | DistantLead |
| -6 | FatWobble |
| -5 | PercussiveBass |
| -4 | HorrorSoundtrack |
| -3 | IdealSequence |
| -2 | LFOHell |
| -1 | GlassandoLead |
| 1 | PWMLead |
| 2 | ElectricCello |
| 3 | DiveBommer |
| 4 | ChurchOrgan |
| 5 | StaccatoBass |
| 6 | HollowSequencer |
| 7 | LoDrone |
| 8 | SequencePulse |
| 9 | AnalogueBass |
| 10 | SquareLead |
| 11 | TheBigSquidge |
| 12 | FatAndWobbly |
| 13 | Noise |
| 14 | BlippyLead |
| 15 | SlapBassGuitar |
| 16 | MixedLead |
| 17 | DigitalThin |
| 18 | SequenceMe |
| 19 | HammondyLead |
| 20 | EgyptianLead |
| 21 | Clarinet |
| 22 | DigitalOrgan |
| 23 | Brutal |
| 24 | Snare |


## Todo
* Improve definition of the Sequence Data Block


## Thanks
Special thanks to Jeff Pinchbeck for providing the OSCar factory sysex and patch name files.