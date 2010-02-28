
from Note import *

class E9_Neck:


    def __init__(self):
        self.down = set([])
        self.tuning = [Fs^4, Ds^4, Gs^4, E^4, B^3, Gs^3, Fs^3, E^3, D^3, B^2]

        self.copedent = dict( nada = [0,0,0,0,0,0,0,0,0,0],
                              P1   = [0,0,0,0,2,0,0,0,0,2],
                              P2   = [0,0,1,0,0,1,0,0,0,0],
                              P3   = [0,0,0,2,2,0,0,0,0,0],
                              LKL  = [0,0,0,1,0,0,0,1,0,0],
                              LKU  = [0,0,0,0,-1,0,0,0,0,-1],
                              LKR  = [0,0,0,-1,0,0,0,-1,0,0],
                              RKL  = [2,1,0,0,0,-2,0,0,0,0],
                              RKR  = [0,-1,0,0,0,0,0,0,-1,0])

    def __getitem__(self, index):
        startnote = self.tuning[index]
        delta = sum([self.copedent[x][index] for x in self.down])
        return [self.tuning[index]+i+delta for i in range(25)]
        
    def toggle(self, pedal):

        if pedal in self.down:
            self.down.remove(pedal)
        else:
            self.down.add(pedal)
            
    def allup(self):
        self.down = set([])

    def pedalstate(self):
        state = [0]*len(self.tuning)
        for p in self.down:
            state = map(sum, zip(state, self.copedent[p]))
        return state

    
