import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")

length = 1
width = 1
height = 1
for i in range(10):
    pyrosim.Send_Cube(name="Box", pos=[0,0,i+0.5] , size=[length,width,height])
    length *= 0.9
    width *= 0.9
    height *= 0.9
pyrosim.End()
