#!/usr/bin/env python

# This script is intended to be run from within the OSCar MIDI Sysex Grammar file

# OSCar Arpeggiator Mode Byte

def parseByteRange(element, byteView, bitPos, bitLength, results):
	# this method parses data starting at bitPos, bitLength bits are remaining
	"""parseByteRange method"""

	processedBytes = 0
	initialBitLow = byteView.readUnsignedIntBits(bitPos, 1, ENDIAN_BIG)

	if (initialBitLow == 0):

			# read bits
			arpMem = byteView.readUnsignedIntBits(bitPos+4, 1, ENDIAN_BIG)
			arpDel = byteView.readUnsignedIntBits(bitPos+5, 1, ENDIAN_BIG)
			arpUp = byteView.readUnsignedIntBits(bitPos+6, 1, ENDIAN_BIG)
			arpDown = byteView.readUnsignedIntBits(bitPos+7, 1, ENDIAN_BIG)

			# set values
			padding = Value()
			arpMemResult = Value()
			arpDelResult = Value()
			arpUpResult = Value()
			arpDownResult = Value()

			# set value strings
			padding.setString("padding: 0000")
			arpMemResult.setString("memory mode: " + str(arpMem))
			arpDelResult.setString("delete mode: " + str(arpDel))
			arpUpResult.setString("up direction: " + str(arpUp))
			arpDownResult.setString("down direction: " + str(arpDown))

			# add values to results
			results.addElementBits(element, 4, 0, padding)
			results.addElementBits(element, 1, 0, arpMemResult)
			results.addElementBits(element, 1, 0, arpDelResult)
			results.addElementBits(element, 1, 0, arpUpResult)
			results.addElementBits(element, 1, 0, arpDownResult)

			processedBytes = 1

	return processedBytes

def fillByteRange(value, byteArray, bitPos, bitLength):
	# this method translates edited values back to the file
	"""fillByteRange method"""

	# get number edited by user
	number = value.getUnsigned()

	if (number < 2):
		byteArray.writeUnsignedIntBits(number, bitPos, 1, ENDIAN_BIG)
	else:
		print("Input value out of range (0-1). Value not updated.")
