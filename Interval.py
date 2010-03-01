#!/usr/bin/python

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

    def __add__(self, other):
        n = Interval(self.value)
        n.value += other.value
        return n

    def __sub__(self, other):
        n = Interval(self.value)
        n.value -= other.value
        return n

    def __str__(self):
        return "Interval(%d)" % (self.value)

    def __repr__(self):
        return "Interval(%d)" % (self.value)


P1 = Interval(0)
m2 = Interval(1)
M2 = Interval(2)
m3 = Interval(3)
M3 = Interval(4)
P4 = Interval(5)

a4 = Interval(6)
d5 = Interval(6)

P5 = Interval(7)

a5 = Interval(8)
m6 = Interval(8)

M6 = Interval(9)
d7 = Interval(9)

m7 = Interval(10)
M7 = Interval(11)
P8 = Interval(12)
m9 = P8 + m2
M9 = P8 + M2
s9 = P8 + m3

m13 = P8 + m6
M13 = P8 + M6
