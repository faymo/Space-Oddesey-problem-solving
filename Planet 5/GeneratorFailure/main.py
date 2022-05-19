#READ INSTRUCTIONS.PY BEFORE STARTING

def generator(circuit):
  ''' 
  The parameter circuit represents a string with Xs and Os (for example "XOXXXO")

  The function must return the amount of excess voltage you need to power the generator. (So 15 minus the power in the circuit)
  '''
  current_power = 0
  current_three = ""

  #write code here
  for char in circuit:
    current_three = current_three + char
    if len(current_three) > 3:
      current_three = current_three[1:]
    if current_three == "XXX":
      current_power += 1
  return 15-current_power

#DO NOT CHANGE THE CODE BELOW
print(f"We need {generator('XXXXXXXOXOXOOOOXOXOOXXXXOXXXOXXOOXOXXXOXOXOXOOOXOOXXXOXXOXXXOXOXOXOXXXOXOXOXOOXOOXOXO')}V more power.")