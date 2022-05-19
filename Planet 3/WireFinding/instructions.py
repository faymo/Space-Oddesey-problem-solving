'''
New Krief Task 1: WireFinding

Drats! You crash-landed into this icy looking planet and your ship is malfunctioning?! How unlucky can you be... At least you have your batteries with you. But first you are going to have to fix the wiring on your ship.

Your are given a CIRCUIT (a list of strings) where each element is either "red", "green", "blue", or "yellow". Here are the rules:

1) Red wires ONLY connects with blue wires
2) Yellow wires ONLY connects with green wires
3) There may be unconnected wires in the circuit (THIS IS NOT TRUE ON EARTH)

Your job is to figure out THE MAXIMUM possible wire connections in the circuit (integer)
'''



CIRCUIT_1 = ["red", "red", "blue", "blue", "green", "green", "yellow"]

'''
Example #1: 

In this circuit, we have 2 red wires, 2 blue wires, 2 green wires, and 1 yellow wire. 

You can make two connections between red and blue wires, but since you only have one yellow wire, you can only make ONE connection between the green and yellow wires. 

Therefore the total number of wire connections possible is 3!

Notice how there is one green wire that is unconnected. That is OK!
'''



CIRCUIT_2 = ["green", "blue", "blue", "blue", "green", "green", "blue"]

'''
Example #2: 

Since there are no possible connections to be made, 0 is what we return.
'''
