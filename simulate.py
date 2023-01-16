import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
 
p.loadSDF("world.sdf")
p.setGravity(0,0,-9.8)

planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

backAmplitude = numpy.pi/4
backFrequency = 10
backPhaseOffset = 0

frontAmplitude = numpy.pi/4
frontFrequency = 7
frontPhaseOffset = numpy.pi/4

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
frontTargetAngles = numpy.sin((numpy.linspace(0, 2*numpy.pi, 1000)*frontFrequency)+frontPhaseOffset)*(frontAmplitude)
backTargetAngles = numpy.sin((numpy.linspace(0, 2*numpy.pi, 1000)*backFrequency)+backPhaseOffset)*(backAmplitude)


for i in range(1000):
    p.stepSimulation()
    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")
    backLegSensorValues[i] = backLegTouch
    frontLegSensorValues[i] = frontLegTouch
    pyrosim.Set_Motor_For_Joint(

    bodyIndex = robotId,

    jointName = b'Torso_BackLeg',

    controlMode = p.POSITION_CONTROL,

    targetPosition = backTargetAngles[i],

    maxForce = 500)
    pyrosim.Set_Motor_For_Joint(

    bodyIndex = robotId,

    jointName = b'Torso_Frontleg',

    controlMode = p.POSITION_CONTROL,

    targetPosition = frontTargetAngles[i],

    maxForce = 500)
    time.sleep(1/60)
numpy.save('data/backLegSensorValues.npy', backLegSensorValues)
numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues)
p.disconnect()