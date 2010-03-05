from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *

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

