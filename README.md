# PnR-Final
The final project for my Programming and Robotics class

below are some methods used in my Programming and Robotics final.

explain and reference, aim to self in the future



'menu(self)' - This is a dictionary, that means it is a list with custom index values.
In my project, I have several options in the menu. There is a navigate forward option,
and this is my self.nav method, which basically just lets the robot start going. There
is also a dance option, this tells the robot to start the dance method. Calibrate helps
to calibrate the motor speeds. It actually calibrates the servo(head) to the midpoint
first by default, and then it calibrates the motors. Quit is also an option, and that
is for when I need to quit the app.


'dance(self)' - This method is a simple dance algorithm that tells the robot to do a
funky dance using encR and encL etc.

'turnR(self, deg)' - This method replaced encR because it was inefficient. These are
better methods because they are based on degrees and time instead of spoke values,
which were not very accurate.

'turnL(self, deg)' - This
setSpeed(self, left, right)
        # AUTONOMOUS DRIVING
    # central logic loop of my navigation

def nav(self)
    #This returns true or false
def isClear(self) -> bool:
cruise(self):
backUp(self):
    # REPLACEMENT TURN METHOD instead of choosePath, find best option to turn
def kenny(self):

    # this code helps me to calibrate motor speed, told me if it was driving straight
calibrate(self):
error():
quit():