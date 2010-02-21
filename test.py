#!/usr/bin/python

from Note import *
from Interval import *
from Neck import *

def test_notes():
    assert A == A0
    assert G == G0
    assert A == A1
    assert C == C3
    assert C != A3
    assert A2 != A3
    
    assert A + 2 == B
    assert A + 14 == B
    assert G + 2 == A
    assert A3 + 2 == B3
    assert G3 + 14 == A5
    
    assert A - 2 == G
    assert A - 14 == G
    assert A3 - 2 == G2
    assert G3 - 14 == F2

def test_neck():
    n = E9_Neck()

    print n[0][0] == Fs4
    print n[0][12] == Fs5
    print n[9][12] == B4
