'''
New Krief Task 3: CaveFinding

You were finaly able to talk to Nishad and learn a bit about the history of New Krief and the District of Krieg. You also obtained some filtered slime, which Nishad said would come in handy soon.

However, now you are going to need to find your way out of the cave. The cave is represented by a matrix CAVE (max 10x10 size), and each element of the matrix will contain a string in the format "ROW_NUM COL_NUM" (rows and columns start at 0) representing a path in the cave. There will also be ONE EXIT element. Your job is to figure out how many paths you must cross to get to the exit (in the form of an integer).

You will start at position "0 0". Then you will move to whatever row and column is at position "0 0". You will continue to do this until you reach the EXIT. IT IS GUARENTEED THAT YOU CAN REACH THE EXIT!!!
'''

EXAMPLE_CAVE_1 = [
	["2 2", "1 1", "EXIT"],
	["0 2", "0 2", "1 2"],
	["2 1", "1 2", "0 1"]
]

'''
Example #1: 

We start at position "0 0". Then we move to position "2 2". Then we move to position "0 1". Then we move to position "1 1". Then we move to position "0 2". As at position "0 2", there is an "EXIT" string, we can exit out of the loop and return how many paths we had to cross.

Since we had to cross "2 2", "0 1", "1 1", and "0 2", we return 4.
'''



EXAMPLE_CAVE_2 = [
	["3 3", "1 1", "0 1", "1 3"],
	["0 2", "0 2", "1 2", "3 2"],
	["2 1", "3 3", "0 3", "3 0"],
	["0 0", "2 3", "3 3", "EXIT"]
]

'''
Example #2: 

We start at position "0 0". Then we move to position "3 3". As at position "3 3", there is an "EXIT" string, we can exit out of the loop and return how many paths we had to cross

Since we just had to cross "3 3", we return 1.
'''