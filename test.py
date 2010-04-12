#!/usr/bin/python

import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

from Note import *
from Interval import *
from Neck import *
from Pedals import *
from Grip import *
import Global as g

import Note as nmod

from nose.tools import *

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

    g.show_octave[0] = True

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

    print C.M7
    assert C in C.M7
    assert E in C.M7
    assert G in C.M7
    assert B in C.M7

    assert C in C.m7
    assert Eb in C.m7
    assert G in C.m7
    assert Bb in C.m7
    assert B not in C.m7

    assert A in A.x7
    assert Cs in A.x7
    assert E in A.x7
    assert G in A.x7
    assert Gb not in A.x7
    assert Ab not in A.x7

def test_globals():
    eq_(g.scaletones[g.sharp][3], '#2')
    eq_(g.solfege[g.sharp][3], 'Ri')
    eq_(g.letternotes[g.sharp][3], 'Ds')
    
def test_pedals():
    assert P1 < P2

def test_grips():

    g1 = Grip([None, P1], [0,0,1])
    g2 = Grip([None, P1], [0,0,1])

    eq_(g1, g2)

    g2 = Grip([None, None], [0,0,1])

    assert_not_equal(g1, g2)
    
    assert not g1.superset_of(g2)
    g2.strings = [0,1,1]
    assert not g2.superset_of(g1)
    assert not g1.superset_of(g2)

def test_grip_normalize():
    print E9.tuning
    g = Grip([P1, P2], [1,0,0,0,0, 1,0,0,0,0], NeckModel(E9))
    h = g.normalize()
    print "normalized:", h
    assert P2 not in h.pedals
    print h.pedals
    assert h.pedals == set([P1])

    g = Grip([], [1,1,1,1,1, 1,1,1,1,1], NeckModel(E9))
    h = g.normalize()
    assert len(h.pedals) == 0

    g.pedals = set([P5])
    h = g.normalize()
    assert len(h.pedals) == 0

    g = Grip([P2, P3, P4, RL, RR], [0,0,0,0,0, 0,0,0,1,1], NeckModel(E9))
    h = g.normalize()
    assert h.pedals == set([RL, RR])

def test_grip_str():
    g = Grip([], [1, 1, 1, 0, 1,   1, 1, 0, 0, 0], tonicstring=2, neck=NeckModel(E9))
    s = str(g)
    print s

def test_grip_superset():
    g = Grip([], [1, 0, 0])
    h = Grip([], [1, 0, 1])
    assert g != h
    assert h.superset_of(g)
    assert not g.superset_of(h)
    h = Grip([], [1, 0, 0])
    assert g == h
    
    g = Grip([], [0, 0, 0])
    h = Grip([], [0, 0, 1])
    assert h.superset_of(g)
    assert not g.superset_of(h)

    g = Grip([P1], [0, 0, 0])
    h = Grip([], [0, 0, 1])
    assert not h.superset_of(g)
    assert not g.superset_of(h)

def test_unicode_display():
    p = g.pretty(As)
    print p.encode('UTF-8')
    print As
    print As

def test_neckmodel():
    n = NeckModel(E9)

    eq_(n[0][0], B)
    eq_(n[0][1], C)
    eq_(n[2][0], E)

    n.toggle(P1)
    eq_(n[0][0], Cs)
    eq_(n[0][3], E)
    n.toggle(P1)
    eq_(n[0][0], B)

    eq_(n[2][3], G)
    n.toggle(LL)
    eq_(n[2][3], Gs)
    n.toggle(LL)
    eq_(n[2][3], G)
    
def test_thin():
    import operator
    def betterthan(l, r):
        return l[0] == r[0] and len(l) > len(r)

    l = ["abcd", "a", "ab", "abc", "b", "bc"]
    r = g.thin(l, betterthan, lambda x: x)

    eq_(r,["abcd", "bc"])

    l = ['a1', 'b1', 'c1', 'a', 'd', 'b']
    r = g.thin(l, betterthan)
    eq_(set(r), set(['a1', 'b1', 'c1', 'd']))
    
def test_uniqify():
    l = [(9,1), (9,2), (8,2), (9,3)]
    eq_(g.uniqify(l, lambda x: x[1]), [(9,1), (9,2), (9,3)])

def test_notemeta():

    print Ds.x7s9alt

    
