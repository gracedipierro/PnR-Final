import pigo
import time
import random
from gopigo import *

'''
This class INHERITS your teacher's Pigo class. That means Mr. A can continue to
improve the parent class and it won't overwrite your work.
'''

class GoPiggy(pigo.Pigo):
    # CUSTOM INSTANCE VARIABLES GO HERE. You get the empty self.scan array from Pigo
    # capital stuff doesn't change while the app is running, turn track constantly changes
    MIDPOINT = 89
    STOP_DIST = 30
        # speed of motors, can be adjusted if needed
    RIGHT_SPEED = 150
    LEFT_SPEED = 150
    turn_track = 0.0
    TIME_PER_DEGREE = .011
    # this tells how long it takes for robot to turn 1 degree
    TURN_MODIFIER = .41
    # this number is multiplied by the speed and it modifies it

    # CONSTRUCTOR
    def __init__(self):
        print("Piggy has been instantiated!")
        ## set speed method, right and left speeds are loaded here
        self.setSpeed(self.LEFT_SPEED, self.RIGHT_SPEED)
        # let's use an event-driven model, make a handler of sorts to listen for "events"
        while True:
            self.stop()
            self.handler()

    ##### HANDLE IT
    def handler(self):
        ## This is a DICTIONARY, it's a list with custom index values
        # You may change the menu if you'd like
        menu = {"1": ("Navigate forward", self.nav),
                "2": ("Rotate", self.rotate),
                "3": ("Dance", self.dance),
                "4": ("Calibrate", self.calibrate),
                ## this will calibrate motor speed instead of servo
                #calibrates servo first as midpoint and then the motors
                "q": ("Quit", quit)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])

        ans = input("Your selection: ")
        menu.get(ans, [None, error])[1]()

##################################################################################################################
    # A SIMPLE DANCE ALGORITHM
    def dance(self):
        print("Piggy dance")
        print('Is it safe to dance?')
        for x in range (100, 200, 25):
            if not self.isClear():
                print ("Not clear!")
                break
            print ('Speed is set to:'+ str(x))
            servo(60)
            set_speed(x)
            self.encB(5)
            self.encF(4)
            self.encL(3)
            servo(20)
            self.encR(3)
            self.encL(3)
            self.encB(3)
            self.encF(4)
            servo(115)
            self.encR(17)
            servo(30)
            self.encB(3)
            self.encL(4)
            servo(96)
            self.encF(5)
            time.sleep(.1)
##################################################################################################################

    ### NEW TURN METHODS BC encR and encL just don't cut it
    # takes number of degrees and turns right/left accordingly
    def turnR(self, deg):
        self.turn_track += deg
        print("The exit is " +str(self.turn_track) + " degrees away.")
        self.setSpeed(self.LEFT_SPEED * self.TURN_MODIFIER, self.RIGHT_SPEED * self.TURN_MODIFIER)
        right_rot()
        time.sleep(deg * self.TIME_PER_DEGREE)
        self.stop()
        # sets speed back to default at top of code
        # uses this speed for the turn and then reverts back
        self.setSpeed(self.LEFT_SPEED, self.RIGHT_SPEED)

    def turnL(self, deg):
        # adjust the tracker so we know how many degrees away our exit is
        self.turn_track -= deg
        print("The exit is " + str(self.turn_track) + " degrees away.")
        self.setSpeed(self.LEFT_SPEED * self.TURN_MODIFIER, self.RIGHT_SPEED * self.TURN_MODIFIER)
        # use our experiments to calculate the time needed to turn
        left_rot()
        time.sleep(deg * self.TIME_PER_DEGREE)
        self.stop()
        self.setSpeed(self.LEFT_SPEED, self.RIGHT_SPEED)

    # set speed is for the whole thing but it is called again to change the speed for the turn
    def setSpeed(self, left, right):
        print("Left speed: " + str(left))
        print("Right speed: " + str(right))
        set_left_speed(int(left))
        set_right_speed(int(right))
        time.sleep(.05)

##################################################################################################################

    # AUTONOMOUS DRIVING
    # central logic loop of my navigation
    def nav(self):
        print("Piggy nav")
        # if loop fails, it will check for other paths
        # main app loop
        while True:
            if self.isClear():
                self.cruise()
                # robot will cruise for a while until it sees something
            if us_dist(15) < 7:
                # when it stops it will check to see if something is up in its face
                # then it will back up and check for a new path
                self.encB(5)
            # trying to get robot to choose a new path if it cannot go forward
            answer = self.choosePath()
            # if the path is clear to the left, it will turn 45 degrees
            if answer == "left":
                self.turnL(45)
            # if the path is clear to the right and not left, it will go right
            elif answer == "right":
                self.turnR(45)
                ## how many degrees do we actually want to turn ?

    def cruise(self):
        # cruise method, tells it to go forward until something is in front of it
        servo(self.MIDPOINT)
        time.sleep(.1)
        fwd()
        while True:
            if us_dist(15)< self.STOP_DIST:
                break
            time.sleep(.05)
        self.stop()

###################################################################################################################
    # this code helps me to calibrate motor speed,
    # tells me if it was driving straight
    def calibrate(self):
        print("Calibrating...")
        servo(self.MIDPOINT)
        response = input("Am I looking straight ahead? (y/n): ")
        if response == 'n':
            # will ask what we want to do, turn r, l, or done?
            while True:
                response = input("Turn right, left, or am I done? (r/l/d): ")
                if response == "r":
                    self.MIDPOINT += 1
                    print("Midpoint: " + str(self.MIDPOINT))
                    servo(self.MIDPOINT)
                    time.sleep(.01)
                elif response == "l":
                    self.MIDPOINT -= 1
                    print("Midpoint: " + str(self.MIDPOINT))
                    servo(self.MIDPOINT)
                    time.sleep(.01)
                else:
                    print("Midpoint now saved to: " + str(self.MIDPOINT))
                    break
        response = input("Do you want to check if I'm driving straight? (y/n)")
        if response == 'y':

            while True:
                set_left_speed(self.LEFT_SPEED)
                set_right_speed(self.RIGHT_SPEED)
                print("Left: " + str(self.LEFT_SPEED) + "//  Right: " + str(self.RIGHT_SPEED))
                self.encF(19)
                response = input("Reduce left, reduce right or done? (l/r/d): ")
                if response == 'l':
                    self.LEFT_SPEED -= 10
                elif response == 'r':
                    self.RIGHT_SPEED -= 10
                elif response == 'd':
                    break

##################################################################################################################
###############
# STATIC FUNCTIONS

def error():
    print('Error in input')

def quit():
    raise SystemExit


####################################################
######## THE ENTIRE APP IS THIS ONE LINE....
g = GoPiggy()