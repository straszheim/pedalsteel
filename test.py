#!/usr/bin/python

import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

from Global import *
from Note import *
from Interval import *
from Neck import *
from Pedals import *
from Grip import *

import Note as nmod

def eql(l, r):
    if l == r:
        return
    else:
        print "ERROR"
        print "l=", l
        print "r=", r
        assert l == r
        

def test_notes():
    assert A == A^0
    assert G == G^0
    assert A == A^1
    assert C == C^3
    assert C != A^3
    assert A^2 != A^3
    
    assert A + 2 == B
    assert A + 14 == B
    assert G + 2 == A
    assert (A^3) + 2 == B^3
    assert (B^3) + 14 == Cs^5
    
    assert A - 2 == G
    assert A - 14 == G
    assert (A^3) - 2 == G^3
    assert (C^3) - 2 == Bb^2
    assert (C^3) - 2 == As^2
    assert (G^3) - 14 == F^2

    nmod.show_octave[0] = True

    assert (G^3) + m3 == Bb^3
    assert (G^3) + m3 == Bb

    assert (G^3) + M3 == B^3
    assert (G^3) + M3 == B

def test_neck():

    n = NeckModel(E9)
    print n[0][0] == Fs^4
    print n[0][12] == Fs^5
    print n[9][12] == B^4


def test_chords():

    assert C in C.M7
    assert E in C.M7
    assert G in C.M7
    assert B in C.M7

    assert C in C.m7
    assert Eb in C.m7
    assert G in C.m7
    assert Bb in C.m7
    assert B not in C.m7

    assert all([x in C.m7b5 for x in m7b5])
    
    assert A in A.x7
    assert Cs in A.x7
    assert E in A.x7
    assert G in A.x7
    assert Gb not in A.x7
    assert Ab not in A.x7

def test_globals():
    assert scaletones[sharp][3] == '2s'
    eql(solfege[sharp][3], 'Ri')
    eql(letternotes[sharp][3], 'Ri')
    
def test_pedals():
    assert P1 < P2

