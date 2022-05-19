'''
YCW Space Station Task #3: GeneratorFailure

You have finally reached the center of the space station after an tough battle. Bruised but not battered, you finally try to open the enterance to the core. OH SHOOT! The power was shut off. You can hear muffled voices and lasers shooting inside. You need to hurry!

You go to the generator, whose circuitboard is marked with either X or O (the circuitboard is a string with either "X" or "O"). X means on and O means off. 

If three contigous (connected) segments are on at once, it adds 1V of power to the generator. The generator needs at least 15V to work, and it will fail if it doesn't reach that amount. Calculate the amount of extra voltage needed TO REACH 15V.
'''


circuit = "XXXOOOOXXOXXX"
'''
Example 1: 

Although there are many cases where there are two Xs in a row and even more Os in a row, we only care about if there are three continous Xs in a row

There is an XXX at the beginning and at the end, therefore there is 2V of power. 

15-2 = 13V needed (13 is our answer)
'''


circuit = "XXXXXOOOXOX"
'''
Example 2: 

This is IMPORTANT!!! Just because there is only one group of Xs that is greater than 3 DOES NOT mean 1V of power.

There is actual 3V of power, because XXXXX can be split up into three ways

1.) [XXX]|XX
2.) X|[XXX]|X
3.) XX|[XXX]

15-3 = 12V needed (12 is our answer)
'''




'''
This is really hard! I recommend you to watch THE VIDEO LINKED BELOW to get some hints on how to solve this problem.
'''