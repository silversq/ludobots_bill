import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c
import math

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myId = nextAvailableID
        self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons)
        self.weights = self.weights*2-1
        self.sensors = []
        self.motors = []
        self.ctr = 1

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
        # pyrosim.Send_Cube(name="Box", pos=[1,2,0.5] , size=[length,width,height])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_SDF("world.sdf")
        length = 1
        width = 1
        height = 1
        self.ctr = 1
        self.sensors = []
        self.motors = []
        pyrosim.End()
        def add_faces(possible_positions, name, length, width, height, last_pos, old_length, old_width, old_height):   
            if old_width != 0:
                if math.copysign(1, old_width) == -1:
                    possible_positions.append((name, [0,-width,0],'w'))
                    possible_positions.append((name, [length/2,-width/2,0],'l'))
                    possible_positions.append((name, [-length/2,-width/2,0],'l'))
                    possible_positions.append((name, [0,-width/2,height/2],'h'))
                    possible_positions.append((name, [0,-width/2,-height/2],'h'))
                else:
                    possible_positions.append((name, [0,width,0],'w'))
                    possible_positions.append((name, [length/2,width/2,0],'l'))
                    possible_positions.append((name, [-length/2,width/2,0],'l'))
                    possible_positions.append((name, [0,width/2,height/2],'h'))
                    possible_positions.append((name, [0,width/2,-height/2],'h'))
                
            elif old_height != 0:
                if math.copysign(1, old_height) == -1:
                    possible_positions.append((name, [0,0,-height],'h'))
                    possible_positions.append((name, [length/2,0,-height/2], 'l'))
                    possible_positions.append((name, [-length/2,0,-height/2],'l'))
                    possible_positions.append((name, [0,width/2,-height/2],'w'))
                    possible_positions.append((name, [0,-width/2,-height/2],'w'))

                else:
                    possible_positions.append((name, [0,0,height],'h'))
                    possible_positions.append((name, [length/2,0,height/2],'l'))
                    possible_positions.append((name, [-length/2,0,height/2],'l'))
                    possible_positions.append((name, [0,width/2,height/2],'w'))
                    possible_positions.append((name, [0,-width/2,height/2],'w'))
            elif old_length != 0:
                if math.copysign(1, old_length) == -1:
                    possible_positions.append((name, [-length, 0, 0],'l'))
                    possible_positions.append((name, [-length/2, width/2, 0],'w'))
                    possible_positions.append((name, [-length/2, -width/2, 0],'w'))
                    possible_positions.append((name, [-length/2, 0, height/2],'h'))
                    possible_positions.append((name, [-length/2, 0, -height/2],'h'))
                else:
                    possible_positions.append((name, [length, 0, 0],'l'))
                    possible_positions.append((name, [length/2, width/2, 0],'w'))
                    possible_positions.append((name, [length/2, -width/2, 0],'w'))
                    possible_positions.append((name, [length/2, 0, height/2],'h'))
                    possible_positions.append((name, [length/2, 0, -height/2],'h'))
            # if last_pos != -old_width:            
            #     possible_positions.append((name,[0, width, 0]))    
            # elif last_pos != old_width:
            #     possible_positions.append((name,[0, -width, 0]))
            # elif last_pos != -old_length:
            #     possible_positions.append((name,[length, 0, 0]))
            # elif last_pos != old_length:
            #     possible_positions.append((name,[-length, 0, 0]))
            # elif last_pos != -old_height:
            #     possible_positions.append((name,[0, 0, height]))  
            # elif last_pos != old_height:
            #     possible_positions.append((name,[0, 0, -height]))    
        pyrosim.Start_URDF("body.urdf")
        last_pos = 0
        space_taken = {}
        abs_x=0
        abs_y=0
        abs_z=0
        self.random_links = []
        self.number_links = random.randint(15,15)
        for i in range(self.number_links):
            if random.random() < 0.5:
                self.random_links.append(1)
            else:
                self.random_links.append(0)
        width = 1
        if self.random_links[0] == 0:
            pyrosim.Send_Cube(name="Cube0", pos=[0,0,0] , size=[1,1,1], color="Green", rgb = "0 1.0 0.0 1.0")
        else:
            pyrosim.Send_Cube(name="Cube0", pos=[0,0,0] , size=[1,1,1], color="Cyan", rgb = "0 1.0 1.0 1.0")
        space_taken["Cube0"] = [abs_x+length/2, abs_x-length/2,abs_y+width/2, abs_y-width/2, abs_z+height/2, abs_z-height/2]
        possible_positions = []
        possible_positions.append(("Cube0", [0.5, 0, 0],'l'))
        possible_positions.append(("Cube0", [-0.5, 0, 0],'l'))
        possible_positions.append(("Cube0", [0, 0.5, 0],'w'))
        possible_positions.append(("Cube0", [0, -0.5, 0],'w'))
        possible_positions.append(("Cube0", [0, 0, 0.5],'h'))
        possible_positions.append(("Cube0", [0, 0, -0.5],'h'))
        length = 1
        width = 1
        height = 1
        rand_link = random.randint(0, len(possible_positions)-1)
        new_link_pos = possible_positions[rand_link]
        possible_positions.remove(new_link_pos)
        old_dim = space_taken[new_link_pos[0]]
        
        if new_link_pos[2] == 'l':
            if math.copysign(1, new_link_pos[1][0]) == 1:
                w = abs(old_dim[2]-old_dim[3])/2 - (width / 2)
                h = abs(old_dim[4]-old_dim[5])/2 - (height / 2)
                new_dim = [old_dim[0]+math.copysign(length, new_link_pos[1][0]), old_dim[0],
                            old_dim[2]-w, old_dim[3]+w,
                            old_dim[4]-h, old_dim[5]+h]
            else:
                w = abs(old_dim[2]-old_dim[3])/2 - (width / 2)
                h = abs(old_dim[4]-old_dim[5])/2 - (height / 2)
                new_dim = [old_dim[1], old_dim[1]+math.copysign(length, new_link_pos[1][0]),
                            old_dim[2]-w, old_dim[3]+w,
                            old_dim[4]-h, old_dim[5]+h]
        elif new_link_pos[2] == 'w':
            if math.copysign(1, new_link_pos[1][1]) == 1:
                l = abs(old_dim[0]-old_dim[1])/2 - (length / 2)
                h = abs(old_dim[4]-old_dim[5])/2 - (height / 2)
                new_dim = [old_dim[0]-l, old_dim[1]+l,
                            old_dim[2]+math.copysign(width, new_link_pos[1][1]), old_dim[2],
                            old_dim[4]-h, old_dim[5]+h]
            else:
                l = abs(old_dim[0]-old_dim[1])/2 - (length / 2)
                h = abs(old_dim[4]-old_dim[5])/2 - (height / 2)
                new_dim = [old_dim[0]-l, old_dim[1]+l,
                            old_dim[3], old_dim[3]+math.copysign(width, new_link_pos[1][1]),
                            old_dim[4]-h, old_dim[5]+h]
        elif new_link_pos[2] == 'h':
            if math.copysign(1, new_link_pos[1][2]) == 1:
                l = abs(old_dim[0]-old_dim[1])/2 - (length / 2)
                w = abs(old_dim[2]-old_dim[3])/2 - (width / 2)
                new_dim = [old_dim[0]-l, old_dim[1]+l,
                            old_dim[2]-w, old_dim[3]+w,
                            old_dim[4]+math.copysign(height, new_link_pos[1][2]), old_dim[4]]
            else:
                l = abs(old_dim[0]-old_dim[1])/2 - (length / 2)
                w = abs(old_dim[2]-old_dim[3])/2 - (width / 2)
                new_dim = [old_dim[0]-l, old_dim[1]+l,
                            old_dim[2]-w, old_dim[3]+w,
                            old_dim[5], old_dim[5]+math.copysign(height, new_link_pos[1][2])]
        # new_dim = [old_dim[0]+length, old_dim[0]-length/2, old_dim[1]+width/2, old_dim[1]-width/2, old_dim[2]+height/2,old_dim[2]-height/2]
        # print(new_link_pos)
        # print(old_dim)
        print(new_dim)
        overlapping = True
        for i in space_taken:
            if new_dim[1] <= space_taken[i][0] and new_dim[0] >= space_taken[i][1] and new_dim[3] <= space_taken[i][2] and new_dim[2] >= space_taken[i][3] and new_dim[5] <= space_taken[i][4] and new_dim[4] >= space_taken[i][5]:
                overlapping = False
            else:
                overlapping = True
                break
        if not overlapping:
            space_taken["Cube"+str(self.ctr)] = new_dim
        
        if new_link_pos[2] == 'l':
            jaxis = "0 0 1"
                
        elif new_link_pos[2] == 'w':
            jaxis = "0 0 1"
        elif new_link_pos[2] == 'h':
            jaxis = "1 0 0"
        cube_pos = [math.copysign(length/2, new_link_pos[1][0]) if new_link_pos[2] == 'l' else 0,
                        math.copysign(width/2, new_link_pos[1][1]) if new_link_pos[2] == 'w' else 0,
                        math.copysign(height/2, new_link_pos[1][2]) if new_link_pos[2] == 'h' else 0]
        pyrosim.Send_Joint(name=new_link_pos[0]+"_Cube"+str(self.ctr), parent=new_link_pos[0], child="Cube"+str(self.ctr), type="revolute", position = new_link_pos[1], jointAxis=jaxis)
        if self.random_links[1] == 0:
                pyrosim.Send_Cube(name="Cube"+str(self.ctr), pos=cube_pos , size=[length,width,height], color="Green", rgb = "0 1.0 0.0 1.0")
            # self.sensors.append("Cube"+str(self.ctr))
            # self.motors.append(new_link_pos[0]+"_Cube"+str(self.ctr))
        else:
                pyrosim.Send_Cube(name="Cube"+str(self.ctr), pos=cube_pos , size=[length,width,height], color="Cyan", rgb = "0 1.0 1.0 1.0")
        
        old_length = length
        old_width = width
        old_height = height
        if new_link_pos[1][0] != 0:
            last_pos = new_link_pos[1][0]
            old_length = math.copysign(old_length, last_pos)
            old_width = 0
            old_height = 0
        elif new_link_pos[1][1] != 0:
            last_pos = new_link_pos[1][1]
            old_width = math.copysign(old_width, last_pos)
            old_length = 0
            old_height = 0
        elif new_link_pos[1][2] != 0:
            last_pos = new_link_pos[1][2]
            old_height = math.copysign(old_height, last_pos)
            old_width = 0
            old_length = 0
        add_faces(possible_positions, "Cube"+str(self.ctr), length, width, height, last_pos, old_length, old_width, old_height)

        self.ctr += 1
        for i in range(2,self.number_links):
            overlapping = True
            # length = 1
            # width = 1
            # height = 1
            while overlapping:
                length = min(random.random()+0.2,1)
                width = min(random.random()+0.2,1)
                height = min(random.random()+0.2,1)
                # print(length, width, height)
                rand_link = random.randint(0, len(possible_positions)-1)
                # print(rand_link)
                new_link_pos = possible_positions[rand_link]
                old_dim = space_taken[new_link_pos[0]]
                if new_link_pos[2] == 'l':
                    if math.copysign(1, new_link_pos[1][0]) == 1:
                        w = abs(old_dim[2]-old_dim[3])/2 - (width / 2)
                        h = abs(old_dim[4]-old_dim[5])/2 - (height / 2)
                        new_dim = [old_dim[0]+math.copysign(length, new_link_pos[1][0]), old_dim[0],
                                    old_dim[2]-w, old_dim[3]+w,
                                    old_dim[4]-h, old_dim[5]+h]
                    else:
                        w = abs(old_dim[2]-old_dim[3])/2 - (width / 2)
                        h = abs(old_dim[4]-old_dim[5])/2 - (height / 2)
                        new_dim = [old_dim[1], old_dim[1]+math.copysign(length, new_link_pos[1][0]),
                                    old_dim[2]-w, old_dim[3]+w,
                                    old_dim[4]-h, old_dim[5]+h]
                elif new_link_pos[2] == 'w':
                    if math.copysign(1, new_link_pos[1][1]) == 1:
                        l = abs(old_dim[0]-old_dim[1])/2 - (length / 2)
                        h = abs(old_dim[4]-old_dim[5])/2 - (height / 2)
                        new_dim = [old_dim[0]-l, old_dim[1]+l,
                                    old_dim[2]+math.copysign(width, new_link_pos[1][1]), old_dim[2],
                                    old_dim[4]-h, old_dim[5]+h]
                    else:
                        l = abs(old_dim[0]-old_dim[1])/2 - (length / 2)
                        h = abs(old_dim[4]-old_dim[5])/2 - (height / 2)
                        new_dim = [old_dim[0]-l, old_dim[1]+l,
                                    old_dim[3], old_dim[3]+math.copysign(width, new_link_pos[1][1]),
                                    old_dim[4]-h, old_dim[5]+h]
                elif new_link_pos[2] == 'h':
                    if math.copysign(1, new_link_pos[1][2]) == 1:
                        l = abs(old_dim[0]-old_dim[1])/2 - (length / 2)
                        w = abs(old_dim[2]-old_dim[3])/2 - (width / 2)
                        new_dim = [old_dim[0]-l, old_dim[1]+l,
                                    old_dim[2]-w, old_dim[3]+w,
                                    old_dim[4]+math.copysign(height, new_link_pos[1][2]), old_dim[4]]
                    else:
                        l = abs(old_dim[0]-old_dim[1])/2 - (length / 2)
                        w = abs(old_dim[2]-old_dim[3])/2 - (width / 2)
                        new_dim = [old_dim[0]-l, old_dim[1]+l,
                                    old_dim[2]-w, old_dim[3]+w,
                                    old_dim[5], old_dim[5]+math.copysign(height, new_link_pos[1][2])]
                print(space_taken.keys(), len(possible_positions))
                print(new_link_pos[0])
                for j in space_taken:
                    if new_dim[1] <= space_taken[j][0] and new_dim[0] >= space_taken[j][1] and new_dim[3] <= space_taken[j][2] and new_dim[2] >= space_taken[j][3] and new_dim[5] <= space_taken[j][4] and new_dim[4] >= space_taken[j][5]:
                        if new_dim != space_taken[j]:
                            overlapping = False
                        else:
                            overlapping = True
                            break
                    else:
                        # print(space_taken[j], new_dim, j, new_link_pos)
                        overlapping = True
                        break
                if not overlapping:
                    space_taken["Cube"+str(self.ctr)] = new_dim
            possible_positions.remove(new_link_pos)
            print(old_dim, new_dim)
            # print(new_link_pos)
            cube_pos = [math.copysign(length/2, new_link_pos[1][0]) if new_link_pos[2] == 'l' else 0,
                        math.copysign(width/2, new_link_pos[1][1]) if new_link_pos[2] == 'w' else 0,
                        math.copysign(height/2, new_link_pos[1][2]) if new_link_pos[2] == 'h' else 0]
            # print(cube_pos)
            if new_link_pos[2] == 'l':
                jaxis = "0 0 1"
            elif new_link_pos[2] == 'w':
                jaxis = "0 0 1"
            elif new_link_pos[2] == 'h':
                jaxis = "1 0 0"
            pyrosim.Send_Joint(name=new_link_pos[0]+"_Cube"+str(i), parent=new_link_pos[0], child="Cube"+str(i), type="revolute", position = new_link_pos[1], jointAxis=jaxis)
            if self.random_links[i] == 0:
                pyrosim.Send_Cube(name="Cube"+str(i), pos=cube_pos , size=[length,width,height], color="Green", rgb = "0 1.0 0.0 1.0")
                if "Cube"+str(i) not in self.sensors:
                    self.sensors.append("Cube"+str(i))
                    # print("Cube"+str(i))
                    # print(new_link_pos[0]+"_Cube"+str(i))
                    self.motors.append(new_link_pos[0]+"_Cube"+str(i))

            else:
                pyrosim.Send_Cube(name="Cube"+str(i), pos=cube_pos , size=[length,width,height], color="Cyan", rgb = "0 1.0 1.0 1.0")
            if new_link_pos[1][0] != 0:
                last_pos = new_link_pos[1][0]
                old_length = math.copysign(old_length, last_pos)
                old_width = 0
                old_height = 0
            elif new_link_pos[1][1] != 0:
                last_pos = new_link_pos[1][1]
                old_width = math.copysign(old_width, last_pos)
                old_length = 0
                old_height = 0
            elif new_link_pos[1][2] != 0:
                last_pos = new_link_pos[1][2]
                old_height = math.copysign(old_height, last_pos)
                old_width = 0
                old_length = 0
            add_faces(possible_positions, "Cube"+str(i), length, width, height, last_pos, old_length, old_width, old_height)
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
            neurons += 1
        sensors = neurons
        c.numSensorNeurons = sensors
        motors = 0
        print(self.sensors)
        print(self.motors)
        print(self.random_links)
        for i in self.motors:
                pyrosim.Send_Motor_Neuron( name = neurons , jointName = i)
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