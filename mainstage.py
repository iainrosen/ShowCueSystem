import scs
import os
import sys
while True:
    cmd = raw_input("MainstageCLI>>> ")
    if cmd == "open":
        try:
            show = raw_input("Show Name: ")
            ffile = open(show, 'r')
            scap = ffile.readlines()
            prod = scap[0].rstrip()
            auth = scap[1].rstrip()
            ffile.close()
            print "Production: " + prod
            print "Author: " + auth
            break
        except:
            print "Show Not Found!"
    if cmd == "new":
        show = raw_input("Show Name: ")
        prod = raw_input("Full Production Name: ")
        auth = raw_input("Author: ")
        if scs.newshow(show, prod, auth) == 1:
            print "Error. Show Already Exists!"
            overr = raw_input("Overwrite(Y/N)? ")
            if overr == "y" or overr == "Y":
                print "Overwriting Show File..."
                os.remove(show)
                scs.newshow(show, prod, auth)
            else:
                print "Show Creation Failure."
        else:
            print "Show Created Successfully."
        break
while True:
    scs.cls()
    print "Open Show Mode"
    print ""
    cmd = raw_input("MainstageCLI>>> ")
    if cmd == "exit":
        sys.exit()
    if cmd == "del":
        c = raw_input("Delete Cue: ")
        scs.cdel(c, show)
    if cmd == "new":
        scs.cls()
        print "Cue Recording Mode. Type 'end' and [ENTER] to exit."
        print ""
        while True:
            cue = raw_input("Cue Number: ")
            if cue == "end":
                break
            desc = raw_input("Cue Description: ")
            scs.crec(cue, show, desc)
    if cmd == "play":
        c = raw_input("Play Cue: ")
        scs.cls()
        print "Indexing..."
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
        scs.cls()
        while True:
            print "Playback Mode."
            print ""
            print "---------------------------------------------------------------------------------------"
            print "   |Cue Number|  |Cue Description|"
            try:
                print "     " + cues[pos - 3] + "           " + scs.cread(cues[pos - 3], show)
                print "     " + cues[pos - 2] + "           " + scs.cread(cues[pos - 2], show)
                print "     " + cues[pos - 1] + "           " + scs.cread(cues[pos - 1], show)
                print ""
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
            scs.cls()
            if next == "q":
                break
            if next == "":
                pos = pos + 1
            if next == "w":
                pos = pos - 1
