
class Grip:
    """
    >>> print 'ayup doctest ok'
    ayup doctest ok
    """
    def __init__(self, pedals=[], strings=[0]*10, neck=None):
        self.pedals = set(pedals)
        self.strings = strings
        self.neck = neck
        print "Grip:", self.pedals, self.strings
        
    def __eq__(self, rhs):
        return self.pedals == rhs.pedals and self.strings == rhs.strings

    def normalize(self):
        assert len(self.neck.tuning) == len(self.strings), \
               "%d strings in tuning, %d in grip" % (len(self.neck.tuning), len(self.strings))
        newgrip = Grip(self.pedals, self.strings)
        for pedal in self.pedals:
            useless = True
            for p, s in zip(self.neck.copedent[pedal], self.strings):
                if s and (p != 0):
                    useless = False
            if useless:
                newgrip.pedals.discard(pedal)
        return newgrip
    
    def superset_of(self, rhs):
        print "superset %s <=> %s" % (self, rhs),
        ss = False
        for mine, theirs in zip(self.strings, rhs.strings):
            if mine == 1 and theirs == 0:
                ss = True
            if mine == 0 and theirs == 1:
                return False
        return ss
    
    def __str__(self):
        return str(self.pedals) + " " + str(self.strings)

    def __repr__(self):
        return repr(self.pedals) + " " + repr(self.strings)
