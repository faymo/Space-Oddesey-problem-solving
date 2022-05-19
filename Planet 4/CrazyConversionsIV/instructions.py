'''
District of Krieg Task #2: CrazyConversionsIV

Finally! After walking back and forth, collecting clues and resources, you find a large underground cellar. Inside, you see an astonishing sight. It's ALL the townsfolk that were missing!  After breaking into the lock, the sheriff greets you. 

"SU GNIVAS ROF UOY KNAHT"

Once again, we have another language on our hands. However, you already know how to decipher this language thanks to your friend Shriya. It's a special type of palindrome, where you not only have to reverse the whole sentence, but also each word in the sentence. 

Create a program that when given a SENTENCE as a string, will return the TRANSLATED_SENTENCE as a string.
'''

sentence = ["SU" ,"GNIVAS", "ROF", "UOY" , "KNAHT"]
'''
Example #1:

Let's try  to decode the message above using 2 steps:

1. First we reverse each word
SU -----------> US 
GNIVAS -------> SAVING  
ROF ----------> FOR 
UOY ----------> YOU 
KNAHT --------> THANK 

2. Then we we reverse the whole sentence:
'US SAVING FOR YOU THANK' = 'THANK YOU FOR SAVING US'
''' 


sentence = ["YADHTRIB", "YPPAH"]
'''
Example #2:

Let's try  to decode the message above using 2 steps (this time in the opposite order):

1. First we reverse the whole sentence
'YADHTRIB YPPAH' = 'YPPAH YADHTRIB'

2.) Then we reverse each word
YPPAH -----------> HAPPY
YADHTRIB --------> BIRTHDAY

'HAPPY BIRTHDAY'
''' 