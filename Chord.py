#!/usr/bin/python

import sys
from Note import *
from Interval import *

#
# generate chords and exec
#

m7 = [P1, m3, P5, m7]
M7 = [P1, M3, P5, M7]
x7 = [P1, M3, P5, m7]
x7b5 = [P1, m3, d5, m7]
d7 = [P1, m3, d5, d7]

chord_types = { 'm7' : m7,
                'M7' : M7,
                'x7' : x7,
                'x7b5' : x7b5,
                'd7' : d7 }



