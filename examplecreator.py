import scs
import random
import time
print "Writing Example Show File..."
scs.newshow("example", "Example Show", "Iain Rosen")
r = 0
while True:
    rndgo = random.randint(0,2)
    if rndgo == 0:
        desc = "LX GO"
    elif rndgo == 1:
        desc = "SFX GO"
    elif rndgo == 2:
        desc = "LX FADE"
    else:
        print "Error"
    if r == 0:
        c = 1
    else:
        c = random.randint(1, 999)
    c = str(c)
    show = "example"
    scs.crec(c, show, desc)
    r = r + 1
    if r == 100:
        print "Cues Created: " + str(r)
        time.sleep(5)
        break
    
