# READ INSTRUCTIONS.PY BEFORE STARTING THIS PROBLEM
def decoding_passcode1(door_code):
	'''
	encrypted_code represents a seven-letter secret code that we need to decrypt

	The function must return a string representing the decrypted version of the door code
	
	USE THE ALPHABET VARIABLE TO HELP WITH YOUR CODE!
	'''
	decrypted_code = []
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	#Step 1: Alphebatize door_code in order
	door_code = list(door_code)
	door_code.sort()

	#Step 2: Convert each letter to corresponding number
	for letter in door_code:
		letter_index = alphabet.index(letter) + 1 #add 1 since lists start at 0 index
		decrypted_code.append(letter_index)
	
	#Step 3: Multiply each number by their position in the list
	for position in range(len(decrypted_code)):
		decrypted_code[position] *= (position + 1) #Taking each number at a certain position and multiplying it by that position
	
	#Step 4: Put together the decrypted code together as a string with dashes
	for position in range(len(decrypted_code)):
		#We need to turn each integer into a string
		decrypted_code[position] = str(decrypted_code[position])

	decrypted_code = "-".join(decrypted_code) #joining together each element of the list together by dashes into a string

	return decrypted_code


#DO NOT TOUCH THE CODE BELOW
door_code = "LIBERTY"
print(decoding_passcode1(door_code))