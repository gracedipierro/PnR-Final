# PnR-Final
The final project for my Programming and Robotics class

 The final project consisted of many trials and many more errors when experimenting
 with robots. We used the Python language to encode our robots to do certain things.
 The goal was to get a robot to go through a maze without any help from me.
 Programming the robot to do this proved to be difficult, but with hard work and
 perseverance, a solution was found. Below are some of the methods used.

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

'turnL(self, deg)' - This method replaced encL and tells the robot to turn left. This
    is also based on degrees instead of counting spokes on the wheel and it is much more
    efficient.

'setSpeed(self, left, right)' - This sets the speed and calibrate the motors for the
    whole thing but it is called again to change the speeds for turns. Once it calibrates
    speeds for turns, it reverts back to speed for normal driving.

'nav(self)' - This method is the central logic loop of my navigation and allows the
    robot to autonomously drive. First it will check to see if the path in front of it
    is clear, then it will cruise forward until it sees something. Then if it does see
    something, it will back up and look for a new path with the kenny method. Then the
    loop will repeat as many times as necessary.

    #This returns true or false
'isClear(self) -> bool' - This method returns true or false.
'cruise(self)' -

'backUp(self)' -
    # REPLACEMENT TURN METHOD instead of choosePath, find best option to turn
'kenny(self)' -

    # this code helps me to calibrate motor speed, told me if it was driving straight
'calibrate(self)' -

'error()' -

'quit()' -
