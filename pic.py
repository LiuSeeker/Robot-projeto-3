import pybullet as p
import time
from random import randint

p.connect(p.GUI)

p.resetSimulation()
p.setGravity(0,0,-10)

p.createCollisionShape(p.GEOM_PLANE)
p.createMultiBody(0,0)

obj = p.loadURDF("nicnic.urdf")

p.setRealTimeSimulation(1)
while(1):
	for i in range(p.getNumJoints(obj)):
		maxVel = randint(50,200)
		maxForce = randint(10, 500)
		p.setJointMotorControl2(obj, i, p.VELOCITY_CONTROL,targetVelocity=20,force=500)
	p.stepSimulation()
	time.sleep(0.01)
p.disconnect()