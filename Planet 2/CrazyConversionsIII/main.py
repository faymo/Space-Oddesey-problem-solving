#READ INSTRUCTIONS.PY BEFORE STARTING

def find_supplies(supplies):
	''' 
	supplies (list) represents the dictionary of supply_name(string):cost(integer)

	The function must return the total cost of two of each supply
	'''
	total_cost = 0

	for supply_name in supplies:
		total_cost += 2 * supplies[supply_name]
	
	return total_cost
	

#DO NOT CHANGE THE CODE BELOW
supply = {"rations":10, "water":5, "pickaxe":50, "ship parts":100}
print(f"The total_cost of supplies is{find_supplies(supply)}")

















#write code here
	for supply_name in supplies:
		total_cost += 2 * supplies[supply_name]

	return total_cost