#!/usr/bin/env python

import sys

def caesar(str, offset):
	def encodeCh(char):
		f = lambda x: chr((ord(char) - x + offset) % 26 + x)
		return f(97) if char.islower() else (f(65) if char.isupper() else char)
	return ''.join(encodeCh(c) for c in str)

def plain_print(cipher):
	for i in range(0, 26):
		print(i)
		print(caesar(cipher,i))
plain_print(sys.argv[1])
