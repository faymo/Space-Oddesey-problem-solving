# READ INSTRUCTIONS.PY BEFORE STARTING THIS PROBLEM

def puzzle(words):
  ''' 
  Words is a parameter that represents the groups of random words from the safety hint card

  The function must return a string representing the matching letters from each of the groups that will form a sentence
  '''
  safety_override_sentence = ""
  #write code here
  for pair in words:
    for char in pair[0]:
      if char in pair[1]:
        safety_override_sentence = safety_override_sentence + char
  return safety_override_sentence


#DO NOT TOUCH THE CODE BELOW

words_list = [('hackworks', 'witch'), ('whirl', 'wistful'), ("life", "lad"), ('forget', 'werwolf'), ('over', 'vault'), ('earn', 'rest'), ('rule', 'neutral'), ('throne', 'sketchy'), ('grail', 'jetlag'), ('laxly', 'anxiety')]

print(puzzle(words_list))