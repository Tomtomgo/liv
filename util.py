import os

def ensure_dir(f):
  d = os.path.dirname(f)
  if not os.path.exists(d):
      os.makedirs(d)

def make_movie(folder, audio_file, vcodec='copy', framerate='24'):
	cmd = "ffmpeg -r "+framerate+" -b 1800 -vcodec "+vcodec+\
	" -i "+folder+"/im_%06d.jpg -i "+audio_file+" "+folder.rstrip("/")+".avi -newaudio"
	os.system(cmd)

	print "WROTE TO "+folder.rstrip("/")+".avi"