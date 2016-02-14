# Compute SHA hash (D13128914)
#
# This program runs on provided the hashlib patch pysha3 0.3 available
# to download at https://pypi.python.org/pypi/pysha3/0.3#downloads
# has also been installed
# 
# Program can take either a file or string as input
#

import sys
import hashlib
import sha3

# User is offered choice of input (file/string)
print("Welcome to hash checker. This program can calculate the hash of a string or file.")
question = input("Do you wish to check the hash of a string (S) or file (F)? Enter S or F: ")

# If user choses file, accept filename as input, open, read file, compute hashes
if question == "F" or question == "f":
	filename = input("Enter a file name: ")
	contents = open(filename, 'rb').read()
	yoursha1 = hashlib.sha1(contents)
	yoursha256 = hashlib.sha256(contents)
	yoursha512 = hashlib.sha512(contents)
	yoursha3224 = hashlib.sha3_224(contents)
	yoursha3256 = hashlib.sha3_256(contents)
	yoursha3384 = hashlib.sha3_384(contents)
	yoursha3512 = hashlib.sha3_512(contents)
else:
	# Prompt user to enter string and compute hashes
	guess = input("\nPlease enter a string: ")
	yoursha1 = hashlib.sha1(guess.encode())
	yoursha256 = hashlib.sha256(guess.encode())
	yoursha512 = hashlib.sha512(guess.encode())
	yoursha3224 = hashlib.sha3_224(guess.encode())
	yoursha3256 = hashlib.sha3_256(guess.encode())
	yoursha3384 = hashlib.sha3_384(guess.encode())
	yoursha3512 = hashlib.sha3_512(guess.encode())

# Convert hashes to readable form and print
print("\nYour hashes are computed as follows: ")
print("\nSHA-1:    ", yoursha1.hexdigest())
print("\nSHA-256:  ", yoursha256.hexdigest())
print("\nSHA-512:  ", yoursha512.hexdigest())
print("\nSHA3-224: ", yoursha3224.hexdigest())
print("\nSHA3-256: ", yoursha3256.hexdigest())
print("\nSHA3-384: ", yoursha3384.hexdigest())
print("\nSHA3-512: ", yoursha3512.hexdigest())


input("\nPress the enter key to exit.")

