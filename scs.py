#Show Cue Software
#Prep DB
import os
import time
import sys
def openshow(show):
    ffile = open(show, 'r')
    showc = ffile.readlines()
    ffile.close()
    while True:
        try:
            showc[r] = showc[r].rstrip()
            r = r + 1
        except:
            break
    return showc
def newshow(show, prod, auth):
    ffile = open(show, 'w')
    wrl(show, prod)
    wrl(show, auth)
    ffile.close()
def read(show):
    cues = []
    showc = openshow(show)
    r = 0
    c = 0
    c = long(c)
    c = 0.1
    while True:
        try:
            s = ":" + str(c) + ":"
            if str(s) == ":999.0:":
                break
            if s in showc[r]:
                #the cue is found
                f = s.strip(':')
                cues.append(f)
                c = c + 0.1
                r = 0
            else:
                r = r + 1
        except:
            c = c + 0.1
            r = 0
            #the cue doesn't exist
    return cues

def wrl(f, c):
    try:
        ffile = open(f, 'a')
        ffile.write(c)
        ffile.write('\n')
        ffile.close()
        return 0
    except:
        return 1
def cread(c, show):
    showc = openshow(show)
    r = 0
    s = ":" + str(c) + ":"
    while True:
        if s in showc[r]:
            cue = showc[r].strip((s + " "))
            cue = cue.rstrip()
            return cue
        else:
            r = r + 1

def crec(c, show, desc):
    #build the line
    if "." not in c:
        c = c + ".0"
    cue = ":" + c + ": " + desc
    wrl(show, cue)
    return 0
print "Show Cue Software"
print "Iain Rosen"
