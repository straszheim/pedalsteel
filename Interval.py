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

    def __str__(self):
        return "Interval(%d)" % (self.value)

    def __repr__(self):
        return "Interval(%d)" % (self.value)

