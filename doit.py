#!/usr/bin/python

import mingus.core.notes as notes

class Note:
    def __init__(self, octave, value):
        self.octave = octave
        self.value = value

    def __neg__(self):
        n = Note(self.octave, self.value)
        n.value -= 1;
        if n.value == -1:
            n.value = 11
            n.octave -= 1
        return n

    def __pos__(self):
        n = Note(self.octave, self.value)
        n.value += 1;
        if n.value == 12:
            n.value = 1
            n.octave += 1
        return n

    def __str__(self):
        return "Note(%d, %d)" % (self.value, self.octave)

    def __repr__(self):
        return "Note(%d, %d)" % (self.value, self.octave)

class Interval:
    def __init__(self, value):
        self.value = value
        
    def __neg__(self):
        n = Interval(self.value)
        n.value -= 1;
        return n

    def __pos__(self):
        n = Interval(self.value)
        n.value += 1;
        return n

    def __str__(self):
        return "Interval(%d)" % (self.value)

    def __repr__(self):
        return "Interval(%d)" % (self.value)


n = Note(5,1)
print n
print -n
print --n
print ---n
print n
print +n
print ++n
print +++n


A = Note(4,0)
B = ++A
C = +B
D = ++C
E = ++D
F = +E
G = ++F

print [A,B,C,D,E,F,G]

i1 = Interval(1)
im2


# alpha beta gamma
# delta epsilon zeta
# eta theta iota
# kappa lambda mu


# notes:      ABCDEFG
# intervals:  1 2 -3 



