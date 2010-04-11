#!/usr/bin/env python

import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

from pprint import pprint
from copy import deepcopy
from operator import and_, or_

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
from Grip import *

#pprint(Pedals.combinations)

neck = NeckModel(E9)

g.setdisplay(g.scaletones)
g.tonic[0] = E

whichchord = sys.argv[1]
print "Looking for", whichchord 

print "The neck:\n"

for i in range(9,-1,-1):

    print " %-5s" % g.letter(neck[i][0]),

    for tstring in range(10):
        g.tonic[0] = neck[tstring][0]

        print "%-4s" % neck[i][0],

    print 
print '-'*40

def score(thingy, chord):

    trimmed = list(thingy)
    while trimmed[0] == None:
        trimmed = trimmed[1:]
    
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
candgrips = []

g.setdisplay(g.scaletones)

for combo in Pedals.combinations:
    for tonicstring in range(0,8):
        neck.allup()
        for p in combo:
            neck.toggle(p)
            
        g.tonic[0] = neck[tonicstring][0]
        soughtchord = getattr(g.tonic[0], whichchord)

        for n in soughtchord:
            n.octave = None

        notes = [neck[x][0] for x in range(10)]
        #print "notes=", notes
        assert len(notes) == 10

        result = ()
        for n in notes:
            if n in soughtchord:
                result += (n,)
            else:
                result += (None,)

        s = score(result, soughtchord)
        # print result, " scored ", s, " relative to", soughtchord
        if s < 1000:
            print "Tonic on string", tonicstring, g.tonic[0], " pedals:", combo, " ==>", result
            print "sought:", soughtchord
            candidates += [(s, combo, result, tonicstring)]
            candgrips += [(s,
                           Grip(combo,
                                [int(x != None) for x in result],
                                neck,
                                tonicstring).normalize())]


neck.allup()
# sys.exit(0)
# candidates.sort(cmp=lambda x,y: x[0] - y[0])

candgrips = g.uniqify(candgrips, lambda x: x[1])

candgrips = g.thin(candgrips, Grip.superset_of, lambda x: x[1])

for c in candgrips:
    print c[0],'\n', str(c[1]), '\n'

sys.exit(1)
redundant_grips = []

print "Done searching.\n", '-'*40, "\nCandidates:"

pprint(candidates)
# pprint(candgrips)
# sys.exit(1)
def clean(l, pred):

    todelete = []
    end = len(l)
    for x in range(len(l)):
        for y in range(x+1, len(l)):
            if pred(l[x], l[y]):
                todelete += [l[y]]

    cleaned = []
    for x in l:
        if x not in todelete:
            cleaned += [x]
    return cleaned

# grips = [Grip(p, s).normalize(tuning) for (score, p, s, tonicstring) in candidates]

# clean(grips, Grip.superset)

# pprint(grips)

# pprint(reversed)

# l = [(score,pedals,grip) for (grip,(pedals,score)) in reversed.items()]
# l.sort(cmp=lambda x,y: x[0]-y[0])

print '-'*40
for score, pedals, grip, tonicstring in candidates:
    print

    pedline = [''] * 10
    for p in pedals:
        for i in range(10):
            if neck.copedent[p][i] != 0 and pedline[i] != None:
                pedline[i] = "%-3s" % p

    for i in range(10):
        if pedline[i] == '':
            pedline[i] = '...'

    g.tonic[0] = grip[tonicstring]
    print "tonic %s, on string %d" % (g.letter(g.tonic[0]), tonicstring)

    printy = ["%-3s" % g.pretty(x) if x != None else '...' for x in grip]
    printy = ['...'] * (10-len(printy)) + printy
    print "tonicstring=", tonicstring
    print ' '.join(pedline), "   ", score
    print ' '.join([x.encode('UTF-8') for x in printy]) 
    # print score, pedals, grip
