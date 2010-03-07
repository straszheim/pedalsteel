#!/usr/bin/env python

import sys
reload(sys)
print sys.setdefaultencoding('UTF-8')

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

neck = E9_Neck()


g.displayer = [g.scaletones]
g.tonic[0] = E

print "\n"

for i in range(10):

    print " %-5s" % g.letter(neck[i][0]),

    for tstring in range(10):
        g.tonic[0] = neck[abs(tstring-9)][0]

        print "%-4s" % neck[i][0],

    print 

