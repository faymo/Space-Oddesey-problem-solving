'''
Arabaro Challenge #2: CrazyConversionsIII

Why is this happening to you. When you can finally help out Commander Kaif, when he finally needs you...and now you're stuck in the middle of a native Arabarian camp with people yelling at you in a language you don't even know. However, thanks to Decrypting School (you've gotten pretty good at it), you know the algorithm to convert their language into one you can understand.

You must configure your translator to reverse the Arbarian speech. However, it is taboo for Arbarian's to speak words with even letter length, so they always tend to always add one grunt,represented by an underscore (_), at the end of their words to make all of their words odd.

Create an algorithm to convert Arbarian language to one you can understand.
'''


arabaro_speech1 = "esaelp_ pleh_ mih"
'''
Example #1:

Let's go through the words step by step:

Word 1: We see there is a grunt (_) at the end, so we remove it to get "esaelp". Then we reverse the word to get "please"

Word 2: We see there is a grunt (_) at the end, so we remove it to get "pleh". Then we reverse the word to get "help"

Word 3: We see there is NOT a grunt (_) at the end, so we simply reverse it to get "him"


The message is "please help him"
'''


arabaro_speech1 = "uoy era elbirret_"
'''
Example #1:

Let's go through the words step by step:

Word 1: We see there is NOT a grunt (_) at the end, so we simply reverse it to get "you"

Word 2: We see there is NOT a grunt (_) at the end, so we simply reverse it to get "are"

Word 3: We see there is a grunt (_) at the end, so we remove it to get "elbirret". Then we reverse the word to get "terrible"


The message is "you are terrible"
'''




#READ INSTRUCTIONS.PY BEFORE STARTING

def translate_arabarian(speech):
	''' 
	speech (string) represents the speech of the Arabarian chieftan.

	The function must return the converted speech from Arabarian to a language you can understand
	'''
	converted_speech = ""

	#write code here

	return converted_speech

#DO NOT CHANGE THE CODE BELOW
arabarian_speech = "uoy era elbirret_"
print(f"The converted speech is {translate_arabarian(arabarian_speech)}")