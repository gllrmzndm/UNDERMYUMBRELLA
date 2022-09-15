from sense_hat import SenseHat
import numpy
import pyaudio
import math
from time import sleep
chunk=1024

def loudness(chunk):
 data = numpy.array(chunk, dtype=float) / 32768.0
 ms = math.sqrt(numpy.sum(data ** 2.0) / len(data))
 if ms < 10e-8: ms = 10e-8
 return 10.0 * math.log(ms, 10.0)