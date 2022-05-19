'''
Proxima Challenge #4: JetpackAttack

Congradulations on cracking the code to the office! Now to do some more investigating...

After discovering Dr. Liberty's office and coming face to face with him, He quickly escapes with a jetpack soaring in the sky and leaving you in the office! You must find a way to get out of there before the real guards show up and you need to track down Dr.Liberty before he gets away! 

There's a safety card on the desk that has an encrypted hint and your job is to solve it using your python knowledge. The weird thing is that the hint only has a bunch of random words written in groups...hmmm. 

In order to disable Dr. Liberty's jetpack to send him flying to the floor, your job is to look through each of the groups of words and find the common letter(s) that match the main word and combine all the letters together to form a sentence. 
'''

encrypted_word_group1 = [("hippo", "hat"), ("pine", "flick")]
'''
Example #1:

Let's separate these into 2 groups of words:
1. "hippo" and "hat"

"hippo" and "hat" has the letter "h" in common

2. "pine" and "flick"

"pine" and "flick" has the letter "i" in common

Therefore the secret message is "hi".
'''

encrypted_word_group2 = [("ballroom", "basket"), ("tide", "day")]
'''
Example #2:

Let's separate these into 2 groups of words:
1. "ballroom" and "basket"

"ballroom" and "basket" has the letters "b" and "a" in common

2. "tide" and "day"

"tide" and "day" has the letter "d" in common

Therefore the secret message is "bad".
'''