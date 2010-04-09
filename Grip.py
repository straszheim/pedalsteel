
class Grip:
    """
    >>> print 'ayup doctest ok'
    ayup doctest ok
    """
    def __init__(self, pedals=[], strings=[None]*10):
        self.pedals = set(pedals)
        self.strings = strings

    def __cmp__(self, rhs):
        c = cmp(self.pedals, rhs.pedals)
        if c != 0:
            return c
        return cmp(self.strings, rhs.strings)

    def superset(self, rhs):
        print "superset %s <=> %s" % (self, rhs),
        for mine, theirs in zip(self.pedals, rhs.pedals):
            if mine == None and theirs != None:
                print "NO"
                return False
        print "YES"
        return True
    
    def __str__(self):
        return str(self.pedals) + " " + str(self.strings)

    def __repr__(self):
        return repr(self.pedals) + " " + repr(self.strings)
