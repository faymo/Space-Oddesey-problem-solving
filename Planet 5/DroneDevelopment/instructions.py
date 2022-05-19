'''
YCW Space Station Task #2: DroneDevelopment

There are drones to your left, drones to your right. The sounds of lasers are screaming around your head. Your senses are sharp, and you have to be quick and nimble in order to dodge the lasers. You can't get closer to the control room without some backup!

You decide to quickly program a couple of simple drones to stall for time. These drones are programmed to see a matrix in front of them, of constant size 3x3. Each cell in the matrix is either False for NO DANGER or True for DANGER. The drone will decide to fire ONLY IF more than 3 squares are considered DANGER.

You will be given a list of matrices in the form of a variable VIDEO_OUTPUT. Loop through each frame of the video and count how many times the drone has fired. This will possibly be the toughest challenge out of them all.
'''


video_output = [
	[
		[True, True, True],
		[True, True, True],
		[False, False, True],
	],
	[
		[True, True, False],
		[False, False, True],
		[False, False, True],
	],
	[
		[True, False, False],
		[False, False, False],
		[False, False, True],
	],
	[
		[False, False, False],
		[False, False, False],
		[False, False, False],
	],
]
'''
Example 1: 

The video output is a list of matrices (or 2-D list). Each matrix represents the danger rating at that point of the video. 

1.) Matrix 1 has 7 DANGERs, which is MORE than 3 DANGERs, therefore it shoots a laser
2.) Matrix 2 has 4 DANGERs, which is MORE than 3 DANGERs, therefore it shoots a laser
3.) Matrix 3 has 2 DANGERs, which is LESS than 3 DANGERs, therefore it DOES NOT shoots a laser
4.) Matrix 4 has 0 DANGERs, which is LESS than 3 DANGERs, therefore it DOES NOT shoots a laser

There were a total of 2 lasers shot!
'''