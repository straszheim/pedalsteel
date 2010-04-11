
from copy import deepcopy
from Note import *
from Pedals import *

nada = [0, 0, 0, 0, 0,  0, 0, 0, 0, 0]

class NeckModel:

    def __init__(self, model):
        self.down = set([])
        self.tuning = model.tuning[:]
        self.copedent = deepcopy(model.copedent)

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

class E9:
    tuning = [B^2, D^3, E^3,  Fs^3, Gs^3,
              B^3, E^4, Gs^4, Ds^4, Fs^4]
    
    copedent = { P1   : [+2, 0, 0, 0, 0, +2, 0, 0, 0, 0], 
                 P2   : [ 0, 0, 0, 0,+1,  0, 0,+1, 0, 0], 
                 P3   : [ 0, 0, 0, 0, 0, +2,+2, 0, 0, 0], 
                 P4   : [ 0, 0, 0, 0,-2, -2, 0, 0, 0, 0],
                 P5   : nada,
                 P6   : nada,
                 P7   : nada,
                 P8   : nada,

                 LKL  : [ 0, 0,+1, 0, 0,  0,+1, 0, 0, 0], 
                 LKU  : [-1, 0, 0, 0, 0, -1, 0, 0, 0, 0], 
                 LKR  : [ 0, 0,-1, 0, 0,  0,-1, 0, 0, 0], 
                 RKL  : [ 0, 0, 0,+2, 0,  0, 0, 0, 0,+2], 
                 RKR  : [ 0, 0, 0, 0, 0,  0, 0, 0,-2, 0]}


class E9_minor:
    tuning = [B^2, D^3,  E^3,  Fs^3, G^3,
              B^3, E^4,  G^4,  Ds^4, Fs^4]

    copedent = dict(P1   = [+1, 0, 0, 0, 0, +1, 0, 0, 0, 0], 
                    P2   = [ 0, 0, 0, 0,+2,  0, 0,+2, 0, 0], 
                    P3   = [ 0, 0, 0, 0, 0, +1,+2, 0, 0, 0], 
                    P4   = [ 0, 0, 0, 0,-2, -2, 0, 0, 0, 0], 
                    P5   = nada,
                    P6   = nada,
                    P7   = nada,
                    P8   = nada,

                    LKL  = [ 0, 0,+1, 0, 0,  0,+1, 0, 0, 0], 
                    LKU  = [-1, 0, 0, 0, 0, -1, 0, 0, 0, 0], 
                    LKR  = [ 0, 0,-1, 0, 0,  0,-1, 0, 0, 0], 
                    RKL  = [ 0, 0, 0, 0,-1,  0, 0, 0,+1,+2], 
                    RKR  = [ 0,-2, 0, 0, 0,  0, 0, 0,-1, 0])

class C6:
    tuning = [C^2,  F^2,  A^3,  C^3,  E^3,
              G^3,  A^4,  C^4,  E^4,  D^4]

    copedent = { P1 :  nada,
                 P2 :  nada,
                 P3 :  nada,
                 P4 :  [ 0, 0,+2, 0, 0,  0,+2, 0, 0, 0], 
                 P5 :  [ 0, 0, 0, 0, 0, -1, 0, 0, 0, 0],
                 P6 :  [ 0, 0, 0, 0,+1,  0, 0, 0,+1, 0],
                 P7 :  [ 0, 0, 0, 0,+2, +2, 0, 0, 0, 0],
                 P8 :  [-3,-1, 0,+1, 0,  0, 0, 0, 0, 0],
                                    
                 LKL : [ 0, 0, 0, 0, 0,  0, 0, 0, 0, 0], 
                 LKU : [ 0, 0, 0, 0, 0,  0, 0, 0, 0, 0], 
                 LKR : [ 0, 0, 0, 0, 0,  0, 0, 0, 0, 0], 
                 RKL : [ 0, 0, 0, 0, 0,  0, 0,-1, 0, 0], 
                 RKR : [ 0, 0, 0, 0, 0,  0, 0, 0, 0, 0] }


        
