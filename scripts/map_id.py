#!/usr/bin/env python

# This script is intended to be run from within the OSCar MIDI Sysex Grammar file

currentGrammar = currentMapper.getCurrentGrammar()
multiByteID = currentGrammar.getStructureByName(&quot;Multi Byte ID&quot;)
singleByteID = currentGrammar.getStructureByName(&quot;Single Byte ID&quot;)

currentPos = currentMapper.getCurrentOffset()
byteView = currentMapper.getCurrentByteView()
byte = byteView.readByte(currentPos)

if (byte == 0x00):
	currentMapper.mapStructure(multiByteID)
	debugLog(&quot;Multi Byte ID mapped at offset &quot; + str(currentPos))
else:
	currentMapper.mapStructure(singleByteID)
	debugLog(&quot;Single Byte ID mapped at offset &quot; + str(currentPos))
