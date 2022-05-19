#READ INSTRUCTIONS.PY BEFORE STARTING

def drone_dev(video_output):
  ''' 
  The parameter video_output is the list of matrices, with each matrix representing a certain 3x3 frame in which the drone will assess the DANGER score of.

  The function must return the total lasers from the drone fired based on the video.
  '''
  total_shots = 0
  danger_score = 0

  #write code here
  for m in video_output:
    for l in m:
      for s in l:
        if s == True:
          danger_score += 1
    if danger_score > 3:
      total_shots += 1
    danger_score = 0
  return total_shots



#DO NOT CHANGE THE CODE BELOW
from random import seed, randint
seed(25565)


video = [[[True if randint(1,2) == 2 else False for k in range(3)] for j in range(3)] for i in range(10)]
print(f"{drone_dev(video)} lasers were shot.")