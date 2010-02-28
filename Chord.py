#!/usr/bin/python

import sys
import Note as n
import Interval as i

#
# generate chords and exec
#

M = [i.P1, i.M3, i.P5]
m = [i.P1, i.m3, i.P5]
d = [i.P1, i.m3, i.d5]

M7 = M + [i.M7]
x7 = M + [i.m7]
m7 = m + [i.m7]

x7b5 = [i.P1, i.M3, i.d5, i.m7]
m7b5 = d + [i.m7]
d7 = d + [i.d7]

chord_types = {
    'M' : M,
    'm' : m,
    'M7' : M7,
    'x7' : x7,
    'm7' : m7,
    'x7b5' : x7b5,
    'm7b5' : m7b5,
    'd7' : d7
    }



