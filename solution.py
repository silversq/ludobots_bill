import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c
import math

class SOLUTION:
    def __init__(self, nextAvailableID, randomSeed):
        self.myId = nextAvailableID
        numpy.random.seed(randomSeed)
        # self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons)
        # self.weights = self.weights*2-1
        self.numSensorNeurons = 0
        self.numMotorNeurons = 0
        self.sensors = []
        self.motors = []
        self.ctr = 1
        self.storage = {self.myId : [],'Joint': [], 'Sensor': [], 'Motor': []}
        self.lastiD = -1
    def Set_ID(self, iD):
        self.lastiD = self.myId
        self.myId = iD
        # print('\n',self.lastiD, self.myId)
        # print('\n', self.storage)
    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        if len(self.storage[self.myId]) == 0:
            self.Create_Body()
            self.Create_Brain()
        else:
            self.Update_Body()
            self.Update_Brain()
        os.system('start /B py simulate.py ' + directOrGUI + ' ' + str(self.myId))

    def Wait_For_Simulation_To_End(self):
        # print(self.myId)
        while not os.path.exists("fitness_" + str(self.myId) + ".txt"):
            time.sleep(0.01)
        while True:
            try:
                f = open("fitness_" + str(self.myId) + ".txt", "r")
                break
            except:
                pass
        self.fitness = float(f.read())
        f.close()
        os.system("del fitness_" + str(self.myId) + ".txt")

    def Mutate(self):
        randrow = random.randint(0, self.numSensorNeurons-1)
        randcol = random.randint(0, self.numMotorNeurons-1)
        self.weights[randrow, randcol] = random.random()*2-1
        if random.random() < 0.5:
            overlapping = True
            self.number_links += 1
            while overlapping:
                length = min(random.random()+0.4,0.8)
                width = min(random.random()+0.4,0.8)
                height = min(random.random()+0.4,0.8)
                rand_link = random.randint(0, len(self.possible_positions)-1)
                new_link_pos = self.possible_positions[rand_link]
                old_dim = self.space_taken[new_link_pos[0]]
                if new_link_pos[2] == 'l':
                    if math.copysign(1, new_link_pos[1][0]) == 1:

                        new_dim = [old_dim[0] + 1, old_dim[1],old_dim[2]]
                    else:

                        new_dim = [old_dim[0] - 1, old_dim[1],old_dim[2]]
                elif new_link_pos[2] == 'w':
                    if math.copysign(1, new_link_pos[1][1]) == 1:

                        new_dim = [old_dim[0], old_dim[1] + 1, old_dim[2]]
                    else:

                        new_dim = [old_dim[0], old_dim[1] - 1, old_dim[2]]
                elif new_link_pos[2] == 'h':
                    if math.copysign(1, new_link_pos[1][2]) == 1:

                        new_dim = [old_dim[0], old_dim[1], old_dim[2] + 1]
                    else:

                        new_dim = [old_dim[0], old_dim[1], old_dim[2] - 1]
                    # print(new_dim)
                    # print(new_link_pos)
                for j in self.space_taken:
                    if self.space_taken[j] == new_dim:
                        overlapping = True
                        self.possible_positions.remove(new_link_pos)
                        break
                    else:
                        overlapping = False

                if not overlapping:
                    self.space_taken["Cube"+str(self.number_links)] = new_dim
            self.possible_positions.remove(new_link_pos)
            # print(old_dim, new_dim)
            # print(new_link_pos)
            cube_pos = [math.copysign(length/2, new_link_pos[1][0]) if new_link_pos[2] == 'l' else 0,
                        math.copysign(width/2, new_link_pos[1][1]) if new_link_pos[2] == 'w' else 0,
                        math.copysign(height/2, new_link_pos[1][2]) if new_link_pos[2] == 'h' else 0]
            # print(cube_pos)
            if new_link_pos[2] == 'l':
                jaxis = "0 1 1"
            elif new_link_pos[2] == 'w':
                jaxis = "1 0 1"
            elif new_link_pos[2] == 'h':
                jaxis = "1 1 0"
            self.storage['Joint'].append([new_link_pos[0]+"_Cube"+str(self.number_links), new_link_pos[0], "Cube"+str(self.number_links), "revolute", new_link_pos[1], jaxis])
            if random.random() < .5:
                self.storage[self.lastiD].append(["Cube"+str(self.number_links), cube_pos , [length,width,height], "Green","0 1.0 0.0 1.0"])
                if "Cube"+str(self.number_links) not in self.sensors:
                    self.storage['Sensor'].append([self.numSensorNeurons+1, "Cube"+str(self.number_links)])
                    self.numSensorNeurons += 1
                    self.numMotorNeurons += 1
                    self.storage['Motor'].append([self.numMotorNeurons+1, new_link_pos[0]+"_Cube"+str(self.number_links)])

            else:
                self.storage[self.lastiD].append(["Cube"+str(self.number_links),cube_pos, [length,width,height],"Cyan", "0 1.0 1.0 1.0"])
            # self.storage['Motor'].append([self.numMotorNeurons+1, new_link_pos[0]+"_Cube"+str(self.number_links)])

            old_length = length
            old_width = width
            old_height = height
            if new_link_pos[1][0] != 0 and new_link_pos[2] == 'l':
                last_pos = new_link_pos[1][0]
                old_length = math.copysign(old_length, last_pos)
                old_width = 0
                old_height = 0
            elif new_link_pos[1][1] != 0 and new_link_pos[2] == 'w':
                last_pos = new_link_pos[1][1]
                old_width = math.copysign(old_width, last_pos)
                old_length = 0
                old_height = 0
            elif new_link_pos[1][2] != 0 and new_link_pos[2] == 'h':
                last_pos = new_link_pos[1][2]
                old_height = math.copysign(old_height, last_pos)
                old_width = 0
                old_length = 0
            self.add_faces("Cube"+str(self.number_links), length, width, height, last_pos, old_length, old_width, old_height)
            # print(self.possible_positions)
        else:
            notChanged = True
            while notChanged and self.numSensorNeurons != self.number_links-1:
                c = random.randint(0, len(self.storage[self.lastiD])-1)
                # print(c, self.numSensorNeurons, self.number_links)
                if self.storage[self.lastiD][c][3] == "Cyan":
                    self.storage[self.lastiD][c][3] = "Green"
                    self.storage[self.lastiD][c][4] = "0 1.0 0.0 1.0"
                    self.storage['Sensor'].append([self.numSensorNeurons+1, self.storage[self.lastiD][c][0]])
                    self.storage['Motor'].append([self.numMotorNeurons+1, self.storage['Joint'][c-1 if c != 0 else 0][0]])
                    self.numSensorNeurons += 1
                    self.numMotorNeurons += 1
                    notChanged=False
        self.storage = {self.myId: self.storage[self.lastiD], 'Joint': self.storage['Joint'], 'Sensor': self.storage['Sensor'],'Motor': self.storage['Motor']}
    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        # pyrosim.Send_Cube(name="Box", pos=[1,2,0.5] , size=[length,width,height])
        pyrosim.End()

    def Update_Body(self):
        link = self.storage[self.myId]
        # print(len(link))
        joint = self.storage['Joint']   
        pyrosim.Start_URDF("body" + str(self.myId) + ".urdf")
        for i in link:
            pyrosim.Send_Cube(name=i[0],pos=i[1],size=i[2],color=i[3],rgb=i[4])
        for i in joint:
            pyrosim.Send_Joint(name=i[0],parent=i[1],child=i[2],type=i[3],position=i[4],jointAxis=i[5])
        pyrosim.End()

    def Update_Brain(self):
        sensor = self.storage['Sensor']
        motor = self.storage['Motor']
        pyrosim.Start_NeuralNetwork("brain" + str(self.myId) + ".nndf")
        for i in sensor:
            pyrosim.Send_Sensor_Neuron(name = i[0], linkName = i[1])
        for i in motor:
            pyrosim.Send_Motor_Neuron( name = i[0] , jointName = i[1])
        self.numSensorNeurons = len(sensor)
        self.numMotorNeurons = len(motor)
        # print('\n', sensor, motor)
        self.weights = numpy.random.rand(self.numSensorNeurons, self.numMotorNeurons)
        self.weights = self.weights*4-1  

        for currentRow in range(self.numSensorNeurons):
            for currentColumn in range(self.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow, targetNeuronName = currentColumn+self.numSensorNeurons, weight = self.weights[currentRow][currentColumn])

        pyrosim.End()

    def add_faces(self, name, length, width, height, last_pos, old_length, old_width, old_height):   
                if old_width != 0:
                    if math.copysign(1, old_width) == -1:
                        self.possible_positions.append((name, [0,-width,0],'w'))
                        self.possible_positions.append((name, [length/2,-width/2,0],'l'))
                        self.possible_positions.append((name, [-length/2,-width/2,0],'l'))
                        self.possible_positions.append((name, [0,-width/2,height/2],'h'))
                        self.possible_positions.append((name, [0,-width/2,-height/2],'h'))
                    else:
                        self.possible_positions.append((name, [0,width,0],'w'))
                        self.possible_positions.append((name, [length/2,width/2,0],'l'))
                        self.possible_positions.append((name, [-length/2,width/2,0],'l'))
                        self.possible_positions.append((name, [0,width/2,height/2],'h'))
                        self.possible_positions.append((name, [0,width/2,-height/2],'h'))
                    
                elif old_height != 0:
                    if math.copysign(1, old_height) == -1:
                        self.possible_positions.append((name, [0,0,-height],'h'))
                        self.possible_positions.append((name, [length/2,0,-height/2], 'l'))
                        self.possible_positions.append((name, [-length/2,0,-height/2],'l'))
                        self.possible_positions.append((name, [0,width/2,-height/2],'w'))
                        self.possible_positions.append((name, [0,-width/2,-height/2],'w'))

                    else:
                        self.possible_positions.append((name, [0,0,height],'h'))
                        self.possible_positions.append((name, [length/2,0,height/2],'l'))
                        self.possible_positions.append((name, [-length/2,0,height/2],'l'))
                        self.possible_positions.append((name, [0,width/2,height/2],'w'))
                        self.possible_positions.append((name, [0,-width/2,height/2],'w'))
                elif old_length != 0:
                    if math.copysign(1, old_length) == -1:
                        self.possible_positions.append((name, [-length, 0, 0],'l'))
                        self.possible_positions.append((name, [-length/2, width/2, 0],'w'))
                        self.possible_positions.append((name, [-length/2, -width/2, 0],'w'))
                        self.possible_positions.append((name, [-length/2, 0, height/2],'h'))
                        self.possible_positions.append((name, [-length/2, 0, -height/2],'h'))
                    else:
                        self.possible_positions.append((name, [length, 0, 0],'l'))
                        self.possible_positions.append((name, [length/2, width/2, 0],'w'))
                        self.possible_positions.append((name, [length/2, -width/2, 0],'w'))
                        self.possible_positions.append((name, [length/2, 0, height/2],'h'))
                        self.possible_positions.append((name, [length/2, 0, -height/2],'h'))
   
        
    def Create_Body(self):
        pyrosim.Start_SDF("world.sdf")
        length = 1
        width = 1
        height = 1
        self.ctr = 1
        pyrosim.End()
        self.sensors = []
        self.motors = []
        pyrosim.Start_URDF("body" + str(self.myId) + ".urdf")
        last_pos = 0
        self.space_taken = {}
        self.number_links = random.randint(4,8)
        self.random_links = [0 for i in range(self.number_links)]
        for i in range(self.number_links):
            if random.random() < 0.5:
                self.random_links[i] = 1
            else:
                self.random_links[i] = 0
        while sum(self.random_links) <= 1:
            for i in range(self.number_links):
                if random.random() < 0.5:
                    self.random_links[i] = 1
                else:
                    self.random_links[i] = 0

        if self.random_links[0] == 1:
            pyrosim.Send_Cube(name="Cube0", pos=[0,0,2] , size=[1,1,1], color="Green", rgb = "0 1.0 0.0 1.0")
            self.storage[self.myId].append(["Cube0",[0,0,2], [1,1,1],"Green", "0 1.0 0.0 1.0"])
        else:
            pyrosim.Send_Cube(name="Cube0", pos=[0,0,2] , size=[1,1,1], color="Cyan", rgb = "0 1.0 1.0 1.0")
            self.storage[self.myId].append(["Cube0",[0,0,2], [1,1,1],"Cyan", "0 1.0 1.0 1.0"])
        # self.space_taken["Cube0"] = [abs_x+length/2, abs_x-length/2,abs_y+width/2, abs_y-width/2, abs_z+height/2, abs_z-height/2]
        self.space_taken["Cube0"] = [0,0,0]
        self.possible_positions = []
        self.possible_positions.append(("Cube0", [0.5, 0, 2],'l'))
        self.possible_positions.append(("Cube0", [-0.5, 0, 2],'l'))
        self.possible_positions.append(("Cube0", [0, 0.5, 2],'w'))
        self.possible_positions.append(("Cube0", [0, -0.5, 2],'w'))
        # self.possible_positions.append(("Cube0", [0, 0, 0.5],'h'))
        # self.possible_positions.append(("Cube0", [0, 0, -0.5],'h'))
        length = 1
        width = 1
        height = 1
        rand_link = random.randint(0, len(self.possible_positions)-1)
        new_link_pos = self.possible_positions[rand_link]
        self.possible_positions.remove(new_link_pos)
        old_dim = self.space_taken[new_link_pos[0]]
        
        if new_link_pos[2] == 'l':
            if math.copysign(1, new_link_pos[1][0]) == 1:

                new_dim = [old_dim[0] + 1, old_dim[1],old_dim[2]]
            else:

                new_dim = [old_dim[0] - 1, old_dim[1],old_dim[2]]
        elif new_link_pos[2] == 'w':
            if math.copysign(1, new_link_pos[1][1]) == 1:

                new_dim = [old_dim[0], old_dim[1] + 1, old_dim[2]]
            else:

                new_dim = [old_dim[0], old_dim[1] - 1, old_dim[2]]
        elif new_link_pos[2] == 'h':
            if math.copysign(1, new_link_pos[1][2]) == 1:

                new_dim = [old_dim[0], old_dim[1], old_dim[2] + 1]
            else:

                new_dim = [old_dim[0], old_dim[1], old_dim[2] - 1]

        # print(new_dim)
        overlapping = True
        for i in self.space_taken:

            if self.space_taken[i] == new_dim:
                overlapping = True
                break
            else:
                overlapping = False
        if not overlapping:
            self.space_taken["Cube"+str(self.ctr)] = new_dim
        
        if new_link_pos[2] == 'l':
            jaxis = "0 1 1"
                
        elif new_link_pos[2] == 'w':
            jaxis = "1 0 1"
        elif new_link_pos[2] == 'h':
            jaxis = "1 1 0"
        cube_pos = [math.copysign(length/2, new_link_pos[1][0]) if new_link_pos[2] == 'l' else 0,
                        math.copysign(width/2, new_link_pos[1][1]) if new_link_pos[2] == 'w' else 0,
                        math.copysign(height/2, new_link_pos[1][2]) if new_link_pos[2] == 'h' else 0]
        pyrosim.Send_Joint(name=new_link_pos[0]+"_Cube"+str(self.ctr), parent=new_link_pos[0], child="Cube"+str(self.ctr), type="revolute", position = new_link_pos[1], jointAxis=jaxis)
        self.storage['Joint'].append([new_link_pos[0]+"_Cube"+str(self.ctr),new_link_pos[0],"Cube"+str(self.ctr),"revolute",new_link_pos[1],jaxis])
        if self.random_links[1] == 1:
                pyrosim.Send_Cube(name="Cube"+str(self.ctr), pos=cube_pos , size=[length,width,height], color="Green", rgb = "0 1.0 0.0 1.0")
                self.sensors.append("Cube1")
                self.motors.append("Cube0_Cube1")
                self.storage[self.myId].append(["Cube"+str(self.ctr),cube_pos, [length,width,height],"Green", "0 1.0 0.0 1.0"])
        else:
                pyrosim.Send_Cube(name="Cube"+str(self.ctr), pos=cube_pos , size=[length,width,height], color="Cyan", rgb = "0 1.0 1.0 1.0")
                self.storage[self.myId].append(["Cube"+str(self.ctr),cube_pos, [length,width,height],"Cyan", "0 1.0 1.0 1.0"])

        old_length = length
        old_width = width
        old_height = height
        if new_link_pos[1][0] != 0 and new_link_pos[2] == 'l':
            last_pos = new_link_pos[1][0]
            old_length = math.copysign(old_length, last_pos)
            old_width = 0
            old_height = 0
        elif new_link_pos[1][1] != 0 and new_link_pos[2] == 'w':
            last_pos = new_link_pos[1][1]
            old_width = math.copysign(old_width, last_pos)
            old_length = 0
            old_height = 0
        elif new_link_pos[1][2] != 0 and new_link_pos[2] == 'h':
            last_pos = new_link_pos[1][2]
            old_height = math.copysign(old_height, last_pos)
            old_width = 0
            old_length = 0
        self.add_faces("Cube"+str(self.ctr), length, width, height, last_pos, old_length, old_width, old_height)

        self.ctr += 1
        for i in range(2,self.number_links):
            overlapping = True

            while overlapping:
                length = min(random.random()+0.4,0.8)
                width = min(random.random()+0.4,0.8)
                height = min(random.random()+0.4,0.8)
                rand_link = random.randint(0, len(self.possible_positions)-1)
                new_link_pos = self.possible_positions[rand_link]
                old_dim = self.space_taken[new_link_pos[0]]
                if new_link_pos[2] == 'l':
                    if math.copysign(1, new_link_pos[1][0]) == 1:

                        new_dim = [old_dim[0] + 1, old_dim[1],old_dim[2]]
                    else:

                        new_dim = [old_dim[0] - 1, old_dim[1],old_dim[2]]
                elif new_link_pos[2] == 'w':
                    if math.copysign(1, new_link_pos[1][1]) == 1:

                        new_dim = [old_dim[0], old_dim[1] + 1, old_dim[2]]
                    else:

                        new_dim = [old_dim[0], old_dim[1] - 1, old_dim[2]]
                elif new_link_pos[2] == 'h':
                    if math.copysign(1, new_link_pos[1][2]) == 1:

                        new_dim = [old_dim[0], old_dim[1], old_dim[2] + 1]
                    else:

                        new_dim = [old_dim[0], old_dim[1], old_dim[2] - 1]
                # print(new_dim)
                # print(new_link_pos)
                for j in self.space_taken:
                    if self.space_taken[j] == new_dim:
                        overlapping = True
                        self.possible_positions.remove(new_link_pos)
                        break
                    else:
                        overlapping = False

                if not overlapping:
                    self.space_taken["Cube"+str(self.ctr)] = new_dim
            self.possible_positions.remove(new_link_pos)
            # print(old_dim, new_dim)
            # print(new_link_pos)
            cube_pos = [math.copysign(length/2, new_link_pos[1][0]) if new_link_pos[2] == 'l' else 0,
                        math.copysign(width/2, new_link_pos[1][1]) if new_link_pos[2] == 'w' else 0,
                        math.copysign(height/2, new_link_pos[1][2]) if new_link_pos[2] == 'h' else 0]
            # print(cube_pos)
            if new_link_pos[2] == 'l':
                jaxis = "0 1 1"
            elif new_link_pos[2] == 'w':
                jaxis = "1 0 1"
            elif new_link_pos[2] == 'h':
                jaxis = "1 1 0"
            pyrosim.Send_Joint(name=new_link_pos[0]+"_Cube"+str(i), parent=new_link_pos[0], child="Cube"+str(i), type="revolute", position = new_link_pos[1], jointAxis=jaxis)
            self.storage['Joint'].append([new_link_pos[0]+"_Cube"+str(i),new_link_pos[0],"Cube"+str(i),"revolute",new_link_pos[1],jaxis])

            if self.random_links[i] == 1:
                pyrosim.Send_Cube(name="Cube"+str(i), pos=cube_pos , size=[length,width,height], color="Green", rgb = "0 1.0 0.0 1.0")
                if "Cube"+str(i) not in self.sensors:
                    self.sensors.append("Cube"+str(i))
                self.storage[self.myId].append(["Cube"+str(i),cube_pos, [length,width,height],"Green", "0 1.0 0.0 1.0"])
                self.motors.append(new_link_pos[0]+"_Cube"+str(i))
            else:
                pyrosim.Send_Cube(name="Cube"+str(i), pos=cube_pos , size=[length,width,height], color="Cyan", rgb = "0 1.0 1.0 1.0")
                self.storage[self.myId].append(["Cube"+str(i),cube_pos, [length,width,height],"Cyan", "0 1.0 1.0 1.0"])
            # self.motors.append(new_link_pos[0]+"_Cube"+str(i))

            old_length = length
            old_width = width
            old_height = height
            if new_link_pos[1][0] != 0 and new_link_pos[2] == 'l':
                last_pos = new_link_pos[1][0]
                old_length = math.copysign(old_length, last_pos)
                old_width = 0
                old_height = 0
            elif new_link_pos[1][1] != 0 and new_link_pos[2] == 'w':
                last_pos = new_link_pos[1][1]
                old_width = math.copysign(old_width, last_pos)
                old_length = 0
                old_height = 0
            elif new_link_pos[1][2] != 0 and new_link_pos[2] == 'h':
                last_pos = new_link_pos[1][2]
                old_height = math.copysign(old_height, last_pos)
                old_width = 0
                old_length = 0
            self.add_faces("Cube"+str(i), length, width, height, last_pos, old_length, old_width, old_height)
            # print(self.possible_positions)
            old_length = length
            old_width = width
            old_height = height
            self.ctr += 1


        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myId) + ".nndf")
        neurons = 0
        for i in self.sensors:
            pyrosim.Send_Sensor_Neuron(name = neurons, linkName = i)
            self.storage['Sensor'].append([neurons, i])
            neurons += 1
        self.numSensorNeurons = len(self.sensors)
        motors = 0
        # print(self.sensors)
        # print(self.numSensorNeurons)
        # print(self.numMotorNeurons)
        # print(self.random_links)
        for i in self.motors:
                pyrosim.Send_Motor_Neuron( name = neurons , jointName = i)
                self.storage['Motor'].append([neurons, i])
                neurons += 1
                motors += 1

        self.numMotorNeurons = len(self.motors)
        self.weights = numpy.random.rand(self.numSensorNeurons, self.numMotorNeurons)
        self.weights = self.weights*4-1  


        for currentRow in range(self.numSensorNeurons):
            for currentColumn in range(self.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow, targetNeuronName = currentColumn+self.numSensorNeurons, weight = self.weights[currentRow][currentColumn])

        pyrosim.End()