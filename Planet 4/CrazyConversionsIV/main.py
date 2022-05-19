# READ INSTRUCTIONS.PY BEFORE STARTING THIS PROBLEM

def crazy_conversions_4(sentence):
  '''
  The sentence parameter is a string with the untranslated message

  Return a string with the translated sentence
  '''
  translated_sentence = ""
  reverse_word = []
  word_reversed = []

  #write code here
  for word in sentence:
    reverse_word.append(word[::-1])
  translated_sentence = " ".join(reverse_word[::-1])
    
  return translated_sentence
    
#DO NOT TOUCH THE CODE BELOW

print(crazy_conversions_4(['MIH', 'TSNIAGA', 'EGNEVER', 'TNAW', 'EW', 'DNA', 'SENORD', 'FO', 'YMRA', 'SIH', 'HTIW', 'SNAVARAC', 'RUO', 'DEDIAR', 'NURAH']))
