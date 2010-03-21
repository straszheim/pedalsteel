#!/usr/bin/env python

import pdb
import sys
reload(sys)
print sys.setdefaultencoding('UTF-8')

# sys.path += ['/home/troy/Projects/pedalsteel/pydee/pydeelib']
# import pydee

import math
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *

import Global as g
from Note import *
import Note as Notemodule
from Neck import *
import Chord
from NeckWidget import NeckWidget
from PedalWidget import PedalWidget
from Pedals import *

def toggle_octave():
    from Note import show_octave
    show_octave[0] = not show_octave[0]
    global widget
    widget.update()
    widget.neck.update()


def setkey(key, w):
    def impl():
        g.tonic[0] = key
        def myhighlight(x):
            if x in g.chord:
                return QtCore.Qt.red
            return None
        g.highlight = myhighlight
        w.tonicwidget.setPlainText(g.letter(key) + g.chordname)
        w.update()
    return impl

def setchordtype(type, w):
    def impl():
        g.chordname = type
        g.chord=[g.tonic[0] + x for x in Chord.chord_types[type]]
        w.tonicwidget.setPlainText(g.letter(g.tonic[0]) + type)
    return impl

class GraphWidget(QtGui.QGraphicsView):
    def __init__(self):
        super(GraphWidget, self).__init__()

        self.timerId = 0

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
        self.neck.tuning = NeckModel(E9)

        scene.addItem(self.neck)

        self.scale(2.0, 2.0)
        self.setMinimumSize(0, 500)
        self.setWindowTitle("Pedal Steel")
        self.timerId = self.startTimer(1000)

        #
        # pedals
        # 
        spacing = 50
        pedalx = 200
        pedaly = 170

        self.pedals = {}
        pedals = self.pedals
        for k in knee_classes:
            name = str(k)
            gi = PedalWidget(name)
            gi.setPos(pedalx, pedaly)
            pedalx += spacing
            pedals[k] = gi
            scene.addItem(gi)

        pedalx = 200
        pedaly = 185
        for p in pedal_classes:
            name = str(p)
            gi = PedalWidget(name)
            gi.setPos(pedalx, pedaly)
            pedalx += spacing
            pedals[p] = gi
            scene.addItem(gi)

        g.tonic = [C]
        self.tonicwidget = QtGui.QGraphicsTextItem(g.letter(g.tonic[0]) + g.chordname)
        self.tonicwidget.setPos(0,170)
        font = self.tonicwidget.font()
        font.setPointSize(30)
        self.tonicwidget.setFont(font)
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

        def setdtype(y):
            def impl():
                print "setting displayer to", [y]
                g.displayer = [y]
            return impl
        

        fnmap = { '!' : lambda: sys.exit(1),
                  'a' : setkey(A, self),
                  'A' : setkey(As, self),
                  'b' : setkey(B, self),
                  'c' : setkey(C, self),
                  'C' : setkey(Cs, self),
                  'd' : setkey(D, self),
                  'D' : setkey(Ds, self),
                  'e' : setkey(E, self),
                  'f' : setkey(F, self),
                  'F' : setkey(Fs, self),
                  'g' : setkey(G, self),
                  'G' : setkey(Gs, self),
                  's' : setdtype(g.solfege),
                  'l' : setdtype(g.letternotes),
                  't' : setdtype(g.scaletones),
                  'm' : setchordtype('m', self),
                  'M' : setchordtype('M', self),
                  'n' : setchordtype('m7', self),
                  'N' : setchordtype('M7', self),
                  'x' : setchordtype('x7', self),
                  #'c' : setchordtype('x7b5', self),
                  'j' : setchordtype('m7b5', self),
                  'J' : setchordtype('d7', self),
                  'X' : setchordtype('x7+5', self),
                  #'C' : setchordtype('x7+9', self),
                  }

        def setglobal(y):
            def impl():
                g.sharporflat = [y]
                self.tonicwidget.setPlainText(g.letter(g.tonic[0]) + g.chordname)
                
            return impl
        
        fnmap['+'] = setglobal(g.sharp) 
        fnmap['-'] = setglobal(g.flat) 

        setkey(g.tonic[0], self)

        print fnmap

        self.keymap = { '1': P1, '2': P2, '3': P3,
                        '4': P4, '5': P5, '6': P6,
                        '7': P7, '8': P8,
                        'y': LKL, 'u': LKU, 'i': LKR,
                        'o': RKL, 'p': RKR}

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
