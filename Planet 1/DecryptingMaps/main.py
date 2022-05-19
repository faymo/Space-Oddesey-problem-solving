# READ INSTRUCTIONS.PY BEFORE STARTING THIS PROBLEM
def translating_map(proxima_text):
  '''
  proxima_test represents a string in Ancient Proxima language

  The function must return a string representing the translation of the Proxima text into English text. 

  USE THE ALPHABET VARIABLE TO HELP WITH YOUR CODE!
  '''
  english_text = ""
  alphabet = "abcdefghijklmnopqrstuvwxyzab" #added "a" and "b" to the end to deal with "y" and  "z"

  #write code here
  for x in proxima_text:
    if x == " " or x == ".":
      english_text = english_text + x
    else:
      alphabetindex = alphabet.index(x) + 2
      english_text = english_text + alphabet[alphabetindex]
  return english_text


#DO NOT TOUCH THE CODE BELOW
text = "em rm qwlrgl pmyb ylb kmtc dmpuypb dmp rcl kgjcq. rfcl ryic y pgefr rspl lcyp rfc eyq qryrgml ylb em lmprfcyqr dmp ypmslb rum kgjcq. wms ugjj dglb y qsqngagmsq aytc jcybgle rm rfc fgbcmsr md bp. jgzcprw."
print(translating_map(text))