from gopigo import *
print("Hi grace")
while True:
    turn = int(input("How much would you like to turn?"))
    rspeed = int(input("What would you like for your right speed?"))
    lspeed = int(input("What would you like for your left speed?"))

    set_left_speed(lspeed)
    set_right_speed(rspeed)
    enc_tgt(1, 1, turn)
    right_rot()

    time.sleep(2)

    ##left_rot(turn)