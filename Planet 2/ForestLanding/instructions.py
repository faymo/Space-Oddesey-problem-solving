''''
Arabaro Challenge #1: ForestLanding

You NEED to descend immediately and recharge your batteries. As you try to land your ship through Arabaro's dense atmosphere, you see a huge forest, as well as a cloud of smog in the distance. You have to land your ship properly, or else it may get damaged in the landing.

You will be given a list of locations. Each location is a tuple in the form (NUMBER_OF_TREES, NUMBER_OF_BUSHES). Each location also has a DANGER_SCORE (integer). The formula for DANGER_SCORE is 

DANGER_SCORE = 5 * NUMBER_OF_TREES + 2 * NUMBER_OF_BUSHES

Find the index number (location) of the tree with the highest DANGER_SCORE
'''

locations1 = [(5,1),(3,5),(1,10)]
'''
Example #1:

Let's first calculate the DANGER_SCORE for each index

Index 0: 5*5+1*2 = 27
Index 1: 3*5+5*2 = 25
Index 2: 1*5+10*2 = 25

As Index 0 (the first location) has the higest number of trees, we return 0.
'''

locations2 = [(10,10),(15,0),(0,50)]
'''
Example #1:

Let's first calculate the DANGER_SCORE for each index

Index 0: 10*5+10*2 = 70
Index 1: 15*5+0*2 = 75
Index 2: 0*5+50*2 = 100

As Index 2 (the third location) has the higest number of trees, we return 2.
'''