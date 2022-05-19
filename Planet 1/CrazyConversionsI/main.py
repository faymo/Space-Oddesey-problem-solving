# READ INSTRUCTIONS.PY BEFORE STARTING THIS PROBLEM

def crazy_conversions(YCWSS):
  '''
	YCWSS is a parameter that represents the amount of YCWSS currency you have

	The function must return a float (with only two numbers past the decimal point) representing YCWSS being converted to PX (Proxima Currency)
  '''
  ig_currency = 0
  px_currency = 0

  #write code here
  ig_currency = 6.23 * YCWSS
  px_currency = ig_currency * 0.79
  px_currency = round(px_currency, 2)
  return px_currency




#DO NOT TOUCH THE CODE BELOW
from random import randint, seed
seed(25565)
current_ycwss_currency = randint(50,300)
print(f"You have {current_ycwss_currency} YCWSS!\nThis is equivalent to {crazy_conversions(current_ycwss_currency)} PX!")

