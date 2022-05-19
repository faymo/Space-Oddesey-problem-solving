# READ INSTRUCTIONS.PY BEFORE STARTING THIS PROBLEM

def slime_finding(SLIME_LAKE):
  '''
  SLIME_LAKE is a parameter that contains a string with space-seperated words.

  The function must return an integer representing the number of occurances of the word "battery" in the string
  '''
  num_batteries = 0

  #write code here
  split_string = SLIME_LAKE.split(" ")
  for word in split_string:
    if word == "battery":
      num_batteries += 1
  return num_batteries



#DO NOT TOUCH THE CODE BELOW
large_slime_pile = "slime slime slime goo goo goo slime goo slime battery slime goo wrench slime slime slime slime goo wrench battery battery battery slime slime slime slime goo goo goo wrench slime slime slime goo slime slime slime battery slime battery battery slime battery gun slime goo goo goo slime battery wrench slime goo battery battery bucket sock slime slime slime skull skull slime goo goo goo slime slime slime battery battery slime slime slime slime goo skull battery battery pin slime goo goo hcw slime goo goo goo goo slime battery skull goo bucket sock slime slime slime goo goo goo slime goo slime battery slime goo wrench slime slime slime slime goo wrench battery battery battery slime slime slime slime goo goo goo wrench slime slime slime goo slime slime slime battery slime battery battery slime battery gun slime goo goo goo slime battery wrench slime goo battery battery bucket sock slime slime slime skull skull slime goo goo goo slime slime slime battery battery slime slime slime slime goo skull battery battery hcwpin slime goo goo hcwpin slime goo goo goo goo slime battery skull goo bucket sock slime slime slime goo goo goo slime goo slime battery slime goo slime slime slime goo goo goo wrench slime slime slime goo slime slime slime battery slime battery battery slime battery gun slime goo goo goo slime battery wrench slime goo battery battery bucket sock slime slime slime skull skull slime goo goo goo slime slime slime battery battery slime slime slime slime goo skull battery battery pin slime goo goo hcw slime goo goo goo goo slime battery skull goo bucket sock battery slime battery battery slime battery gun slime goo goo goo slime battery wrench slime goo battery battery bucket sock slime slime slime skull skull slime goo goo goo slime slime slime battery battery slime slime slime slime goo skull battery battery pin slime goo goo hcw slime goo goo goo goo slime battery skull goo bucket sock"

print(slime_finding(large_slime_pile)) 
