#!/usr/bin/python

import sys
import Global as g
from Interval import Interval
from Chord import *

class Note:
    
    __metaclass__ = NoteMeta
    
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

    def normalize(self):
        while self.value >= 12:
            self.value -= 12
            if self.octave != None:
                self.octave += 1
        while self.value < 0:
            self.value += 12
            if self.octave != None:
                self.octave -= 1

    def __pos__(self):
        n = Note(self.octave, self.value)
        n.value += 1;
        if n.value == 12:
            n.value = 0
            n.octave += 1
        return n

    def __xor__(self, o):
        n = Note(o, self.value)
        return n

    def addone(self, x):
        return x + 1

    def __add__(self, howmuch):
        n = Note(self.octave, self.value)
        n.value += (howmuch.value if isinstance(howmuch,Interval) else howmuch)
        n.normalize()
        return n

    def __sub__(self, howmuch):
        n = Note(self.octave, self.value)
        n.value -= (howmuch.value if isinstance(howmuch,Interval) else howmuch)
        n.normalize()
        return n

    def __eq__(self, other):
        # print "eq", self, other, "?"
        if other == None:
            return False
        if self.octave == None or other.octave == None:
            return self.value == other.value
        else:
            return self.octave == other.octave and self.value == other.value

    def __hash__(self):
        if self.octave == None:
            return self.value
        return self.octave * 12 + self.value

    def __str__(self):
        self.normalize()
        return g.pretty(self)

    def __repr__(self):
        return str(self)

#
# generate notes and exec
#

values_file = open('NoteValues.py.generated', 'w')

for value, letter in list(enumerate(g.letternotes[g.sharp][g.ALL])) + \
        list(enumerate(g.letternotes[g.flat][g.ALL])):
    values_file.write('%s = Note(octave=None, value=%s)\n' % (letter, value))

#for octave in range(10):
#    for value, letter in sharp_notes + flat_notes:
#        values_file.write("%s%d = Note(value=%d, octave=%d)\n" % (letter, octave, value, octave))

values_file.close()

execfile('NoteValues.py.generated')


