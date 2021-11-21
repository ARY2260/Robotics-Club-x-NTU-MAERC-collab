""" 
    basic tasks: (move 2 r2d2 robot objs)

        - import dependencies
        - connect to the client
        - set inventory path (optional)
        - load plane (.URDF)
        - set object1 pos data
        - set object1 orient data 
        - load object1 (.URDF)
        - set object2 pos data
        - set object2 orient data 
        - load object2 (.URDF)
        - set time loop
        - manipulate gravity till a certain value of x is achieved
        - set simulation and sleep time
        - else case : remove old bodies and insert new ones
        - disconnect from the client
"""
import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally

planeId = p.loadURDF("plane.urdf")

roboStartPos = [2,2,1]
roboStartOrientation = p.getQuaternionFromEuler([0,0,0])
roboId = p.loadURDF("r2d2.urdf",roboStartPos, roboStartOrientation)

robo2StartPos = [0,0,1]
robo2StartOrientation = p.getQuaternionFromEuler([0,0,0])
robo2Id = p.loadURDF("r2d2.urdf",robo2StartPos, robo2StartOrientation)

x=0.0
for i in range (10000):
    if x<6.92:
     x=x+0.01
    else:
     x=0
     p.removeBody(roboId) # removeBody(<obj_id>) method to remove objs
     p.removeBody(robo2Id) 
     roboId = p.loadURDF("r2d2.urdf",roboStartPos, roboStartOrientation)
     robo2Id = p.loadURDF("r2d2.urdf",robo2StartPos, robo2StartOrientation)
    p.setGravity(-x,-x,0) 
    p.stepSimulation()
    time.sleep(1./240.)
 
    

p.disconnect()
