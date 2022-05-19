# READ INSTRUCTIONS.PY BEFORE STARTING THIS PROBLEM
def cave_finding(CAVE):
  '''
  CAVE is a parameter that contains a matrix representing the cave the player must traverse.

  The function must return an integer representing the number of caves crossed during his path finding.
  '''
  num_caves = 0
  current_position = CAVE[0][0]
  x = []

  #write code below	
  while current_position != "EXIT":
    x = current_position.split(" ")
    row = int(x[0])
    column = int(x[1])
    current_position = CAVE[row][column]
    num_caves += 1
  return num_caves




#DO NOT TOUCH THE CODE BELOW
slime_cave = [
	["4 4", "3 3", "1 1", "4 2", "4 0"],
	["1 3", "3 1", "1 0", "2 2","0 3"],
	["0 0", "0 1", "EXIT", "0 3", "4 3"],
	["3 4", "3 3", "3 2", "1 3", "2 3"],
	["1 1", "2 1", "4 1", "1 3", "0 4"]
]
print(cave_finding(slime_cave)) 