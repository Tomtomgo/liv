from PIL import Image
from moo_moo_moo.face import *
from moo_moo_moo.animator import *
from util.util import *
from cv import *
import time
import glob
import pickle
import operator

# Settings
out_fps = 24
out_folder = os.getcwd()+'/tmp/run_'+str(int(time.time()))+"/"
out_length = 10
analyze_fps = 0.5


def go_moo(vid):
  '''
  # Go get video
  cmd = "python util/youtube-dl.py "+args[1]
  os.system(cmd)

  f = glob.glob('*.mp4')

  # Video downloaded and stored
  if len(f) > 0:
    f = f[0]
    
    # Move the file
    ensure_dir(out_folder)
    new_location = out_folder+f
    os.rename(f, new_location)

    find_face_points(out_folder, f)
      
  else:
    print "Video downloading failed."   
  '''
  
  #faces = find_face_points("tmp/run_1341256821/", "EaVpjQuZgcg.mp4", analyze_fps)
  #f = open('test.pickle','w+')
  #pickle.dump(faces, f)
  #f.close()
  ''
  f = open('test.pickle','r')
  faces = pickle.load(f)
  f.close()

  # Order by number of faces
  faces = sorted(faces.iteritems(), key=operator.itemgetter(1))
  
  # Descending  
  faces.reverse()

  # Get a script for our movie
  script = make_script(faces, out_length)

  # Convert to AVI for good cutting
  #convert_to_avi("tmp/run_1341256821/", "EaVpjQuZgcg.mp4")

  # Make the animation
  animate(script, out_fps, analyze_fps, "tmp/run_1341256821/", "EaVpjQuZgcg.avi")

  # Destroy old files
  cleanup("/tmp")

if __name__ == '__main__':
  args = sys.argv
  
  # Get arguments
  if len(args) > 1:
    
    go_moo(args[1])

  else:
    print "No video given."

  exit(0)