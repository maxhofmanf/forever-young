from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
robotArm.grab()
for r in range(2):
    robotArm.moveRight()
robotArm.drop()
for r in range(2):
    robotArm.moveLeft()
robotArm.grab()
for r in range(2):
    robotArm.moveRight()
robotArm.drop()
for r in range(2):
    robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
robotArm.moveRight()
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()
robotArm.moveRight()
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()