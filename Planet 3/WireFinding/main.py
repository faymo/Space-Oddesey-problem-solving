# READ INSTRUCTIONS.PY BEFORE STARTING THIS PROBLEM

def wire_finding(CIRCUIT):
  '''
  CIRCUIT is a parameter that contains a list with either "red", "blue", "green", or "yellow"

  The function must return an integer representing the number of connections that can be made
  '''
  num_connections = 0
  red_wires = 0
  green_wires = 0
  blue_wires = 0
  yellow_wires = 0

  #write code here
  for word in CIRCUIT:
    if word == "red":
      red_wires += 1
    elif word == "blue":
      blue_wires += 1
    elif word == "yellow":
      yellow_wires += 1
    elif word == "green":
      green_wires += 1
  num_connections = min(red_wires, blue_wires) + min(yellow_wires, green_wires)
  return num_connections

#DO NOT TOUCH THE CODE BELOW
large_circuit = ["red", "green", "blue", "blue", "green", "red", "yellow", "yellow", "yellow", "red", "green", "red", "green", "blue", "yellow", "red", "green", "red", "yellow", "red", "green", "red", "yellow", "red", "green", "red", "orange", "red", "green", "red", "blue", "yellow", "red", "green", "red", "green", "blue", "yellow", "red", "green", "red", "blue", "yellow","yellow", "yellow", "yellow", "red", "green", "red", "green", "blue", "yellow", "yellow", "yellow", "red", "green", "red", "green", "blue","red", "green", "blue", "blue", "green", "red", "yellow", "yellow", "yellow", "red", "green", "red", "green", "blue", "yellow", "red", "green", "red", "yellow", "red", "green", "red", "yellow", "red", "green", "hcw", "red", "green", "red", "blue", "blue","red", "green", "blue", "blue", "green", "red", "yellow", "yellow", "yellow", "red", "green", "red", "green", "blue", "yellow", "red", "green", "red", "yellow", "red", "green", "red", "yellow", "red", "green", "red", "red", "green", "red", "blue", "green", "red", "red", "green", "red", "blue", "yellow","red", "green", "blue", "red", "blue", "yellow", "red", "green", "red", "green", "blue", "yellow", "red", "red", "blue", "yellow","yellow", "yellow", "yellow", "red", "green", "red", "green", "blue", "yellow", "yellow", "yellow", "red", "green", "red", "green", "blue", "yellow", "red", "green", "red", "blue", "yellow","yellow", "yellow", "yellow", "red", "green", "red", "green", "blue", "yellow", "yellow", "yellow", "red"]

print(wire_finding(large_circuit)) 