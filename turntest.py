from gopigo import *
print("Hi grace")
while True:
    turn = int(input("How much would you like to turn?"))
    rspeed = int(input("What would you like for your right speed?"))
    lspeed = int(input("What would you like for your left speed?"))

    set_left_speed(lspeed)
    set_right_speed(rspeed)
    print(enc_tgt(1, 1, turn))
    right_rot()

    imput("Press any key to stop")
    #time.sleep(5)
    stop()
    ##left_rot(turn)