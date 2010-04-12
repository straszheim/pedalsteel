import Interval as i

#
# generate chords and exec
#

n = [i.P1]

M = [i.P1, i.M3, i.P5]
m = [i.P1, i.m3, i.P5]
d = [i.P1, i.m3, i.d5]

M7 = M + [i.M7]
x7 = M + [i.m7]
m7 = m + [i.m7]

x7b5 =  [i.P1, i.M3, i.d5, i.m7]
x7s5 =  [i.P1, i.M3, i.a5, i.m7]
m7b5 =  d + [i.m7]
d7   =  d + [i.d7]
x7s9 =  [i.P1, i.M3, i.m7, i.s9]
x7b9 =  [i.P1, i.M3, i.m7, i.m9]
x7s9alt =  [i.M3, i.m7, i.s9]

chord_types = {
    'n' : n,
    'M' : M,
    'm' : m,
    'M7' : M7,
    'x7' : x7,
    'm7' : m7,
    'x7b5' : x7b5,
    'x7+5' : x7s5,
    'm7b5' : m7b5,
    'd7' : d7,
    'x7+9' : x7s9,
    'x7b9' : x7b9
    'x7s9alt' : x7s9alt
    }



