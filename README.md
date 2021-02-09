# OSCar MIDI System Exclusive (Sysex) Grammar

![OSCar screenshot](https://github.com/codemechanic/oscar-sysex-grammar/blob/main/images/oscar.jpg?raw=true)

This grammar file maps the structure of the MIDI System Exclusive File Format for the [OSCar synthesizer](https://en.wikipedia.org/wiki/OSC_OSCar), and is based on the generic [MIDI System Exclusive (Sysex) Grammar](https://github.com/codemechanic/midi-sysex-grammar).

The OSCar synthesizer was designed by [Chris Huggett](https://en.wikipedia.org/wiki/Chris_Huggett), [Paul Wiffen](http://www.electricityclub.co.uk/synth-guru-interview/), and Anthony Harris-Griffin, and was manufactured by the [Oxford Synthesiser Company](https://en.wikipedia.org/wiki/Oxford_Synthesiser_Company) from 1983 to 1985. The OSCar was ahead of its time in many ways and was one of the few mono-synths of its time to have MIDI.

Grammar files provide an interface for editing and translating human readable values to and from the binary file, and are used in conjunction with the hex and binary file analysis tools [Synalize It!](https://www.synalysis.net) on macOS and [Hexinator](https://hexinator.com) on Windows. Grammars are stored as XML, support both Python and Lua scripting languages, and can export to C structs as well as inherit structures from object oriented languages.

This grammar is intended to be used with Non Real Time Universal System Exclusive Messages.


## Useage
1. Download either the original [oscar_sysex.grammar](https://github.com/codemechanic/oscar-sysex-grammar/blob/main/grammar/oscar_sysex.grammar?raw=true) or the Tauntek version [oscar_tauntek_sysex.grammar](https://github.com/codemechanic/oscar-sysex-grammar/blob/main/grammar/oscar_tauntek_sysex.grammar?raw=true), and open the grammar with Synalize It! or Hexinator.
2. Open an OSCar MIDI Sysex file. If you don't have one available you can download the [factory OSCar Sysex file](https://github.com/codemechanic/oscar-sysex-grammar/blob/main/sysex/factory/FactoryPatch_Wavetable.syx?raw=true) that is provided as a part of this repository.
3. Apply the MIDI Sysex grammar to the Sysex file.


![OSCar screenshot](https://github.com/codemechanic/oscar-sysex-grammar/blob/main/images/screenshot.gif?raw=true)


## New Tauntek firmware and hardware

Bob Grieb from [Tauntek](http://tauntek.com) has developed an updated operating system and [MIDI daughter board for the OSCar synthesizer](http://tauntek.com/OSCar.htm) that add new features and improve its reliability. Settings for the new features have been stored in the unused bits of the Voice Program (patch) data. The benefit to this approach is that Voice Programs stored with new settings take up the same amount of space and are backwards compatible with earlier OSCar firmware revisions. If you're running an older version of the OSCar firmware and do not have the new daughterboard installed, settings for the new features will simply be ignored.

**Improvements:**
1. Reliable power cycling and settings retention.
	* MIDI channel and settings are preserved when the power is turned off.
	* Powering cycling no longer corrupts the RAM.
	* RAM is checked and initialized if contents have been lost, and the factory patch bank is then loaded.
2. MIDI CC reception added for all front panel controls except volume.
3. LFO modulations to Oscillator 1 can be enabled/disabled. This new setting is saved in the patch data.
4. LFO waveform sync can be enabled/disabled. This means the LFO waveform can be reset each time the arpeggiator or sequencer advances to the next note, and runs at the rate set by the LFO rate knob.
5. 3 new Pulse Width Modulation rates (one faster and two slower). This new setting is saved in the patch data.
6. MIDI note velocity can be also used to control filter envelope amount.
7. 3 sets of 36 patches can be loaded from the EPROM (36 factory patches plus two new sets).
8. Current set of patches can be saved in one of two new RAM "save areas". These two slots can be used as a fourth or fifth set of patches to load.
9. New random arpeggiator mode. All held keys are played in a random order.
10. The current patch can be saved to the same location it was loaded from.
11. The last loaded patch is selected at power up rather than defaulting to patch 1.
12. Patch 6 is no longer automatically selected when editing a sequence.
13. CC dump of patch paramters after patch selection can be enabled/disabled. CC dumps are disabled during sequencer playback.


## OSCar schematics
Taking nothing away the hand drawn schematics Chris generously provided, Bob has released a more legible and [modern and set of schematics for the OSCar](http://tauntek.com/oscarschems.zip).


## OSCar Tauntek MIDI Sysex grammar

The [Tauntek version of the OSCar Sysex grammar](https://github.com/codemechanic/oscar-sysex-grammar/blob/main/grammar/oscar_tauntek_sysex.grammar?raw=true) supports the features provided by Tauntek firmware and hardware. This grammar is backwards compatible with Sysex files from earlier firmware revisions. Note that new patch settings in Tauntek Sysex files are simply not applicable to Sysex files saved out by older firmware revisions, and results will be stored in their default (zero) state.


## OSCar Factory Patch and Wavetable sysex plus Patch Names
The [factory Patch and Wavetable sysex](https://github.com/codemechanic/oscar-sysex-grammar/blob/main/sysex/factory/FactoryPatch_Wavetable.syx?raw=true) is available in the sysex folder. The OSCar sysex file does not contain the factory Patch names, however the [list of patch names](https://github.com/codemechanic/oscar-sysex-grammar/blob/main/sysex/factory/FactoryPatchNames.txt?raw=true) can be found in the sysex folder, as well as being provided below:

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


## Special Thanks
* Bob Grieb for his work on the new operatinge system firmware and MIDI daughterboard
* Jeff Pinchbeck for supplying the OSCar factory sysex and patch name files
* Members of the OSCar Synth Owners mailing list for their feedback on feature enhancements and testing
