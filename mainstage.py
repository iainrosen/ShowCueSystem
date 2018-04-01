import scs
import os
print "Mainstage CLI for ShowCueSystem"
print "Iain Rosen"
while True:
    cmd = raw_input("MainstageCLI>>> ")
    if cmd == "open":
        show = raw_input("Show Name: ")
        try:
            ffile = open(show, 'r')
            ffile.close()
            break
        except:
            print "Error. Show Not Found."
    if cmd == "new":
        show = raw_input("Show Name: ")
        prod = raw_input("Full Production Name: ")
        auth = raw_input("Author: ")
        scs.newshow(show, prod, auth)
        break
while True:
    cmd = raw_input("(SHOW OPEN) MainstageCLI>>> ")
    if cmd == "new":
        cue = raw_input("Cue Number: ")
        desc = raw_input("Cue Description: ")
        scs.crec(cue, show, desc)
    if cmd == "play":
        c = raw_input("Play Cue: ")
        if "." not in c:
            c = c + ".0"
        cues = scs.read(show)
        r = 0
        while True:
            try:
                if cues[r] == c:
                    pos = r
                    break
                else:
                    r = r + 1
            except:
                print "No Cue Exists."
                break
        while True:
            print "---------------------------------------------------------------------------------------"
            try:
                print "     " + cues[pos - 3] + "           " + scs.cread(cues[pos - 3], show)
                print "     " + cues[pos - 2] + "           " + scs.cread(cues[pos - 2], show)
                print "     " + cues[pos - 1] + "           " + scs.cread(cues[pos - 1], show)
            except:
                print " "
            try:
                print " >>> " + cues[pos] + "           " + scs.cread(cues[pos], show)
                print "     " + cues[pos + 1] + "           " + scs.cread(cues[pos + 1], show)
                print "     " + cues[pos + 2] + "           " + scs.cread(cues[pos + 2], show)
                print "     " + cues[pos + 3] + "           " + scs.cread(cues[pos + 3], show)
                print "     " + cues[pos + 4] + "           " + scs.cread(cues[pos + 4], show)
                print "     " + cues[pos + 5] + "           " + scs.cread(cues[pos + 5], show)
                print "     " + cues[pos + 6] + "           " + scs.cread(cues[pos + 6], show)
                print "     " + cues[pos + 7] + "           " + scs.cread(cues[pos + 7], show)
                print "     " + cues[pos + 8] + "           " + scs.cread(cues[pos + 8], show)
                print "     " + cues[pos + 9] + "           " + scs.cread(cues[pos + 9], show)
                print "     " + cues[pos + 10] + "           " + scs.cread(cues[pos + 10], show)
                print "---------------------------------------------------------------------------------------"
            except:
                print "End of Cues."
            next = raw_input("Next?")
            os.system("cls")
            if next != "":
                break
            else:
                pos = pos + 1
