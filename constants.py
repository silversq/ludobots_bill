import numpy 

numberOfGenerations = 1
populationSize = 1

motorJointAngle = 1
nSteps = 300

numSensorNeurons = 1
numMotorNeurons = 1
backAmplitude = numpy.pi/4
backFrequency = 10
backPhaseOffset = 0

frontAmplitude = numpy.pi/4
frontFrequency = 7
frontPhaseOffset = numpy.pi/4

backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
frontTargetAngles = numpy.sin((numpy.linspace(0, 2*numpy.pi, 1000)*frontFrequency)+frontPhaseOffset)*(frontAmplitude)
backTargetAngles = numpy.sin((numpy.linspace(0, 2*numpy.pi, 1000)*backFrequency)+backPhaseOffset)*(backAmplitude)