#!/usr/bin/python

import sys
from curses import *
from Note import *
from Interval import *
from Neck import *

sc = initscr()
start_color()
sc.border(0)
sc.refresh()

init_pair(1, COLOR_WHITE, COLOR_BLACK)
white = color_pair(1)
init_pair(2, COLOR_RED, COLOR_BLACK)
red = color_pair(2)
init_pair(3, COLOR_GREEN, COLOR_BLACK)
green = color_pair(3)
init_pair(4, COLOR_CYAN, COLOR_BLACK)
cyan = color_pair(4)
init_pair(5, COLOR_MAGENTA, COLOR_BLACK)
magenta = color_pair(5)
init_pair(6, COLOR_YELLOW, COLOR_BLACK)
yellow = color_pair(6)


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
            c = green if emph(s) else white
            sc.addstr (sn+yoff, xoff+fret*fretwidth, str(s), c) #A_NORMAL)
            s = +s
        
def emph(s):
    return s in [E,G,B]

try:
    print_neck(open_g, emph)
    sc.refresh()
    sc.getch()
finally:
    endwin()
