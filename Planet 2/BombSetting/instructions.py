''''
Arabaro Challenge #3: BombSetting

Time to take out a factory! Oh boy is Commander Kaif not going to like this...but hey, it's for a good cause! You have infiltrated the factory and you need to rig the bomb to signal the attack to the Arabarian Natives. 

You will be given four parameters: RED_WIRES, GREEN_WIRES, YELLOW_WIRES, and BLUE_WIRES. The bomb WILL NOT work unless you have the correct configuration for the wires. Here are the requirements:

1.) There must be the same number of red wires as there are green wires
2.) There must be the same number of blue wires as there are yellow wires
3.) You CANNOT REMOVE wires...you can only configure/add more wires


How many total wires do you need to add
'''


red, green, yellow, blue = 10, 8, 9, 9
'''
Example #1:

1.) We have 10 red wires and 8 green wires. That means we must need 2 more green wires
2.) We already have the same amount of blue wires as yellow wires :)

ANSWER: 2 more total wires
'''


red, green, yellow, blue = 8, 10, 2, 5
'''
Example #2:

1.) We have 8 red wires and 10 green wires. That means we must need 2 more red wires
2.) We have 2 yellow wires and 5 blue wires. That means we need 3 more yellow wires

ANSWER: 5 more total wires
'''