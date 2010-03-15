class PedalMeta(type):
    def __str__(cls):
        return cls.__name__
    def __repr__(cls):
        return cls.__name__


class P1: __metaclass__ = PedalMeta
class P2: __metaclass__ = PedalMeta
class P3: __metaclass__ = PedalMeta
class P4: __metaclass__ = PedalMeta
class P5: __metaclass__ = PedalMeta
class P6: __metaclass__ = PedalMeta
class P7: __metaclass__ = PedalMeta
class P8: __metaclass__ = PedalMeta

class LKL: __metaclass__ = PedalMeta
class LKU: __metaclass__ = PedalMeta
class LKR: __metaclass__ = PedalMeta
class RKL: __metaclass__ = PedalMeta
class RKR: __metaclass__ = PedalMeta

import itertools

pedals = [(P1,), (P2,), (P3,),
          (P1, P2), (P2, P3)]

knees = [(LKL,), (LKR,),
         (RKL,), (RKR,),
         (LKL, RKL), (LKL, RKR),
         (LKR, RKL), (LKR, RKR)]

combinations = [()] + pedals + knees + [x+y for x in pedals for y in knees]





         

