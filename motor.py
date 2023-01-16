import numpy
import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p
class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()
    
    def Prepare_To_Act(self):
        self.values =  numpy.zeros(1000)
        self.amplitude = c.backAmplitude
        if self.jointName == b'Torso_Frontleg':
            self.frequency = c.backFrequency
        else:
            self.frequency = c.backFrequency / 2

        self.phaseOffset = c.backPhaseOffset
        print(self.jointName)
        self.motorValues = numpy.sin((numpy.linspace(0, 2*numpy.pi, 1000)*self.frequency)+self.phaseOffset)*(self.amplitude)   
    
    def Set_Value(self, robot, i):
        pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = self.jointName, controlMode = p.POSITION_CONTROL, 
                                    targetPosition = self.motorValues[i], maxForce = 500)

    def Save_Values(self):
        numpy.save('data/MotorValues.npy', self.values)
