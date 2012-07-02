import os, random, time
import math

def determine_new_char(char):
  if random.randint(0,20) == 0:
    return randchar()
  else:
    return char

def randchar():
  return chr(random.randint(0,255))

def randseq(l):
  seq = [randchar() for n in range(l)]
  return "".join(seq)

def offset_seq(seq, offset):
  seq = [chr(ord(n)+offset) if ord(n)+offset <= 255 and ord(n)+offset >= 0 else n for n in seq]
  return seq

def inplace_shift(L, start, length, pos):
    if pos > start + length:
        (a, b, c) = (start, start + length, pos)
    elif pos <= start:
        (a, b, c) = (pos, start, start + length)
    else:
        raise ValueError("Cannot shift a subsequence to inside itself")

    span1, span2 = (b - a, c - b)
    if span1 < span2:
        tmp = L[a:b]
        L[a:a + span2] = L[b:c]
        L[c - span1:c] = tmp
    else:
        tmp = L[b:c]
        L[a + span2:c] = L[a:b]
        L[a:a + span2] = tmp

def random_shuffle_sequence_mutations(im_list):
  n = 0

  # shuffle sequence mutations
  while n < 50:
    if random.randrange(0,10) == 1:
      mutation_length = random.randrange(1,5000)
      mutation_position = random.randrange(0,len(im_list)-1)
      sequence = im_list[mutation_position:(mutation_position+mutation_length)]
      random.shuffle(sequence)
      im_list[mutation_position:(mutation_position+mutation_length)]=sequence
      
    n+=1

  return im_list

def random_sequence_mutations(im_list):
  n = 0

  # shuffle sequence mutations
  while n < 50:
    if random.randrange(0,10) == 1:
      mutation_length = random.randrange(1,int(len(im_list)/200))
      mutation_position = random.randrange(0,len(im_list)-1)
      im_list[mutation_position:(mutation_position+mutation_length)]=randseq(mutation_length)
      
    n+=1

  return im_list

def random_offset_sequence_mutations(im_list):
  n = 0

  # shuffle sequence mutations
  while n < 50:
    if random.randrange(0,2) == 1:
      mutation_length = random.randrange(1,int(len(im_list)/20))
      mutation_position = random.randrange(0,len(im_list)-mutation_length)
      offset_strength = random.randrange(0,250)-125
      seq = im_list[mutation_position:(mutation_position+mutation_length)]
      s2 = offset_seq(seq,offset_strength)
      
      im_list[mutation_position:(mutation_position+mutation_length)]= s2
      
    n+=1

  return im_list

def offset_sequence_mutations(im_list, mutation_list, treshold, max_freq, min_freq):
  
  # mutation_list[n] = (frequency, strength)
  
  # Get image list length
  im_list_l = len(im_list)

  # Get max-min frequency difference
  freq_diff = max_freq - min_freq
  
  # Do the mutations
  for mutation in mutation_list:
    
    # If below treshold
    if mutation[1] > treshold:

      # Calculate mutation length by strength TODO NORMALIZE?
      mutation_length =  int(math.log(mutation[1])**3)*500
      
      # Normalize frequency
      norm_freq = mutation[0]/freq_diff

      # Get position in image
      mutation_position = int(norm_freq * (im_list_l - mutation_length))

      # Strength of offset
      offset_strength = int((norm_freq * 510) - 255)

      # Get sequence
      seq = im_list[mutation_position:(mutation_position+mutation_length)]

      # Offset it
      im_list[mutation_position:(mutation_position+mutation_length)] = offset_seq(seq,offset_strength)

    else:
      
      # Assume list ordered on strength, if below treshold,FAILS
      break

  return im_list

def block_repositioning(im_list, mutation_list, treshold, max_freq, min_freq):

  # Get image list length
  im_list_l = len(im_list)

  # Get max-min frequency difference
  freq_diff = max_freq - min_freq

  # Do the mutations
  for mutation in mutation_list:
    
    # If below treshold
    if mutation[1] > treshold:

      # Calculate mutation length by strength TODO NORMALIZE?
      mutation_length =  int(math.log(mutation[1])**3)*5
      
      # Normalize frequency
      norm_freq = mutation[0]/freq_diff

      # Strength of offset
      offset_strength = int((norm_freq * 510) - 255)

      # Get position in image
      mutation_position = int(norm_freq * (im_list_l - mutation_length))
      to_position = mutation_position+1

      while to_position > mutation_position and to_position <= mutation_position+mutation_length:
        to_position = random.randrange(0,len(im_list)-mutation_length,1)

      # Get sequence
      seq = im_list[mutation_position:(mutation_position+mutation_length)]

      inplace_shift(im_list, mutation_position, mutation_length, to_position)

    else:

      # Assume list ordered on strength, if below treshold,FAILS
      break

  return im_list

def random_block_repositioning(im_list):

  n = 0

  # random block repositioning
  while n < 100:
    if random.randrange(0,10) == 1:
      mutation_length = random.randrange(1,int(len(im_list)/1.1))

      from_position = random.randrange(0,len(im_list)-1,1)
      to_position = from_position+1

      while to_position > from_position and to_position <= from_position+mutation_length:
        to_position = random.randrange(0,len(im_list)-mutation_length,1)

      inplace_shift(im_list, from_position, mutation_length, to_position)

    n+=1

  return im_list