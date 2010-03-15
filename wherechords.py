#!/usr/bin/env python

import sys
reload(sys)
print sys.setdefaultencoding('UTF-8')

from pprint import pprint

# sys.path += ['/home/troy/Projects/pedalsteel/pydee/pydeelib']
# import pydee

import math
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *

import Global as g
from Note import *
import Note as Notemodule
from Neck import *
import Chord
import Pedals
pprint(Pedals.combinations)
neck = NeckModel(E9)

g.setdisplay(g.scaletones)
g.tonic[0] = E

print "\n"

for i in range(10):

    print " %-5s" % g.letter(neck[i][0]),

    for tstring in range(10):
        g.tonic[0] = neck[abs(tstring-9)][0]

        print "%-4s" % neck[i][0],

    print 

print
print

def score(thingy, chord):

    trimmed = list(thingy)
    while trimmed[-1] == None:
        trimmed = trimmed[:-1]
    

    missing = 0
    for n in chord:
        if n not in thingy:
            return 1000

    found = [False, False, False]
    space = 0
    deadstrings = 0
    for i in range(len(trimmed)):
        space += 1
        if thingy[i] == chord[0]:
            found[0] = True
        if thingy[i] == chord[1]:
            found[1] = True
        if thingy[i] == chord[3]:
            found[2] = True
        if thingy[i] == None:
            deadstrings += 1
        if all(found):
            break

    return space + deadstrings
    
            
    


candidates = []

for combo in Pedals.combinations:
    for i in range(10,2, -1):
        print "%2d: " % i,
        sn = i-1

        neck.allup()
        for p in combo:
            neck.toggle(p)
            
        print combo

        g.tonic[0] = neck[sn][0]

        soughtchord = g.tonic[0].x7b5


        for n in soughtchord:
            n.octave = None

        #for offset in range(sn, 0, -1):
        notes = [neck[x][0] for x in range(sn, -1, -1)]
        print notes

        result = ()
        # print soughtchord
        for n in notes:
            # print ">>", n, "?"
            if n in soughtchord:
                result += (n,)
            else:
                result += (None,)

        print result

        s = score(result, soughtchord)
        if s < 1000:
            candidates += [(s, combo, result)]

candidates.sort(cmp=lambda x,y: x[0] - y[0])

print "CANDIDATES:"

reversed = {}

for c in candidates:
    if c[2] not in reversed:
        reversed[c[2]] = (c[1], c[0])
    elif len(reversed[c[2]][0]) > len(c[1]):
        reversed[c[2]] = (c[1], c[0])
    else:
        print "Tossing   ", c
        print "in lieu of", reversed[c[2]]

pprint(reversed)

l = [(score,pedals,grip) for (grip,(pedals,score)) in reversed.items()]
l.sort(cmp=lambda x,y: x[0]-y[0])

for score, pedals, grip in l:
    g.tonic[0] = grip[0]
    printy = ["%-2s" % unicode(x) if x != None else '..' for x in grip]
    printy = ['..'] * (10-len(printy)) + printy
    print "%20s   %s" % (pedals, ' '.join(printy)) 

