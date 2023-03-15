import numpy 

numberOfGenerations = 5
populationSize = 5

motorJointAngle = 0.7
nSteps = 1000
randomSeed = 10

numSensorNeurons = 1
numMotorNeurons = 1
backAmplitude = numpy.pi/4
backFrequency = 10
backPhaseOffset = 0

frontAmplitude = numpy.pi/4
frontFrequency = 7
frontPhaseOffset = numpy.pi/4

backLegSensorValues = numpy.zeros(nSteps)
frontLegSensorValues = numpy.zeros(nSteps)
frontTargetAngles = numpy.sin((numpy.linspace(0, 2*numpy.pi, nSteps)*frontFrequency)+frontPhaseOffset)*(frontAmplitude)
backTargetAngles = numpy.sin((numpy.linspace(0, 2*numpy.pi, nSteps)*backFrequency)+backPhaseOffset)*(backAmplitude)