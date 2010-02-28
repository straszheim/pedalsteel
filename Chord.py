#!/usr/bin/python

import sys
import Note as n
import Interval as i

#
# generate chords and exec
#

m7 = [i.P1, i.m3, i.P5, i.m7]

M7 = [i.P1, i.M3, i.P5, i.M7]

x7 = [i.P1, i.M3, i.P5, i.m7]

x7b5 = [i.P1, i.M3, i.d5, i.m7]
m7b5 = [i.P1, i.m3, i.d5, i.m7]
d7 = [i.P1, i.m3, i.d5, i.d7]

chord_types = { 'm7' : m7,
                'M7' : M7,
                'x7' : x7,
                'x7b5' : x7b5,
                'm7b5' : m7b5,
                'd7' : d7 }



