
class Grip:
    """
    >>> print 'ayup doctest ok'
    ayup doctest ok
    """
    def __init__(self, pedals=[], strings=[None]*10):
        self.pedals = pedals
        self.strings = strings


    def __cmp__(self, rhs):
        pass
