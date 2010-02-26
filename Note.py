#!/usr/bin/python

import sys

sharp_notes = list(enumerate(['C', 'Cs', 'D', 'Ds', 'E', 'F',
                              'Fs', 'G', 'Gs', 'A', 'As', 'B']))

flat_notes = list(enumerate(['C', 'Db', 'D', 'Eb', 'E', 'F',
                             'Gb', 'G', 'Ab', 'A', 'Bb', 'B']))

notes = flat_notes

value2flat = dict(flat_notes)
value2sharp = dict(sharp_notes)

value2letter = {}
letter2value = {}

def use_flats():
    global value2letter, letter2value, notes
    notes = flat_notes
    value2letter = dict(notes)
    letter2value = dict([(y,x) for (x,y) in notes])


def use_sharps():
    global value2letter, letter2value, notes
    notes = sharp_notes
    value2letter = dict(notes)
    letter2value = dict([(y,x) for (x,y) in notes])

use_flats()

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

    def addone(self, x):
        return x + 1

    def __add__(self, howmuch):
        n = Note(self.octave, self.value)
        n.value += howmuch
        n.normalize()
        return n

    def __sub__(self, howmuch):
        n = Note(self.octave, self.value)
        n.value -= howmuch
        n.normalize()
        return n

    def __eq__(self, other):
        if self.octave == None or other.octave == None:
            return self.value == other.value
        else:
            return self.octave == other.octave and self.value == other.value

    def __str__(self):
        self.normalize()
        return value2letter[self.value] + str(self.octave)

    def __repr__(self):
        return str(self)

#
# generate notes and exec
#

values_file = open("NoteValues.py", "w")
values_file.write("print 'importing values'\n")

values_file.write("print '....>', dir()\n")

print notes
for value, letter in sharp_notes + flat_notes:
    values_file.write('%s = Note(octave=None, value=%s)\n' % (letter, value))

for octave in range(10):
    for value, letter in sharp_notes + flat_notes:
        values_file.write("%s%d = Note(value=%d, octave=%d)\n" % (letter, octave, value, octave))

values_file.close()

execfile('NoteValues.py')

