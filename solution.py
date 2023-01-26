import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myId = nextAvailableID
        self.weights = numpy.random.rand(3,2)
        self.weights = self.weights*2-1
    
    def Set_ID(self):
        pass
    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system('start /B py simulate.py ' + directOrGUI + ' ' + str(self.myId))

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myId) + ".txt"):
            time.sleep(0.01)
        f = open("fitness" + str(self.myId) + ".txt", "r")
        self.fitness = float(f.read())
        f.close()
        os.system("del fitness" + str(self.myId) + ".txt")

    def Mutate(self):
        randrow = random.randint(0, 2)
        randcol = random.randint(0, 1)
        self.weights[randrow, randcol] = random.random()*2-1
    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        length = 1
        width = 1
        height = 1
        pyrosim.Send_Cube(name="Box", pos=[1,2,0.5] , size=[length,width,height])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_SDF("world.sdf")
        length = 1
        width = 1
        height = 1
        pyrosim.Send_Cube(name="Box", pos=[1,2,0.5] , size=[length,width,height])
        pyrosim.End()

        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1.5] , size=[length,width,height])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0.5,0,1])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [-0.5,0,1])
        pyrosim.Send_Cube(name="BackLeg", pos=[0.5,0,-0.5] , size=[length,width,height])
        pyrosim.Send_Cube(name="FrontLeg", pos=[-0.5,0,-0.5] , size=[length,width,height])
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myId) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
        for currentRow in [0, 1, 2]:
            for currentColumn in [0, 1]:
                pyrosim.Send_Synapse( sourceNeuronName = currentRow, targetNeuronName = currentColumn+3, weight = self.weights[currentRow][currentColumn])

        pyrosim.End()