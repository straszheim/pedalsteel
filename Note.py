#!/usr/bin/python

import sys
from Global import *
from Interval import Interval
from Chord import *

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

    @property
    def M7(self):
        return [self + x for x in M7]

    @property
    def m7(self):
        return [self + x for x in m7]

    @property
    def x7(self):
        return [self + x for x in x7]

    @property
    def x7b5(self):
        return [self + x for x in x7b5]

    @property
    def m7b5(self):
        return [self + x for x in m7b5]

    @property
    def d7(self):
        return [self + x for x in d7]

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
        if self.octave == None or other.octave == None:
            return self.value == other.value
        else:
            return self.octave == other.octave and self.value == other.value

    def __str__(self):
        self.normalize()
        return pretty(self)

    def as_flat(self):
        return pretty(self)

    def as_sharp(self):
        return pretty(self)

    def as_letter(self):
        self.normalize()
        return self.as_sharp()

    def __repr__(self):
        return str(self)

#
# generate notes and exec
#

values_file = open("NoteValues.py", "w")
values_file.write("print 'importing values'\n")

values_file.write("print '....>', dir()\n")

for value, letter in list(enumerate(letternotes[sharp][ALL])) + \
        list(enumerate(letternotes[flat][ALL])):
    values_file.write('%s = Note(octave=None, value=%s)\n' % (letter, value))

#for octave in range(10):
#    for value, letter in sharp_notes + flat_notes:
#        values_file.write("%s%d = Note(value=%d, octave=%d)\n" % (letter, octave, value, octave))

values_file.close()

execfile('NoteValues.py')


