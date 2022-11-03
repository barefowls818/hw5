#import necessary materials
import numpy
from numpy import sin,cos
import math
#set number of points ("darts") for hit or miss method
N=1000000
#set coordianted using uniform random distribution from -1 to 1 with N coordinates
x = numpy.random.uniform(low= -1, high=1, size = [N,1])
y = numpy.random.uniform(low= -1, high=1, size = [N,1])
#create function defining interior of circle A=pi*r**2 = pi
f = x**2 + y**2 <1
#mult by 4 because f only gives 1/4 circle
mypi = 4*numpy.sum(f)/N
#print results
print('pi: {}, guess: {}'.format(numpy.pi, mypi))
