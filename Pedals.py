"""
>>> P1 > P2
1
"""

class PedalMeta(type):
    def __str__(cls):
        return cls.__name__
    def __repr__(cls):
        return cls.__name__
    def __cmp__(cls, other):
        return cmp(cls.__name__, other.__name__)
    
class P1: __metaclass__ = PedalMeta
class P2: __metaclass__ = PedalMeta
class P3: __metaclass__ = PedalMeta
class P4: __metaclass__ = PedalMeta
class P5: __metaclass__ = PedalMeta
class P6: __metaclass__ = PedalMeta
class P7: __metaclass__ = PedalMeta
class P8: __metaclass__ = PedalMeta

pedal_classes = [P1, P2, P3, P4, P5, P6, P7, P8]

class LKL: __metaclass__ = PedalMeta
class LKU: __metaclass__ = PedalMeta
class LKR: __metaclass__ = PedalMeta
class RKL: __metaclass__ = PedalMeta
class RKR: __metaclass__ = PedalMeta

knee_classes = [LKL, LKU, LKR, RKL, RKR]

import itertools

pedal_combos = [(P1,),
                (P2,),
                (P3,),
                (P4,),
                (P1, P2),
                (P2, P3)]

knee_combos = [(LKL,),
               (LKR,),
               (RKL,),
               (RKR,),
               (LKL, RKL),
               (LKL, RKR),
               (LKR, RKL),
               (LKR, RKR)]

combinations = [()] + pedal_combos + knee_combos + [x+y for x in pedal_combos for y in knee_combos]





         

