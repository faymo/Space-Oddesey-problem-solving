#READ INSTRUCTIONS.PY BEFORE STARTING

def location_to_land(locations):
  ''' 
  locations is a parameter representing a list of locations. Each location in the list is in the form (NUM_TREES, NUM_BUSHES). Both trees and bushes are integers.

  The function must return the index in the locations list that has the lower danger_score
  '''
  danger_score = 0
  best_location = 0
  current_position = 0
  
  #write code here
  for location in locations:
    NUMBER_OF_TREES = location[0]
    NUMBER_OF_BUSHES = location [1]
    DANGER_SCORE = 5 * NUMBER_OF_TREES + 2 * NUMBER_OF_BUSHES
    if DANGER_SCORE >= current_position:
      current_position = DANGER_SCORE
      best_location = locations.index(location)
  return best_location

#DO NOT CHANGE THE CODE BELOW
from random import randint as ri
from random import seed
seed(25565)
locations = [(ri(1,50), ri(1,50)) for i in range(25)]
print(f"Best position to land is at position {location_to_land(locations)}")
locations1 = [(5,1),(3,5),(1,10)]
print(location_to_land(locations1))