#!/usr/bin/env python

import math
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *

from Note import *
import Note as Notemodule
from Interval import *
from Neck import *

class NeckWidget(QtGui.QGraphicsItem):

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

        ratio = 2**(1./12)
        print "ratio=%f" % ratio
        curlen = xsize
        self.fretlocations[0] = x

        for i in range(1, self.nfrets+1):
            nextfret = (curlen / ratio) + x
            curlen /= ratio
            self.fretlocations[i] = x + (xsize - curlen)

        for i in range(self.nstrings):
            self.stringlocations[i] = ysize * i / (self.nstrings - 1)

    def type(self):
        return NeckWidget.Type

    def boundingRect(self):
        (x,y, xsize, ysize) = (self.x, self.y, self.xsize, self.ysize)
        return QtCore.QRectF(QtCore.QPointF(x,y),
                             QtCore.QPointF(x+xsize, y+ysize))

    def paint(self, painter, option, widget):
        print "paint!"
        painter.setPen(QtGui.QPen(QtCore.Qt.black, 1, QtCore.Qt.SolidLine,
                QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
        (x,y, xsize, ysize) = (self.x, self.y, self.xsize, self.ysize)
        def line(x1,y1,x2,y2):
            # print (x1,y1,x2,y2)
            painter.drawLine(QLineF(QPointF(x1,y1), QPointF(x2,y2)))
            
        def dot(x, y, color=QtCore.Qt.red, size=3):
            # print (x,y)
            painter.setPen(QtCore.Qt.NoPen)
            painter.setBrush(color)
            painter.drawEllipse(x, y, size, size)
    
        def text(x, y, s):
            #print s.value
            painter.setPen(Qt.darkGray)
            t = unicode(s)
            t = t.replace('s', u'\u266F')
            t = t.replace('b', u'\u266D')
            painter.drawText(QRectF(x, y, x+20, y+20), t)

        for (fretindex, loc) in enumerate(self.fretlocations):

            # line(loc, y, loc, y+ysize)

            if fretindex in [3,5,7,9, 12, 15, 17, 19, 21, 24]:
                dot(loc, y-30, QtCore.Qt.blue, 5)
            if fretindex in [12,24]:
                dot(loc, y-40, QtCore.Qt.blue, 5)
                
            for (stringindex, yloc) in enumerate(self.stringlocations):
                dot(loc, yloc)
                text(loc, yloc, self.tuning[stringindex][fretindex])
                
class GraphWidget(QtGui.QGraphicsView):
    def __init__(self):
        super(GraphWidget, self).__init__()

        self.timerId = 0

        scene = QtGui.QGraphicsScene(self)
        scene.setItemIndexMethod(QtGui.QGraphicsScene.NoIndex)
        scene.setSceneRect(-50, -50, 1000, 250)
        self.setScene(scene)
        self.setCacheMode(QtGui.QGraphicsView.CacheBackground)
        self.setViewportUpdateMode(QtGui.QGraphicsView.BoundingRectViewportUpdate)
        self.setRenderHint(QtGui.QPainter.Antialiasing)
        self.setTransformationAnchor(QtGui.QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QtGui.QGraphicsView.AnchorViewCenter)

        self.neck = NeckWidget(0, 0, 1000, 150)
        self.neck.tuning = E9_Neck()

        scene.addItem(self.neck)

        self.scale(1.0, 1.0)
        self.setMinimumSize(0, 250)
        self.setWindowTitle("Pedal Steel")
        self.timerId = self.startTimer(1000)

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

    def keyPressEvent(self, event):
        print "keyPressEvent!",
        for t in [event.text()]:
            if t == 'q':
                sys.exit(1)
            if t == 'b':
                Notemodule.use_flats()
                break
            if t == 's':
                Notemodule.use_sharps()
                break
            
    def keyReleaseEvent(self, event):
        print "keyReleaseEvent!"

if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    # QtCore.qsrand(QtCore.QTime(0,0,0).secsTo(QtCore.QTime.currentTime()))

    widget = GraphWidget()
    widget.show()

    sys.exit(app.exec_())
