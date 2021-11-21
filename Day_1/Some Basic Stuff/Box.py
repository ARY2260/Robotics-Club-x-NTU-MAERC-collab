""" 
    basic tasks: (to drop a cube from certain height)

        - import dependencies
        - connect to the client
        - set inventory path (optional)
        - set gravity
        - load plane (.URDF)
        - set object pos data
        - set object orient data 
        - load object (.URDF)
        - start a simulation and set sleep time in a time loop
        - get pos and orient values of the object
        - execute other statements 
        - disconnect from the client
"""
import pybullet as p
import time
import pybullet_data  # takes in built data from pybullet


physicsClient = p.connect(p.GUI)  # or p.DIRECT for non-graphical version
# optionally (to search for an existing file in pybullet library)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, 9.8)  # gravity setup


planeId = p.loadURDF("plane.urdf")

cubeStartPos = [0, 0, 1]  # spawn point
cubeStartOrientation = p.getQuaternionFromEuler(
    [0, 1.56, 0.57])  # rpy value at spawn

# spawning fn : loadURDF(<file>,position,orientation)
boxId = p.loadURDF("Box.urdf", cubeStartPos, cubeStartOrientation)
# object id is stored in the variable that calls loadURDF method

for i in range(100):  # defines the length of the simulation

    p.stepSimulation()  # doubt: what is the length of one step?

    time.sleep(1./240.)  # get simulation after every 1/240th of a sec
# its a pause during a code execution to let other libs or executions run
cubePos, cubeOrn = p.getBasePositionAndOrientation(
    boxId)  # get fn for pos and orient values

print(cubePos, " orientation = ", cubeOrn)

p.disconnect()  # disconnect from client

# doubt: even without p.diconnect(), the client window automatically closes
# doubt : what is the 4th value in cube orientation values?
