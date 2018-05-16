print "ShowEmu v0.0.1"
import os
import time
import sys
x = raw_input("Number of Mics: ")
x = int(x)
act = []

while True:
    os.system("cls")
    setact = "null"
    setoff = "null"
    b = 1
    while x >= b:
        if str(b) in act:
            print "Mic " + str(b) + " >> " + "ON"
        else:
            print "Mic " + str(b) + " >> "
        b = b + 1
    while setact != "":
        setact = raw_input("Set Active: ")
        act.append(setact)
    while setoff != "":
        setoff = raw_input("Set Off: ")
        if setoff in act:
            act.remove(setoff)
