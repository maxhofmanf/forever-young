from RobotArm import RobotArm

robotArm = RobotArm('exercise 3')

# Jouw python instructies zet je vanaf hier:
robotArm.grab()
for n in range(9):
    robotArm.moveRight()
robotArm.drop()
for n in range(9):
    robotArm.moveLeft()
robotArm.grab()
for n in range(9):
    robotArm.moveRight()
robotArm.drop()
for n in range(9):
    robotArm.moveLeft()
robotArm.grab()
for n in range(9):
    robotArm.moveRight()
robotArm.drop()
for n in range(9):
    robotArm.moveLeft()
robotArm.grab()
for n in range(9):
    robotArm.moveRight()
robotArm.drop()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()