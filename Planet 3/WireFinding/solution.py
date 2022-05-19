# READ INSTRUCTIONS.PY BEFORE STARTING THIS PROBLEM

def wire_finding(CIRCUIT):
	'''
	CIRCUIT is a parameter that contains a list with either "red", "blue", "green", or "yellow"

	The function must return an integer representing the number of connections that can be made
	'''
	num_connections = 0

	red = 0
	blue = 0
	green = 0
	yellow = 0

	for wire in CIRCUIT:
		if (wire == "red"): 
			red += 1
		elif(wire == "green"):
			green += 1
		elif(wire == "blue"): 
			blue += 1
		elif(wire == "yellow"):
			yellow += 1
	
	#Example: If there are 4 red and 2 green wires, there are only 2 connections. So it is the minimum of the two that represent the max connections.
	num_connections += min(red, green)
	num_connections += min(blue, yellow)

	return num_connections

#DO NOT TOUCH THE CODE BELOW
large_circuit = ["red", "green", "blue", "blue", "green", "red", "yellow", "yellow", "yellow", "red", "green", "red", "green", "blue", "yellow", "red", "green", "red", "yellow", "red", "green", "red", "yellow", "red", "green", "red", "orange", "red", "green", "red", "blue", "yellow", "red", "green", "red", "green", "blue", "yellow", "red", "green", "red", "blue", "yellow","yellow", "yellow", "yellow", "red", "green", "red", "green", "blue", "yellow", "yellow", "yellow", "red", "green", "red", "green", "blue","red", "green", "blue", "blue", "green", "red", "yellow", "yellow", "yellow", "red", "green", "red", "green", "blue", "yellow", "red", "green", "red", "yellow", "red", "green", "red", "yellow", "red", "green", "hcw", "red", "green", "red", "blue", "blue","red", "green", "blue", "blue", "green", "red", "yellow", "yellow", "yellow", "red", "green", "red", "green", "blue", "yellow", "red", "green", "red", "yellow", "red", "green", "red", "yellow", "red", "green", "red", "red", "green", "red", "blue", "green", "red", "red", "green", "red", "blue", "yellow","red", "green", "blue", "red", "blue", "yellow", "red", "green", "red", "green", "blue", "yellow", "red", "red", "blue", "yellow","yellow", "yellow", "yellow", "red", "green", "red", "green", "blue", "yellow", "yellow", "yellow", "red", "green", "red", "green", "blue", "yellow", "red", "green", "red", "blue", "yellow","yellow", "yellow", "yellow", "red", "green", "red", "green", "blue", "yellow", "yellow", "yellow", "red"]

print(wire_finding(large_circuit)) 