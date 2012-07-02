import os

def ensure_dir(f):
  d = os.path.dirname(f)
  if not os.path.exists(d):
      os.makedirs(d)

def cleanup(folder):
  for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
      os.unlink(file_path)
    except Exception, e:
      print e

def format_time(seconds):
  milliseconds = ("%.f"%(seconds-int(seconds)))[2:]
  seconds = int(seconds)
  hours = seconds / 3600
  seconds -= 3600*hours
  minutes = seconds / 60
  seconds -= 60*minutes
  
  return "%02d:%02d:%02d.%s" % (hours, minutes, seconds, milliseconds)

def make_movie(folder, audio_file, vcodec='copy', framerate='24'):
	cmd = "ffmpeg -r "+framerate+" -b 1800 -vcodec "+vcodec+\
	" -i "+folder+"/im_%06d.jpg -i "+audio_file+" "+folder.rstrip("/")+".avi -newaudio"
	os.system(cmd)

	print "WROTE TO "+folder.rstrip("/")+".avi"

def split_video(folder, video, fps):
  cmd ="ffmpeg -i "+folder+video+" -r "+str(fps)+" -f image2 "+folder+"image-%07d.png"
  os.system(cmd)

def convert_to_avi(folder, video):
  cmd ="ffmpeg -i "+folder+video+" "+folder+video[:len(video)-4]+".avi"
  os.system(cmd)

def chop_sequence(folder, video, out_name, start, duration):
  ensure_dir(folder+"/pieces/")  
  cmd = "ffmpeg -ss "+start+" -t "+duration+" -i "+folder+video+" -acodec copy -vcodec copy -async 1 "+folder+"pieces/"+out_name
  os.system(cmd)

def merge_sequence(out_list, out_name):
  cmd = "ffmpeg -i concat:\""+out_list+"\" "+out_name
  os.system(cmd)
