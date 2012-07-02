from scipy.stats import truncnorm
import random
from util.util import *

def make_script(faces, length):
  
  total_time = 0.0
  script = [] # (frame_index, sample_length, total_length)

  while total_time < length:
    
    # Get a frame
    frame_index = int(truncnorm.rvs(0,1)*len(faces))

    # Decide the sample's length
    sample_length = random.random()/4

    # Decide the total movie's length
    repetitions = int(random.random()*10)

    total_time += (sample_length*repetitions)

    script.append((faces[frame_index][0], sample_length, repetitions))

  return script

def animate(script, out_fps, analyze_fps, out_folder, video):
  
  i = 0
  out_list = ""

  for scene in script:

    # Count
    i+=1

    # Unpack
    frame, sample_length, repetitions = scene
    
    # Get start_time
    start = frame.replace('.png','')
    start = float(start[start.rfind('-')+1:])
    start = start * (1/analyze_fps)

    start = format_time(start)
    duration = format_time(sample_length)

    # Create tempname
    out_name = frame[frame.rfind("/"):]+".mpg"
    
    # Chop it up
    chop_sequence(out_folder, video, out_name, start, duration)

    # Create the list to merge
    for r in range(repetitions):
      out_list += out_folder+"pieces/"+out_name+"|"

  # Remove additional |
  out_list = out_list[:len(out_list)-1]

  ensure_dir("rendered")

  # Make the movie
  merge_sequence(out_list, "rendered/"+video+".avi")