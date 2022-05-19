# READ INSTRUCTIONS.PY BEFORE STARTING THIS PROBLEM
def decoding_passcode1(door_code):
  '''
  encrypted_code represents a seven-letter secret code that we need to decrypt

  The function must return a string representing the decrypted version of the door code

  USE THE ALPHABET VARIABLE TO HELP WITH YOUR CODE!
  '''
  decrypted_code = ""
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  
  #write code here
  decrypted_code = sorted(door_code)
  decrypted_code2 = []
  for x in decrypted_code:
    index = alphabet.index(x) + 1
    decrypted_code2.append(index)
  
  step3 =
  return decrypted_code


#DO NOT TOUCH THE CODE BELOW
door_code = "LIBERTY"
print(decoding_passcode1(door_code))