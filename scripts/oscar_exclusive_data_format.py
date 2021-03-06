#!/usr/bin/env python

# This script is intended to be run from within the OSCar MIDI Sysex Grammar file

# OSCar Exclusive Data Format
#
# 2 MIDI bytes contain one byte of data
# first byte contains low 4 bit nibble
# second byte contains high 4 bit nibble
#
# 0                8               16
# +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+
# |0|0|0|0|l|l|l|l| |0|0|0|0|h|h|h|h|
# +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+
# \______/ \______/ \______/ \______/
#  4 zero   4 low    4 zero   4 high 


def parseByteRange(element, byteView, bitPos, bitLength, results):
	"""parseByteRange method"""

	processedBytes = 0
	initialBitLow = byteView.readUnsignedIntBits(bitPos, 1, ENDIAN_BIG)

	if (initialBitLow == 0):

		initialBitHigh = byteView.readUnsignedIntBits(bitPos+8, 1, ENDIAN_BIG)

		if (initialBitHigh == 0):

			# combine high and low nibbles from two bytes into one byte
			low = byteView.readUnsignedIntBits(bitPos+4, 4, ENDIAN_BIG)
			high = byteView.readUnsignedIntBits(bitPos+12, 4, ENDIAN_BIG)
			result = (high << 4) | low;

			# return value to results
			value = Value()
			value.setString(str(result))
			results.addElement(element, 2, 0, value)
			processedBytes = 2

	return processedBytes

def fillByteRange(value, byteArray, bitPos, bitLength):
	"""fillByteRange method"""

	if (bitLength < 16):
		print "Not enough space for OSCar Exclusive Data Format, 16 bits needed"

	# get number edited by user
	number = value.getUnsigned()
	high, low = number &gt;&gt; 4, number &amp; 0x0F

	# verbose flag
	verbose = False

	# verbose info
	if verbose:
		print("Input value: " + str(number))
		print("byteArray length: " + str(byteArray.getLength()))
		print("bitPos: " + str(bitPos))
		print("bitLength: " + str(bitLength))

		# number in hex
		numHex = str.format('0x{:02X}', int(str(number), 16))
		print("Input value hex: " + str(numHex))

		# number in binary
		numBinary = '{0:08b}'.format(number)
		print("Input value binary: " + str(numBinary))
		
		# number high and low nibbles
		print("Input value binary (low nibble): " + str('{0:04b}'.format(low)))
		print("Input value binary (high nibble): " + str('{0:04b}'.format(high)))

	if (number < 256):
		byteArray.writeUnsignedIntBits(low, bitPos, 8, ENDIAN_BIG)
		byteArray.writeUnsignedIntBits(high, bitPos+8, 8, ENDIAN_BIG)
	else:
		print("Input value out of range (0-255). Value not updated.")
