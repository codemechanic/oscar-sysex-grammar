#!/usr/bin/env python

# This script is intended to be run from within the OSCar MIDI Sysex Grammar file

# OSCar Function Byte
#
# Function Labels 0-5

from enum import Enum
valueLabels = Enum('Function', 'Normal, Arpeggiator, Duophonic, Normal-Hold, Arpeggiator-Hold, Duophonic-Hold', start=0)

def parseByteRange(element, byteView, bitPos, bitLength, results):
	# this method parses data starting at bitPos, bitLength bits are remaining
	&quot;&quot;&quot;parseByteRange method&quot;&quot;&quot;

	processedBytes = 0
	initialBitLow = byteView.readUnsignedIntBits(bitPos, 1, ENDIAN_BIG)

	if (initialBitLow == 0):

			# read bits
			result = byteView.readUnsignedIntBits(bitPos+5, 3, ENDIAN_BIG)

			# return value to results
			if (result &lt; len(valueLabels)):
				value = Value()
				value.setString(str(result) + &quot;: &quot; + str(valueLabels(result).name))
				results.addElement(element, 1, 0, value)
				processedBytes = 1
			else:
				print(&quot;Value out of range (0-&quot; + str(len(valueLabels)-1) + &quot;)&quot;)

	return processedBytes

def fillByteRange(value, byteArray, bitPos, bitLength):
	# this method translates edited values back to the file
	&quot;&quot;&quot;fillByteRange method&quot;&quot;&quot;

	# get number edited by user
	number = value.getUnsigned()

	if (number &lt; len(valueLabels)):
		byteArray.writeUnsignedIntBits(number, bitPos, 8, ENDIAN_BIG)
	else:
		print(&quot;Input value out of range (0-&quot; + str(len(valueLabels)-1) + &quot;). Value not updated.&quot;)
