#!/usr/bin/env python

import sys

# sys.path += ['/home/troy/Projects/pedalsteel/pydee/pydeelib']
# import pydee

import math
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *

from Note import *
import Note as Notemodule
from Neck import *
import Chord

def nohighlight(x):
    return None

highlight = nohighlight

class NeckWidget(QtGui.QGraphicsWidget):

    Type = QtGui.QGraphicsItem.UserType + 3

    def __init__(self, x, y, xsize, ysize):
        super(NeckWidget, self).__init__()
        (self.x, self.y) = (x, y)
        (self.xsize, self.ysize) = (xsize, ysize)
        self.kneey = y + ysize + 15

        (self.lkl, self.lku, self.lkr, self.rkl, self.rkr) = \
            [x*25 for x in range(5)]

        self.nfrets = 24
        self.nstrings = 10
        self.fretlocations = [0]*(self.nfrets+1)
        self.stringlocations = [0]*self.nstrings
        self.stringboxes = [None]*self.nstrings

        ratio = 2**(1./12)
        print "ratio=%f" % ratio
        curlen = xsize
        self.fretlocations[0] = x

        for i in range(1, self.nfrets+1):
            nextfret = (curlen / ratio) + x
            curlen /= ratio
            self.fretlocations[i] = x + (xsize - curlen)

        for i in range(self.nstrings):
            v = 10+ (ysize-20) * i / (self.nstrings - 1)
            self.stringlocations[i] = v

        self.dotsize=5

        self.font = QtGui.QFont()
        self.font.setPointSize(4)
        self.fontpixels = QtGui.QFontInfo(self.font).pixelSize()
        
    def type(self):
        return NeckWidget.Type

    def boundingRect(self):
        (x,y, xsize, ysize) = (self.x, self.y, self.xsize, self.ysize)
        return QtCore.QRectF(QtCore.QPointF(x,y),
                             QtCore.QPointF(x+xsize, y+ysize))

    def paint(self, painter, option, widget):
        painter.setFont(self.font)

        painter.setPen(QtGui.QPen(QtCore.Qt.black, 1, QtCore.Qt.SolidLine,
                                  QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
        (x,y, w, h) = (self.x, self.y, self.xsize, self.ysize)

        def line(x1,y1,x2,y2):
            painter.drawLine(QLineF(QPointF(x1,y1), QPointF(x2,y2)))

        line(x,y,x+w,y)
        line(x,y,x,y+h)

        line(x+w,y+h,x+w, y)
        line(x+w,y+h,x, y+h)
        
        def makebrush(tuningdelta):
            if tuningdelta > 0:
                return QtGui.QBrush(QtGui.QColor(255, 0, 0, tuningdelta * 15))
            else:
                return QtGui.QBrush(QtGui.QColor(0, 0, 255, -1 * tuningdelta * 15))
            
        pstate = self.tuning.pedalstate()
        oldbrush = painter.brush()
        oldpen = painter.pen()
        painter.setPen(QtGui.QPen(QtGui.QColor(255,255,255,0)))
        for (index, delta) in enumerate(pstate):
            if delta:
                curbrush = makebrush(delta)
                painter.setBrush(curbrush)
                
                painter.drawRect(x, self.stringlocations[index] - self.fontpixels/2 - 4,
                                 w, 10)

        painter.setBrush(oldbrush)
        painter.setPen(oldpen)
                
        def dot(x, y, color=QtCore.Qt.red, size=3):
            # print (x,y)
            painter.setPen(QtCore.Qt.NoPen)
            painter.setBrush(color)
            painter.drawEllipse(x, y, size, size)
    
        def text(x, y, s):
            # print (x,y,s)
            global highlight
            clr = highlight(s)
            if clr:
                painter.setPen(clr)
            else:
                painter.setPen(QtCore.Qt.black)
            t = unicode(s)
            t = t.replace('s', u'\u266F')
            t = t.replace('b', u'\u266D')
            painter.drawText(x, y, t)

        prevloc = 0
        for (fretindex, loc) in enumerate(self.fretlocations):
            # line(loc, y, loc, y+ysize)
            xloc = loc - (loc - prevloc)/2
            ycenter = y+self.ysize/2
            if fretindex in [3, 5, 7, 9, 15, 17, 19, 21]:
                dot(xloc, ycenter, QtCore.Qt.blue, self.dotsize)
            if fretindex in [12,24]:
                dot(xloc, ycenter + self.dotsize, QtCore.Qt.blue, self.dotsize)
                dot(xloc, ycenter - self.dotsize, QtCore.Qt.blue, self.dotsize)
            for (stringindex, yloc) in enumerate(self.stringlocations):
                text(loc, yloc, self.tuning[stringindex][fretindex])

            prevloc = loc
                
class PedalWidget(QtGui.QGraphicsTextItem):
    def __init__(self, name):
        super(PedalWidget, self).__init__(name)
        self.on = False

    def toggle(self):
        thisfont = self.font()
        if self.on:
            thisfont.setWeight(QtGui.QFont.Normal)
        else:
            thisfont.setWeight(QtGui.QFont.Bold)
            
        self.on = not self.on

        self.setFont(thisfont)

def schlup(fname):
    def doit():
        global highlight
        execfile(fname, globals(), locals())
    return doit

def toggle_octave():
    from Note import show_octave
    show_octave[0] = not show_octave[0]
    global widget
    widget.update()
    widget.neck.update()

def setkey(key, w):
    def impl():
        def myhighlight(x):
            if x in [key, key+4, key+7, key+10]:
                return QtCore.Qt.red
            return None
        global highlight
        highlight = myhighlight
        w.tonicwidget.setPlainText(key.as_flat())
        Notemodule.tonic = [key]
        Notemodule.use_numbers()
        w.update()
    return impl

class GraphWidget(QtGui.QGraphicsView):
    def __init__(self):
        super(GraphWidget, self).__init__()

        self.timerId = 0

        self.keymap = { '1':'P1', '2':'P2', '3':'P3',
                        'y':'LKL', 'u':'LKU', 'i':'LKR',
                        'o':'RKL', 'p':'RKR'}
        
        scene = QtGui.QGraphicsScene(self)
        scene.setItemIndexMethod(QtGui.QGraphicsScene.NoIndex)
        scene.setSceneRect(-20, -50, 800, 300)

        self.setScene(scene)
        self.setCacheMode(QtGui.QGraphicsView.CacheBackground)
        self.setViewportUpdateMode(QtGui.QGraphicsView.BoundingRectViewportUpdate)
        self.setRenderHint(QtGui.QPainter.Antialiasing)
        self.setTransformationAnchor(QtGui.QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QtGui.QGraphicsView.AnchorViewCenter)

        self.neck = NeckWidget(0, 0, 1000, 150)
        self.neck.tuning = E9_Neck()

        scene.addItem(self.neck)

        self.scale(2.0, 2.0)
        self.setMinimumSize(0, 500)
        self.setWindowTitle("Pedal Steel")
        self.timerId = self.startTimer(1000)

        #
        # pedals
        # 
        spacing = 100
        pedalx = 100
        pedaly = 170

        self.pedals = {}
        pedals = self.pedals
        for name in ['LKL', 'LKU', 'LKR', 'RKL', 'RKR']:
            gi = PedalWidget(name)
            gi.setPos(pedalx, pedaly)
            pedalx += spacing
            pedals[name] = gi
            scene.addItem(gi)

        pedalx = 100
        pedaly = 185
        for name in ['P1', 'P2', 'P3']:
            gi = PedalWidget(name)
            gi.setPos(pedalx, pedaly)
            pedalx += spacing
            pedals[name] = gi
            scene.addItem(gi)

        self.tonicwidget = QtGui.QGraphicsTextItem(Notemodule.tonic[0].as_flat())
        self.tonicwidget.setPos(0,170)
        scene.addItem(self.tonicwidget)

    def wheelEvent(self, event):
        self.scaleView(math.pow(2.0, -event.delta() / 240.0))

    def scaleView(self, scaleFactor):
        factor = self.matrix().scale(scaleFactor, scaleFactor).mapRect(QtCore.QRectF(0, 0, 1, 1)).width()

        if factor < 0.07 or factor > 100:
            return

        self.scale(scaleFactor, scaleFactor)
        print "scalefactor=", scaleFactor

    def timerEvent(self, event):
        pass

    def enterEvent(self, event):
        print "enterEvent!"

    def pedtoggle(self, name):
        self.neck.tuning.toggle(name)
        self.pedals[name].toggle()


    def keyPressEvent(self, event):
        if event.isAutoRepeat():
            return
        print "keyPressEvent!", event

        fnmap = dict(#b = Notemodule.use_flats,
                     #v = Notemodule.use_sharps,
                     n = Notemodule.use_numbers,
                     x = lambda: sys.exit(1),
                     a = setkey(A, self),
                     A = setkey(As, self),
                     b = setkey(B, self),
                     c = setkey(C, self),
                     C = setkey(Cs, self),
                     d = setkey(D, self),
                     D = setkey(Ds, self),
                     e = setkey(E, self),
                     f = setkey(F, self),
                     F = setkey(Fs, self),
                     g = setkey(G, self),
                     G = setkey(Gs, self))

        fnmap['+'] = Notemodule.use_sharps
        fnmap['-'] = Notemodule.use_flats

        print fnmap
        for t in [event.text()]:
            if t in fnmap.keys():
                fnmap[str(t)]()
            if t in self.keymap.keys():
                self.pedtoggle(self.keymap[str(t)])
            
        self.neck.update()

    def keyReleaseEvent(self, event):
        pass

app = QtGui.QApplication(sys.argv)

widget = GraphWidget()
widget.show()

sys.exit(app.exec_())
