#!/usr/bin/python

import sys
from curses import *
sc = initscr()
start_color()
from Colors import *


from Note import *
from Interval import *
from Neck import *

sc.border(0)
sc.refresh()


nfrets = 17

xoff = 5
yoff = 5
fretwidth = 5

chordcolors = [cyan, magenta, yellow, green]

for f in range(nfrets):
    pass # sc.addstr(yoff-1, xoff+f*fretwidth, str(f), red)

for y in [yoff-1, yoff+10]:
    sc.addstr(y, xoff, '|', red)
    sc.addstr(y, xoff+3*fretwidth, 'o', red)
    sc.addstr(y, xoff+5*fretwidth, 'o', red)
    sc.addstr(y, xoff+7*fretwidth, 'o', red)
    sc.addstr(y, xoff+9*fretwidth, 'o', red)
    sc.addstr(y, xoff+12*fretwidth, 'oo', red)
    sc.addstr(y, xoff+15*fretwidth, 'o', red)
    sc.addstr(y, xoff+17*fretwidth, 'o', red)
    sc.addstr(y, xoff+19*fretwidth, 'o', red)
    sc.addstr(y, xoff+21*fretwidth, 'o', red)
    sc.addstr(y, xoff+24*fretwidth, 'oo', red)
    
def print_neck(tuning, emph):

    for (sn, s) in enumerate(tuning):
        # print "|",
        for fret in range(nfrets+1):
            c = green if emph(s+fret) else white
            sc.addstr (sn+yoff, xoff+fret*fretwidth, str(s+fret), c)
        
def emph(s):
    return s in [E,B]

try:
    n = E9_Neck()
    n.render(sc, emph)

    sc.refresh()
    sc.getch()
finally:
    endwin()
