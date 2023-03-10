import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myId = nextAvailableID
        self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons)
        self.weights = self.weights*2-1
    
    def Set_ID(self, iD):
        self.myId = iD
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
        randrow = random.randint(0, c.numSensorNeurons-1)
        randcol = random.randint(0, c.numMotorNeurons-1)
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
        pyrosim.End()

        pyrosim.Start_URDF("body.urdf")
        self.random_links = []
        self.number_links = random.randint(5, 12)
        for i in range(self.number_links):
            if random.random() < 0.5:
                self.random_links.append(1)
            else:
                self.random_links.append(0)
        width = 1
        if self.random_links[0] == 0:
            pyrosim.Send_Cube(name="Cube0", pos=[0,0,1] , size=[length,width,height], color="Green", rgb = "0 1.0 0.0 1.0")
        else:
            pyrosim.Send_Cube(name="Cube0", pos=[0,0,1] , size=[length,width,height], color="Cyan", rgb = "0 1.0 1.0 1.0")

        pyrosim.Send_Joint(name="Cube0_Cube1", parent="Cube0", child="Cube1", type="revolute", position = [0,width/2, 1], jointAxis="1 0 1")
        if self.random_links[0] == 0:
            pyrosim.Send_Cube(name="Cube1", pos=[0,width/2,0] , size=[length,width,height], color="Green", rgb = "0 1.0 0.0 1.0")
        else:
            pyrosim.Send_Cube(name="Cube1", pos=[0,width/2,0] , size=[length,width,height], color="Cyan", rgb = "0 1.0 1.0 1.0")
        for i in range(2,self.number_links):
            prev_width = width
            length = random.random()+0.3
            width = random.random()+0.3
            height = random.random()+0.2
            if self.random_links[i] == 1:
                pyrosim.Send_Cube(name="Cube"+str(i), pos=[0,width/2,0] , size=[length,width,height], color="Cyan", rgb="0 1.0 1.0 1.0")
            else:
                pyrosim.Send_Cube(name="Cube"+str(i), pos=[0,width/2,0] , size=[length,width,height], color="Green", rgb="0 1.0 0.0 1.0")
            pyrosim.Send_Joint(name="Cube"+str(i-1)+"_"+"Cube"+str(i), parent="Cube"+str(i-1), child="Cube"+str(i), type="revolute", position = [0,prev_width+0.1, 0], jointAxis="1 0 1")
        # pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0, -0.5, 1], jointAxis = "1 0 0")
        # pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")
        # pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-0.5,0,1], jointAxis = "0 1 0")
        # pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [0.5,0,1], jointAxis = "0 1 0")
        # pyrosim.Send_Joint( name = "BackLeg_LowerBackLeg" , parent= "BackLeg" , child = "LowerBackLeg" , type = "revolute", position = [0, -1, 0], jointAxis = "0 1 1")
        # pyrosim.Send_Joint( name = "FrontLeg_LowerFrontLeg" , parent= "FrontLeg" , child = "LowerFrontLeg" , type = "revolute", position = [0, 1, 0], jointAxis = "0 1 1")
        # pyrosim.Send_Joint( name = "LeftLeg_LowerLeftLeg" , parent= "LeftLeg" , child = "LowerLeftLeg" , type = "revolute", position = [-1, 0, 0], jointAxis = "0 1 1")
        # pyrosim.Send_Joint( name = "RightLeg_LowerRightLeg" , parent= "RightLeg" , child = "LowerRightLeg" , type = "revolute", position = [1, 0, 0], jointAxis = "0 1 1")

        # pyrosim.Send_Cube(name="LowerBackLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1], color="Green", rgb="0 1.0 0 1.0")
        # pyrosim.Send_Cube(name="LowerFrontLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])
        # pyrosim.Send_Cube(name="LowerLeftLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])
        # pyrosim.Send_Cube(name="LowerRightLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])

        # pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0] , size=[0.2,1,0.2])
        # pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0] , size=[0.2,1,0.2])
        # pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5,0,0] , size=[1,0.2,0.2])
        # pyrosim.Send_Cube(name="RightLeg", pos=[0.5,0,0] , size=[1,0.2,0.2])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myId) + ".nndf")
        neurons = 0
        for i in range(len(self.random_links)):
            if self.random_links[i] == 0:
                pyrosim.Send_Sensor_Neuron(name = neurons, linkName = "Cube"+str(i))
                neurons += 1
        sensors = neurons
        c.numSensorNeurons = sensors
        motors = 0
        for i in range(len(self.random_links)):
            if self.random_links[i] == 0:
                if i != 0:
                    pyrosim.Send_Motor_Neuron( name = neurons , jointName = "Cube"+str(i-1)+"_"+"Cube"+str(i))
                    neurons += 1
                    motors += 1
        print("sensors: " + str(sensors))
        print("motors: " + str(motors))
        c.numMotorNeurons = motors
        self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons)
        self.weights = self.weights*2-1
        # pyrosim.Send_Motor_Neuron( name = 5 , jointName = "Torso_FrontLeg")
        # pyrosim.Send_Motor_Neuron( name = 6 , jointName = "Torso_LeftLeg")
        # pyrosim.Send_Motor_Neuron( name = 7 , jointName = "Torso_RightLeg")
        # pyrosim.Send_Motor_Neuron( name = 8 , jointName = "RightLeg_LowerRightLeg")
        # pyrosim.Send_Motor_Neuron( name = 9 , jointName = "LeftLeg_LowerLeftLeg")
        # pyrosim.Send_Motor_Neuron( name = 10 , jointName = "BackLeg_LowerBackLeg")
        # pyrosim.Send_Motor_Neuron( name = 11 , jointName = "FrontLeg_LowerFrontLeg")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow, targetNeuronName = currentColumn+sensors, weight = self.weights[currentRow][currentColumn])

        pyrosim.End()