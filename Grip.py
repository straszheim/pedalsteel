import Global as g
class Grip:
    """
    >>> print 'ayup doctest ok'
    ayup doctest ok
    """
    def __init__(self, pedals=[], strings=[0]*10, neck=None, tonicstring=0):
        self.pedals = set(pedals)
        self.strings = strings
        self.neck = neck
        self.tonicstring = tonicstring
        print "Grip:", self.pedals, self.strings
        
    def __eq__(self, rhs):
        return self.pedals == rhs.pedals and self.strings == rhs.strings

    def normalize(self):
        assert len(self.neck.tuning) == len(self.strings), \
               "%d strings in tuning, %d in grip" % (len(self.neck.tuning), len(self.strings))
        newgrip = Grip(self.pedals, self.strings, self.neck, self.tonicstring)
        for pedal in self.pedals:
            useless = True
            for p, s in zip(self.neck.copedent[pedal], self.strings):
                if s and (p != 0):
                    useless = False
            if useless:
                newgrip.pedals.discard(pedal)
        return newgrip
    
    def superset_of(self, rhs):
        ss = False
        if self.pedals != rhs.pedals:
            return False
        for mine, theirs in zip(self.strings, rhs.strings):
            if mine == 1 and theirs == 0:
                ss = True
            if mine == 0 and theirs == 1:
                return False
        return ss
    
    def __str__(self):

        self.neck.allup()
        pedline = ['  '] * 10
        for p in self.pedals:
            self.neck.toggle(p)
            for i in range(10):
                if self.neck.copedent[p][i] != 0 and pedline[i] != None:
                    pedline[i] = "%-2s" % p

        g.tonic[0] = self.neck[self.tonicstring][0]
        sr = ''

        printy = []
        for j, s in enumerate(self.strings):
            if s == 0:
                printy += ['. ']
            else:
                printy += ["%-2s" % g.pretty(self.neck[j][0])]

        sr += ' '.join(pedline) + '\n'
        sr += ' '.join([x.encode('UTF-8') for x in printy])
        return sr

    def __repr__(self):
        return repr(self.pedals) + " " + repr(self.strings)

