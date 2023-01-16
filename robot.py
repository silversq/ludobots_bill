from motor import MOTOR
from sensor import SENSOR
import pyrosim.pyrosim as pyrosim
import pybullet as p
class ROBOT:
    def __init__(self):

        self.robotId = p.loadURDF("body.urdf")
    
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def SENSE(self, t):
        for i in self.sensors.values():
            i.Get_Value(t)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, t):
        for i in self.motors.values():
            i.Set_Value(self.robotId, t)

        