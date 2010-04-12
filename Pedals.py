"""
>>> P1 < P2
True
>>> P1 > P2
False
>>> cmp(P1, P2)
-1
>>> cmp(P2, P1)
1
>>> cmp(P1, P1)
0
"""

class PedalMeta(type):
    def __str__(cls):
        return cls.__name__
    def __repr__(cls):
        return cls.__name__
    def __cmp__(cls, other):
        if other == None:
            return -1
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

class LL: __metaclass__ = PedalMeta
class LU: __metaclass__ = PedalMeta
class LR: __metaclass__ = PedalMeta
class RL: __metaclass__ = PedalMeta
class RR: __metaclass__ = PedalMeta

knee_classes = [LL, LU, LR, RL, RR]

import itertools

pedal_combos = [(P1,),
                (P2,),
                (P3,),
                (P4,),
                (P1, P2),
                (P2, P3)]

knee_combos = [(LL,),
               (LR,),
               (RL,),
               (RR,),
               (LL, RL),
               (LL, RR),
               (LR, RL),
               (LR, RR)]

combinations = [()] + pedal_combos + knee_combos + [x+y for x in pedal_combos for y in knee_combos]

# FIXME: remove incompatible pedal/knee combinations, some overlap



         

