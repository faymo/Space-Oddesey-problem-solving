#READ INSTRUCTIONS.PY BEFORE STARTING

def decrypting_maps_3(serial_code):
  ''' 
  There is one parameter, a string serial_code, which needs to be converted to the password

  The function must return the decrypted password as a string
  '''
  password = ""
  letter_code = ""
  special_characters = "!@#$%^&*"

  #write code here
  for char in serial_code:
    if not char in special_characters:
      letter_code = letter_code + char
  half = len(letter_code) // 2
  firsthalf = letter_code[:half]
  secondhalf = letter_code[half:]
  reversefirst = firsthalf[::-1]
  reversesecond = secondhalf[::-1]
  password = reversefirst + reversesecond
  return password

#DO NOT CHANGE THE CODE BELOW
print(f"The password is {decrypting_maps_3('!i#%#n^##^&#^a$gr##%#^#^#o%##^&&n%o^^@$it#^#^a#^#%&&$#^z')}")