from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
import Global as g

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

        ratio = 2**(1.0/16)
        print "ratio=%f" % ratio
        curlen = xsize * 1.5
        self.fretlocations[0] = x

        for i in range(1, self.nfrets+1):
            nextfret = (curlen / ratio) + x
            curlen /= ratio
            self.fretlocations[i] = x + ((xsize * 1.5) - curlen)

        for i in range(self.nstrings):
            v = 10 + (ysize-20) * i / (self.nstrings - 1)
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
                
                painter.drawRect(x, self.stringlocations[(self.nstrings-1)-index] - self.fontpixels/2 - 4,
                                 w, 10)

        painter.setBrush(oldbrush)
        painter.setPen(oldpen)
                
        def dot(x, y, color=QtCore.Qt.red, size=3):
            # print (x,y)
            painter.setPen(QtCore.Qt.NoPen)
            painter.setBrush(color)
            painter.drawEllipse(x, y, size, size)
    
        def text(x, y, s):
            clr = g.highlight(s)
            if clr:
                painter.setPen(clr)
            else:
                painter.setPen(QtCore.Qt.black)
            painter.drawText(x, y, unicode(g.pretty(s)))

        #
        #  Fretboard dots
        #
        prevloc = 0
        for (fretindex, loc) in enumerate(self.fretlocations):
            xloc = loc - (loc - prevloc)/2
            ycenter = (self.stringlocations[0] + self.stringlocations[-1]) / 2 -4
            if fretindex in [3, 5, 7, 9, 15, 17, 19, 21]:
                dot(xloc, ycenter, QtCore.Qt.blue, self.dotsize)
            if fretindex in [12,24]:
                dot(xloc, ycenter + self.dotsize, QtCore.Qt.blue, self.dotsize)
                dot(xloc, ycenter - self.dotsize, QtCore.Qt.blue, self.dotsize)
            for (stringindex, yloc) in enumerate(self.stringlocations):
                text(loc, yloc, self.tuning[9-stringindex][fretindex])

            prevloc = loc
