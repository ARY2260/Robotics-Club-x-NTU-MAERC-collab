import pybullet as p

p.connect(p.DIRECT)
arm = p.loadURDF('robot_arm.urdf')

number_of_joints = p.getNumJoints(arm)

for joint_number in range(number_of_joints):
    info = p.getJointInfo(arm,joint_number) 
    print(info) #first arg in output is joint id

# doubt: did not find joint type in output

