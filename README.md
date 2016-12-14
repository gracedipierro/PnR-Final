# PnR-Final
The final project for my Programming and Robotics class

 The final project consisted of many trials and many more errors when experimenting
 with robots. We used the Python language to encode our robots to do certain things.
 The goal was to get a robot to go through a maze without any help from me.
 Programming the robot to do this proved to be difficult, but with hard work and
 perseverance, a solution was found. Below are some of the methods used.

'handler (self)' - This is a dictionary, that means it is a list with custom index values.
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
    loop will repeat as many times as necessary.  Included in this is the cdoe for
    the backup, if it sees something that is too close, it will tell itself to back up
    and check for new paths.

'isClear(self) -> bool' - This method returns true or false because of the bool.
    It is what tells the robot to check its surroundings. First the sensor moves and
    takes the first measurement. Then it goes back and takes the same measurement and
    if there is a significant difference between them, then it will take a third.
    Then it will average all the scans and store them in a list. It will print
    the findings and if it any of them look bad, it will restart the method and look
    for new options.

'cruise(self' - This method is what tells the robot to go forward for as long as it
    can without stopping. Once it sees something, it will stop and look for a new
    option and/or back up if it is too close to something.

'calibrate(self)' - This code helps to calibrate the motor speed and will tell us if
    the robot is driving straight or not. You can reduce left, right, or encode the
    speed to find a more accurate speed for the motors.

'error()' - This is a method that prints a message when there is an error in the code.

'quit()' - This method quits the app when it senses an error.



