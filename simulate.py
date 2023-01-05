import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
 
p.loadSDF("world.sdf")
p.setGravity(0,0,-9.8)

planeId = p.loadURDF("plane.urdf")


for i in range(1000):
    p.stepSimulation()
    time.sleep(1/60)
    print(i)
p.disconnect()