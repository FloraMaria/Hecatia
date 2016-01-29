import random
import os

def Generate_Key(size, string):
	# Randomly generate a key of a given size.
	# This key is really just a 'map'.
	# Each number corresponds to a place in the sequence that contains real, and not 'junk', data.
	# The first five digits of the key are the amount of characters of real data.
	# The key cannot be smaller than they string you are inputting.
	string_map = list(string)
	key = []
	data_count = str(len(string_map))
	for zeroes in range(5 - len(data_count)):
		key.append("0")
	for value in data_count:
		key.append(value)
	
	digits = "123456789"
	key2 = ' '.join(random.choice(digits) for _ in range(size))
	key2 = key2.split(" ")
	for keys in key2:
		key.append(keys)
	return key

def Encrypt(key, string, bit_size):
	# Random numbers. Generates a better seed than system time.
	seed_number = int(os.urandom(bit_size).encode('hex'), 16)
	
	# Seed the random number generator.
	random.seed(seed_number)
	
	# Split the key into an array. They then can be easily accessed as integers.
	key_array = key
	
	# Convert the string into binary.
	# Which really doesn't add too much of a security benefit...
	# It was purely a choice of aesthetic.
	converted_string = ' '.join(format(ord(x), 'b') for x in string)
	string_map = converted_string.split(" ")

	#Initialize an empty list.
	#It can support up to 99,999 characters of "real" data.
	data = []
	
	i = 5
	queue = 0

	for strings in string_map:
		for x in range(int(key_array[i]) - 1):
			# All the usable digits for junk data.
			digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789.,;:?!' "
		
			# Create some junk.
			junk = ' '.join(random.choice(digits) for _ in range(1))
		
			# Convert the junk and append it.
			converted_junk = ' '.join(format(ord(x), 'b') for x in junk)

			data.append(converted_junk)
			
		data.append(strings)
		i += 1
		queue += 1
	
	queue2 = len(key_array) - queue
	if queue2 != 0:
		for x in range(queue2):
			digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789.,;:?! "
			junk = ' '.join(random.choice(digits) for _ in range(1))
			converted_junk = ' '.join(format(ord(x), 'b') for x in junk)
			data.append(converted_junk)		
	
	return data
	
def Decrypt(key, data):
	#Gets the size of the string from the first 5 numbers.
	key_array = key
	number_key = str(key_array[0]) + str(key_array[1]) + str(key_array[2]) + str(key_array[3]) + str(key_array[4])
			
	tl_data = []
	# The number in the array.
	y = int(key_array[5]) - 1
	# The number of places to move..
	point = 5
	
	#Decrypt at the specified points.
	for d in range(int(len(key_array))):
		try:
			if d < int(number_key):
				c = data[y]
				decrypted_character = ''.join(chr(int(c[i:i+8], 2)) for i in xrange(0, len(str(c)), 8))
				tl_data.append(decrypted_character)
				point += 1
				y += int(key_array[point])
			else:
				break
		except IndexError:
			break
			
	#Return translated data.
	return tl_data
