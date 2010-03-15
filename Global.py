from pprint import pprint
class sharp: pass
class flat:  pass
class ALL:   pass

def makedict(*args):
    x = list(enumerate(args))
    y = [(a,b) for b,a in enumerate(args)]
    d = dict(x + y)
    d[ALL]=args
    return d

scaletones = {}
scaletones[sharp] = makedict('1', '1s', '2', '2s', '3', '4',
                             '4s', '5', '5s', '6', '6s', '7')
scaletones[flat] = makedict('1', '2b', '2', '3b', '3', '4', 
                            '5b', '5', '6b', '6', '7b', '7')

solfege = {}
solfege[sharp] = makedict('Do', 'Di', 'Re', 'Ri', 'Mi', 'Fa',
                          'Fi', 'So', 'Si', 'La', 'Li', 'Ti')

solfege[flat] = makedict('Do', 'Ra', 'Re', 'Ma', 'Mi', 'Fa',
                         'Se', 'So', 'Le', 'La', 'Te', 'Ti')

letternotes = {}
letternotes[sharp] = makedict('C', 'Cs', 'D', 'Ds', 'E', 'F',
                              'Fs', 'G', 'Gs', 'A', 'As', 'B')

letternotes[flat] = makedict('C', 'Db', 'D', 'Eb', 'E', 'F',
                             'Gb', 'G', 'Ab', 'A', 'Bb', 'B')


pprint(scaletones)
pprint(solfege)
pprint(letternotes)

show_octave = [False]

sharporflat = [flat]

displayer = [letternotes]

def pretty(n):
    v = n.value
    if tonic[0] != None:
        if displayer[0] == solfege:
            v -= tonic[0].value
        if displayer[0] == scaletones:
            v -= tonic[0].value
    v = v % 12
    s = displayer[0][sharporflat[0]][v]
    if n.octave and show_octave[0]:
        s += '^' + str(n.octave)
    t = unicode(s)
    t = t.replace('s', u'\u266F')
    t = t.replace('b', u'\u266D')
    return t

def letter(n):
    n.normalize()
    s = letternotes[sharporflat[0]][n.value]
    if n.octave and show_octave[0]:
        s += '^' + str(n.octave)
    # print "returning %s for %d" %( s, n.value)
    t = unicode(s)
    t = t.replace('s', u'\u266F')
    t = t.replace('b', u'\u266D')
    return t

tonic = [None]

chord = []
chordname = ''

def nohighlight(x):
    return None

highlight = nohighlight

def setdisplay(y):
    global displayer
    displayer = [y]

