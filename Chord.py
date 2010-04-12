import Interval as i

#
# generate chords and exec
#
chord_types = dict(
    n = [i.P1],

    M = [i.P1, i.M3, i.P5],
    m = [i.P1, i.m3, i.P5],
    d = [i.P1, i.m3, i.d5],

    M7 = [i.P1, i.M3, i.P5, i.M7],
    x7 = [i.P1, i.M3, i.P5, i.m7],
    m7 = [i.P1, i.m3, i.P5, i.m7],

    x7b5 =  [i.P1, i.M3, i.d5, i.m7],
    x7s5 =  [i.P1, i.M3, i.a5, i.m7],
    m7b5 =  [i.P1, i.m3, i.d5, i.m7],
    d7   =  [i.P1, i.m3, i.d5, i.d7],
    x7s9 =  [i.P1, i.M3, i.m7, i.s9],
    x7b9 =  [i.P1, i.M3, i.m7, i.m9],
    x7s9alt =  [i.M3, i.m7, i.s9]
    )

class NoteMeta(type):
    @property
    def x7bang9(self):
        return [self + x for x in x7s9alt]

    def __init__(cls, name, bases, dct):
        super(NoteMeta, cls).__init__(name, bases, dct)

        for n, v in chord_types.items():
            print n, " = ", v
            def makeprop(r):
                def propget(self):
                    print "get, v is", r
                    return [self + x for x in r]
                return property(propget)

            setattr(cls, n, makeprop(v))
