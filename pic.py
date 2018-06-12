import pybullet as p
import time
from random import randint
from script import escreve_urdf

p.connect(p.GUI)
p.setRealTimeSimulation(1)



while True:
	escreve_urdf()
	print("-----------------------------------------------------------------------------------------------------------")
	p.resetSimulation()
	p.setGravity(0,0,-10)

	p.createCollisionShape(p.GEOM_PLANE)
	p.createMultiBody(0,0)
	timme = time.time()

	obj = p.loadURDF("oba.urdf")
	dist = 0

	for j in range(p.getNumJoints(obj)):
		maxVel = randint(5,30)
		maxForce = randint(100, 400)

	while(time.time() <= timme + 5):
			p.setJointMotorControl2(obj, j, p.VELOCITY_CONTROL,targetVelocity=maxVel,force=maxForce)
			pos = p.getLinkState(obj,j)[0]
			dist = (pos[0]**2 + pos[1]**2)**0.5
	p.stepSimulation()
	time.sleep(0.01)
p.disconnect()