'''
Proxima Task 1: DecryptMaps

Now that we have money and supplies to officially start this mission, Mr. SaShrey has also provided us with a note from one of Commander Kaif's officials that will tell you where to go next to stop Dr. Liberation. While preparing for this route, you find that the language that the map is written in is completely different! Mr.SaShrey tells you that it is written in Ancient Proximian, which is a weird form of English.

You realize that Ancient Proximian is simply the English language but every character is shifted backward 2 letters. For example, "fgr" in Proximian is "hit" in English:

"h" -> backwards 2 -> "f"
"i" -> backwards 2 -> "g"
"t" -> backwards 2 -> "r"

Write a function that takes in text in Ancient Proximian and returns it in English for you to navigate to Dr. Liberty's base! 

NOTE: ALL TEXT WILL BE IN LOWERCASE!!!
'''




map_text1 = "npmvgky"
'''
Example #1:
Going through each of these 7 characters, we want to shift each of these letters FORWARDS 2 characters (it's important to understand WHY!!!).

"n" -> forwards 2 -> "p"
"p" -> forwards 2 -> "r"
"m" -> forwards 2 -> "o"
"v" -> forwards 2 -> "x"
"g" -> forwards 2 -> "i"
"k" -> forwards 2 -> "m"
"y" -> forwards 2 -> "a"

The word in English is "proxima"! 
Notice the last character was "y". If we went forward two, we would go outside the alphabet. That is why we cycled back to "a" instead!
'''




map_text2 = "zyb"
'''
Example #2
Going through each of these 3 characters, we want to shift each of these letters FORWARDS 2 characters (it's important to understand WHY!!!).

"z" -> forwards 2 -> "b"
"y" -> forwards 2 -> "a"
"b" -> forwards 2 -> "d"

The word in English is "bad"! 
Notice the first and second characters was "z" and "y". If we went two characters forward, we would reach the end of the alphabet! Instead, we cycle back to the beginning. "z" becomes "b" and "y" becomes "a".
'''