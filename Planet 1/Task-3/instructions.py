'''
You have finally arrived at the hideout of Dr. Liberty. You see androids moving on and about, and a lot of crates filled with goods. As you try to investigate the place via stealth, you come across an annoying door. The door has a faded logo on it that you just can't quite make out. "H...something...W"

You hear androids nearby. You have to hurry! There is a security terminal asking for the correct password to open the door. Luckily, you were told by Mr. SaShrey some intel on how these passwords work, which he wrote down on a note.

The note gives you a couple of steps to decrypt the password on the security terminal. Based on the seven-letter code on top of the door, you must do these steps:

1.) Arrange all letters alphabetically
2.) Convert each letter into a number corresponding to its place on the alphabet (i.e "a" is 1, "b" is 2, "z" is 26)
3.) Multiply each number of the code by its position (i.e first letter * 1, second letter * 2, and so on)
4.) Return the code seperated by dashes (as a string) 
'''

door_code1 = "ABCDABC"
'''
Example #1:
Let's do this in steps.

1.) Sorting this alphabetically would result in "AABBCCD"

2.) Converting each letter to its corresponding number as mentioned in step 2 would result in something like [1,1,2,2,3,3,4]

3.) Applying the third step would result in a list like [1*1,1*2,2*3,2*4,3*5,3*6,4*7]. This would simplify to [1,2,6,8,15,18,28]

4.) Return a string with code seperated by dashes: "1-2-6-8-15-18-28"
'''


door_code2 = "ALKWSAAS"
'''
Example #2:

1.) Sorting this alphabetically would result in aklssw "AAAKLSSW"

2.) Converting each letter to its corresponding number as mentioned in step 2 would result in something like [1,11,12,19,19,23]

3.) Applying the third step (count the number of each letter, 3 a's, 4 t's) would result in a list like [1*1,11*1,19*2,23*1]. This would simplify to [1,11,12,38,23]

4.) Return a string with code seperated by dashes: "1-11-12-38-23"
'''