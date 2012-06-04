from PIL import Image
from glitches import *
from audio import *
from util import *
import time

# Settings
fps = 12
max_freq = 2000
min_freq = 100
out_folder = os.getcwd()+'/run_'+str(int(time.time()))+"/"
wave_file = 'test3.wav'

ensure_dir(out_folder)

im = Image.open("test2.jpg")

image_string = im.tostring()

wave_object = loadwav(wave_file)
frame_length = get_frame_length(wave_object[0], fps)
sample_length = get_sample_length(wave_object[0])

iterations = (len(wave_object[1])/frame_length)-1

t = time.time()

for i in range(iterations):
  
  if i % 10 == 0: 
    print "t: %.3f" % (float(i)*(frame_length*float(sample_length)))
    print "calc. time: ", time.time() - t

  new_image_list = list(image_string)
  
  signal = wave_object[1][i*frame_length:(i+1)*frame_length]
  f_s = get_strongest_frequencies(signal, sample_length, max_freq, min_freq, 20)

  #new_image_list = offset_sequence_mutations(new_image_list, f_s, 80000, max_freq, min_freq)
  new_image_list = random_sequence_mutations(new_image_list)
  new_image_list = block_repositioning(new_image_list, f_s, 900000, max_freq, min_freq)
  new_image_string = "".join(new_image_list)

  new_image = Image.fromstring(im.mode, im.size, new_image_string)
  new_image.save(out_folder+"/im_"+str(i).zfill(6)+".jpg" , "JPEG")

make_movie(out_folder, wave_file, framerate=str(fps))

#new_image_list = random_sequence_mutations(new_image_list)
#new_image_list = random_shuffle_sequence_mutations(new_image_list)
#new_image_list = random_block_repositioning(new_image_list)
