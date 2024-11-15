import os
import random
import time

random.seed(os.urandom(32))
def guesrand():

    guess=int(input("guess \n > "))
    randbit = int(random.getrandbits(32))
    if (guess!=randbit):
        print (randbit,"\n")
        return 0
    else:
        print ("Flag{wh4t_1s_0n_m0n4'5_m1nd}",guess,"=",randbit)
        return 1


if __name__ == '__main__':
    print("I kept a 32 bit number in my mind if you find this number I will give you a flag ")
    c=0
    while not c:
        c=guesrand()



