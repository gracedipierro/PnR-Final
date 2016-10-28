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
    # You may want to add a variable to store your default speed
    MIDPOINT = 89
    STOP_DIST = 30

    # CONSTRUCTOR
    def __init__(self):
        print("Piggy has be instantiated!")
        # this method makes sure Piggy is looking forward
        self.calibrate()
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
                "4": ("Calibrate servo", self.calibrate),
                "q": ("Quit", quit)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        #
        ans = input("Your selection: ")
        menu.get(ans, [None, error])[1]()

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
                self.encL(5)
            # if the path is clear to the right and not left it will go right
            elif answer == "right":
                self.encR(5)
        ### TODO: how to change how much it turns when it changes directions
                #TODO: add the test drive code and fix speed

####################################################
############### STATIC FUNCTIONS

def error():
    print('Error in input')


def quit():
    raise SystemExit


####################################################
######## THE ENTIRE APP IS THIS ONE LINE....
g = GoPiggy()
