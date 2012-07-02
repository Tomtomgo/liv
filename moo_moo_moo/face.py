import sys, os
from util.util import *
from cv import *
from PIL import Image
import glob

def detectObjects(image):
  """Converts an image to grayscale and prints the locations of any 
     faces found"""
  grayscale = CreateImage((image.width, image.height), 8, 1)
  CvtColor(image, grayscale, CV_BGR2GRAY)
  
  storage = CreateMemStorage()
  #ClearMemStorage(storage)
  EqualizeHist(grayscale, grayscale)

  cascade = Load(
    '/home/tom/Projects/liv/moo_moo_moo/haarcascade_frontalface_default.xml')

  faces = HaarDetectObjects(grayscale, cascade, storage, 1.2, 2,
                             CV_HAAR_DO_CANNY_PRUNING, (50,50))

  positions = []

  if faces:
    positions = [(f[0][0], f[0][1], f[0][2], f[0][3]) for f in faces]
  
  return positions

def find_face_points(folder,video, fps):

  # Split video into images
  # split_video(folder,video,fps)

  im_list = glob.glob(folder+'*.png')
  faces = dict()

  for f in im_list:
    # Load image
    image = LoadImage(f);

    # Get the positions of the faces
    positions = detectObjects(image)

    # And store the number of faces
    faces[f] = len(positions)

  return faces

def find_faces_and_replace(in_file, replace_file):
  
  # Load image
  main_image = LoadImage(in_file);

  # Get the positions of the faces
  positions = detectObjects(main_image)  
  
  # Open main image
  image = Image.open(in_file)

  # Get the replace face
  face_replace = Image.open(replace_file)

  # Cover every face with the TROLL
  for face in positions:
        
    # Get size and position
    position_xy = (face[0],face[1])
    size = (face[2],face[3])

    # Resize overlay
    f = face_replace.resize(size)

    # Paste
    image.paste(f, position_xy, f)

  image.save(in_file, 'jpeg')
