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
    STOP_DIST = 20
    # Turn speed ? adjust speeds if needed
    RIGHT_SPEED = 150
    LEFT_SPEED = 150
    turn_track = 0.0
    TIME_PER_DEGREE = .011
    # this tells how long it takes for robot to turn 1 degree
    TURN_MODIFIER = .41
    # this number is multiplied by the speed and it modifies it
    # scan = [None] * 180


    # CONSTRUCTOR
    def __init__(self):
        print("Piggy has been instantiated!")
        ## set speed method, right and left speeds are loaded here
        self.setSpeed(self.LEFT_SPEED, self.RIGHT_SPEED)
        # let's use an event-driven model, make a handler of sorts to listen for "events"
        while True:
            self.stop()
            self.menu()
        # asking if I want to calibrate head

    ## call methods based on response
    def menu(self):
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
        # set speed back to normal bc we only adjust it for turns

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
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        print("[ Press CTRL + C to stop me, then run stop.py ]\n")
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        # main app loop
        while True:
            if self.isClear():
                self.cruise()
                # repeat this to make it double check, is it really able to go forward?
                # robot will cruise for a while until it sees something
            self.backUp()
            # if I had to stop, pick a better path
            turn_target = self.kenny()
            if turn_target > 0:
                self.turnR(turn_target)
                #neg degrees means left
            else:
                self.turnL(abs(turn_target))
                # this takes care of neg with absolute values

    #########################################
    ### QUICK CHECK - is it safe to drive forward?

    #This returns true or false
    def isClear(self) -> bool:
        #YOU DECIDE: What range from our midpoint should we check?
        for x in range((self.MIDPOINT - 20), (self.MIDPOINT + 20), 4):
            #move the sensor
            servo(x)
            #Give a little time to turn the servo
            time.sleep(.1)
            #Take our first measurement
            scan1 = us_dist(15)
            #Give a little time for the measurement
            time.sleep(.1)
            #Take the same measurement
            scan2 = us_dist(15)
            # Give a little time for the measurement
            time.sleep(.1)
            #if there's a significant difference between the measurements
            if abs(scan1 - scan2) > 2:
                #take a third measurement
                scan3 = us_dist(15)
                time.sleep(.1)
                #take another scan and average? the three together - you decide
                scan1 = (scan1 + scan2 + scan3) / 3
            #store the measurement in our list
            self.scan[x] = scan1
            #print the finding
            print("Degree: " + str(x) + ", distance: " + str(scan1))
            #If any one finding looks bad
            if scan1 < self.STOP_DIST:
                print("\n--isClear method returns FALSE--\n")
                return False
        print("\n--isClear method returns TRUE--\n")
        return True



    def cruise(self):
        servo(self.MIDPOINT)
        time.sleep(.1)
        fwd()
        while True:
            if us_dist(15)< self.STOP_DIST:
                self.stop()
                if us_dist(15) < self.STOP_DIST:
                    break
                else:
                    fwd()
                    continue
            time.sleep(.05)
        self.stop()

    def backUp(self):
        # will check to see if something is up in its face
        if us_dist(15) < 15:
            print(" Too close, backing up")
            bwd()
            # sleep for .5 sec
            time.sleep(.2)
            self.stop()

    # REPLACEMENT TURN METHOD instead of choosePath, find best option to turn
    def kenny(self):
        # use built-in wide scan
        self.wideScan()
        # will double check, if finds that first scan is different, take a 2nd or 3rd scan & average to be extra sure
        # count will keep track of contigeous positive readings
        count = 0
        # list of all open paths we detect
        option = [0]
        SAFETY_BUFFER = 30
        # what increment do you have your widescan set to?
        INC = 2

        #############################
        ##### Build the options #####
        #############################
        # brackets makes it a list, first item is 0
        for x in range(self.MIDPOINT - 60, self.MIDPOINT + 60):
            if self.scan[x]:
                # if there is an actual value in x, consider it. otherwise skip over it
                if self.scan[x] > self.STOP_DIST + SAFETY_BUFFER:
                        # add 30 if necessary, safety buffer
                    count += 1
                else:
                    count  = 0
            # reset the count, path won't work
                if count == (17/INC) -1:
                    # Success! Found enough positive readings in a row to count
                    print("Found an option from " + str(x - 17) + "to " + str(x))
                        # set counter again for the next time
                    count = 0
                    option.append(x-8)
                    # we are done finding spots, list options

        #########################
        ### Pick from options ###
        #########################
        bestoption = 2000
        ideal_angle = self.MIDPOINT + self.turn_track
        print("\nTHINKING. Ideal turn: " + str(ideal_angle) + " degrees\n")
        for x in option:
            if x != 0:
                # skip filler option
                # the change to the midpoint needed to aim at this path
            # state our logic so debugging is easier
                print("\nPATH @  " + str(x) + " degrees means a turn of " + str(turn))
            # if this option is closer to our ideal than our current best option...
                if abs(ideal_angle - bestoption) > abs(ideal_angle - x):
                    # store this turn as the best option
                    bestoption = x
            bestoption = self.MIDPOINT - bestoption
        if bestoption > 0:
            input("\nABOUT TO TURN RIGHT BY: " + str(bestoption) + " degrees")
        else:
            input("\nABOUT TO TURN LEFT BY: " + str(abs(bestoption)) + " degrees")
        if bestoption != 2000 and abs(bestoption) >5 and abs(bestoption) < 190:
            return bestoption
        else:
            return -self.turn_track




    #######################################################################################
    # this code helps me to calibrate motor speed, told me if it was driving straight

    def calibrate(self):
        print("Calibrating...")
        servo(self.MIDPOINT)
        response = input("Am I looking straight ahead? (y/n): ")
        if response == 'n':
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
############### STATIC FUNCTIONS

def error():
    print('Error in input')

def quit():
    raise SystemExit


####################################################
######## THE ENTIRE APP IS THIS ONE LINE....
g = GoPiggy()