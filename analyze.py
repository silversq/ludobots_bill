import numpy
import matplotlib.pyplot as mpl


c = numpy.load('data/backLegSensorValues.npy')
d = numpy.load('data/frontLegSensorValues.npy')

print(c)
line, = mpl.plot(c, label = 'Back Leg')
line2, = mpl.plot(d, label = 'Front Leg')
mpl.legend()

mpl.show()