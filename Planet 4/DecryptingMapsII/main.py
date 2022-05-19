# READ INSTRUCTIONS.PY BEFORE STARTING THIS PROBLEM
def decrypt_maps_2(hint_word):
  '''
  hint_word represents a string that is a hint for the password to unlock the cage.

  The function must return a list of numbers that has the same amount of numbers as letters in the hint word.

  USE THE ALPHABET VARIABLE TO HELP WITH YOUR CODE!
  '''

  alphabet = 'abcdefghijklmnopqrstuvwxyz'

  password = []

  #write code here
  for char in hint_word:
    if char in alphabet:
      n = alphabet.index(char) + 1
      password.append(n)
  return password


#DO NOT TOUCH THE CODE BELOW

map_path = "-".join([str(e) for e in decrypt_maps_2("saveus")])
print(f"The map path is (ENTER THE FOLLOWING EXACTLY ON THE WEBSITE): {map_path}")
