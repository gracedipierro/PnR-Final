import pigo
import time
import random
from gopigo import *

'''
This class INHERITS your teacher's Pigo class. That means Mr. A can continue to
improve the parent class and it won't overwrite your work.
'''
## TODO from the board in class: Calibrate, Cruise, Turn Track, Turn options, other
## TODO add some more class variables up at the top

class GoPiggy(pigo.Pigo):
    # CUSTOM INSTANCE VARIABLES GO HERE. You get the empty self.scan array from Pigo
    # You may want to add a variable to store your default speed
    # capital stuff doesn't change while the app is running, turn track constantly changes
    MIDPOINT = 89
    STOP_DIST = 30
    #Turn speed ?
    RIGHT_SPEED = 200
    LEFT_SPEED = 200
    turn_track = 0
    # every time I use encR or L I want to adjust the number and print it as well (below)
    # instance variables
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
## asking if I want to calibrate head

    ##### HANDLE IT
    def handler(self):
        ## This is a DICTIONARY, it's a list with custom index values
        # You may change the menu if you'd like
        menu = {"1": ("Navigate forward", self.nav),
                "2": ("Rotate", self.rotate),
                "3": ("Dance", self.dance),
                "4": ("Calibrate", self.calibrate),
                ## this will calibrate motor speed now instead of servo
                #does servo first as midpoint and then the motors
                "q": ("Quit", quit)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        #
        ans = input("Your selection: ")
        menu.get(ans, [None, error])[1]()

##################################################################################################################
    # A SIMPLE DANCE ALGORITHM
    def dance(self):
        print("Piggy dance")
        ##### WRITE YOUR FIRST PROJECT HERE
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
#################################################################################################################S

    ### MY NEW TURN METHODS BC encR and encL just don't cut it
    # takes number of degs and turns right accordingly
    def turnR(self, deg):
        self.turn_track += deg
        print("The exit is " +str(self.turn_track) + " degrees away.")
        self.setSpeed(self.LEFT_SPEED * self.TURN_MODIFIER, self.RIGHT_SPEED * self.TURN_MODIFIER)
        right_rot()
        time.sleep(deg * self.TIME_PER_DEGREE)
        self.stop()
        #sets speed back to default at top of code
        self.setSpeed(self.LEFT_SPEED, self.RIGHT_SPEED)


    def turnL(self, deg):
        # adjust the tracker so we know how many degrees away our exit is
        self.turn_track -= deg
        print("The exit is " + str(self.turn_track) + " degrees away.")
        self.setSpeed(self.LEFT_SPEED * self.TURN_MODIFIER, self.RIGHT_SPEED * self.TURN_MODIFIER
        # use our experiments to calculate the time needed to turn
        left_rot()
        time.sleep(deg * self.TIME_PER_DEGREE)
        self.stop
        self.setSpeed(self.LEFT_SPEED, self.RIGHT_SPEED)
        #set speed back to normal bc we only adjust it for turns

    def setSpeed(self, left, right):
        print("Left speed: " + str(left))
        print("Right speed: " + str(right))
        set_left_speed(int(left))
        set_right_speed(int(right))
        time.sleep(.05)


    # AUTONOMOUS DRIVING
    def nav(self):
        print("Piggy nav")
        # WRITE YOUR FINAL PROJECT HERE
        # if loop fails, it will check for other paths
        # loop: first check that it is clear, also with nested loop
        while True:
            while self.isClear():
            # go forward 10 if it is clear
                self.encF(5)
            self.stop()
            # trying to get robot to choose a new path if it cannot go forward
            answer = self.choosePath()
            # if the path is clear to the left, it will go left 5
            if answer == "left":
                self.turnL(45)
            # if the path is clear to the right and not left it will go right
            elif answer == "right":
                self.turnR(45)
                ## how many degrees do we actually want to turn ?



#################################################################################################################
####THIS CODE IS NO LONGER USED FOR NAV BUT ONLY FOR DANCE I THINK
    ## every time robot turns it will print how much it will turn to get back on track
    def encR(self, enc):
        self.turn_track -= enc
        ## subtract same amount that is encoded
        super(pigo.Pigo, self).encR(enc)
        ## error here, object super no attribute encR
    def encL(self, enc):
        self.turn_track += enc
        if(self.turn_track > 0):
            # turn track is pos, (facing left) needs to turn right to face exit
            print("The exit is to my right by" + str(self.turn_track) + "units")
            # exit is to right by however much turn track is
        else:
            print("The exit is to my left by" + str(abs(self.turn_track)) + "units")
        super(pigo.Pigo, self).encL(enc)
    ### if this works, learn how robot uses rotate method to measure what each encode unit means in degrees
    ### can figure out how much we want to turn, but first see if we can track accurately
        ### TODO: test this out

##################################################################################################################
############### STATIC FUNCTIONS

def error():
    print('Error in input')


def quit():
    raise SystemExit


####################################################
######## THE ENTIRE APP IS THIS ONE LINE....
g = GoPiggy()
