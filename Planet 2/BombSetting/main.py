#READ INSTRUCTIONS.PY BEFORE STARTING

def bomb_setting(red_wires, green_wires, yellow_wires, blue_wires):
  ''' 
  There are four parameters (or local variables), each representing the amount of either red, green, yellow, or blue wires.

  The function must return the total amount of extra wiring needed.
  '''
  extra_wires = 0

  #write code here
  a = max(red_wires, green_wires) - min(red_wires, green_wires)
  b = max(yellow_wires, blue_wires) - min(yellow_wires, blue_wires)
  extra_wires = a + b
  return extra_wires

#DO NOT CHANGE THE CODE BELOW
from random import seed, randint
seed(25565)
print(f"There are {bomb_setting(randint(1,10),randint(1,10),randint(1,10),randint(1,10))} extra wires needed.")