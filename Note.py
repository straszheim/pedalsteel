#!/usr/bin/python

import sys

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
            n.value = 0
            n.octave += 1
        return n

    def addone(self, x):
        return x + 1

    def __add__(self, howmuch):
        n = Note(self.octave, self.value)
        n.value += howmuch
        while n.value >= 12:
            n.value -= 12
            if n.octave != None:
                n.octave += 1
        return n

    def __sub__(self, howmuch):
        n = Note(self.octave, self.value)
        n.value -= howmuch
        while n.value < 0:
            n.value += 12
            if n.octave != None:
                n.octave -= 1
        return n

    def __eq__(self, other):
        if self.octave == None or other.octave == None:
            return self.value == other.value
        else:
            return self.octave == other.octave and self.value == other.value

    def __str__(self):
        return value2letter[self.value] + str(self.octave)

    def __repr__(self):
        return str(self)

notes = list(enumerate(['A', 'As', 'B', 'C', 'Cs', 'D', 'Ds', 'E', 'F', 'Fs', 'G', 'Gs']))
value2letter = dict(notes)
letter2value = dict([(y,x) for (x,y) in notes])

#
# generate notes and exec
#

values_file = open("NoteValues.py", "w")
values_file.write("print 'importing values'\n")

values_file.write("print '....>', dir()\n")

print notes
for value, letter in notes:
    values_file.write('%s = Note(octave=None, value=%s)\n' % (letter, value))

for octave in range(10):
    for value, letter in notes:
        values_file.write("%s%d = Note(value=%d, octave=%d)\n" % (letter, octave, value, octave))

values_file.close()

execfile('NoteValues.py')

