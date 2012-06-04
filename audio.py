from numpy import *
from scipy.io import wavfile

def loadwav(filename, mono=True):
  (sampling_rate,signal_in) = wavfile.read(filename)
  
  if mono:
    signal_in = make_mono(signal_in)

  return (sampling_rate,signal_in)

def make_mono(signal):
  if signal.shape[1] > 1:
    signal = (signal[:, 1] + signal[:, 0]) / 2

  return signal

# Calculate length of frame as number of samples
def get_frame_length(sample_rate, fps):
  frame_length = sample_rate/fps
  return frame_length

# Calculate length of sample in secs
def get_sample_length(sample_rate):
  sample_length = 1/float(sample_rate)
  return sample_length

# Get strongest frequencies in signal
def get_strongest_frequencies(signal, sample_length, max_freq, min_freq, number_of_frequencies):

  try:
    # Do FFT
    fourier = fft.fft(signal)
  except:
    print signal
    print "It was error"
    return

  # Get frequencies
  frequencies = fft.fftfreq(len(signal), sample_length)

  # Cut off top
  fourier = fourier[(frequencies < max_freq)]
  frequencies = frequencies[(frequencies < max_freq)]

  # Cut off low
  fourier = fourier[(frequencies > min_freq)]
  frequencies = frequencies[(frequencies > min_freq)]

  # Get strongest n frequencies
  indices = fourier.argsort()[::-1]
  return [(frequencies[i], abs(fourier[i])) for i in indices[0:number_of_frequencies]]
