'''
District of Krieg Challenge #1: DecryptingMapsII

Desolate...That's the only thing you can think about when you see the rows upon rows of endless empty tents upon the dry, sandy dunes of this planet. As you rumage through the ghost town, you seem to find a map. Here we go again...

This map in particular is one of the weirdest maps you've seen. There is a random word on the top of the map and grid squares marked by numbers from 1-26. After some deduction, you realize that the word maps out a specific path.

You will be given a word as a string. Your job is to convert every character to its numeric equivalent and return a list of integers representing a path on the map (A is 1, B is 2, and so on). The examples can further elaborate!
'''

hint_word1 = 'app'
'''
Example #1:

There's 3 letters in this hint, so the code would produce 3 numbers as the password.

1. A ---> 1st letter in the alphabet
2. P ---> 16th letter in the alphabet
3. P ---> 16th letter in the alphabet

So our password would be: [1, 16, 16]

Hint: If you use the index to find where the letter is in the alphabet remeber indices start count at 0, not 1
'''



hint_word2 = 'attack'
'''
Example #2:

There's 6 letters in this hint, so the code would produce 6 numbers as the password.

1. A ---> 1st letter in the alphabet
2. T ---> 20th letter in the alphabet
3. T ---> 20th letter in the alphabet
4. A ---> 1st letter in the alphabet
5. C ---> 3rd letter in the alphabet
6. K ---> 11th letter in the alphabet

So our password would be: [1, 20, 20, 1, 3, 11]
'''