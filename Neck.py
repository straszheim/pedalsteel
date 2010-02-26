from Note import *

class E9_Neck:

    tuning = [Fs4, Ds4, Gs4, E4, B3, Gs3, Fs3, E3, D3, B2]

    nada = [0,0,0,0,0,0,0,0,0,0]
    p1   = [0,0,0,0,2,0,0,0,0,2]
    p2   = [0,0,1,0,0,1,0,0,0,0]
    p3   = [0,0,0,2,2,0,0,0,0,0]
    lkl  = [0,0,0,1,0,0,0,1,0,0]
    v    = [0,0,0,0,-1,0,0,0,0,-1]
    lkr  = [0,0,0,-1,0,0,0,-1,0,0]
    rkl  = [2,1,0,0,0,-2,0,0,0,0]
    rkr  = [0,-1,0,0,0,0,0,0,-1,0]

    def __init__(self):
        self.pedalstate = E9_Neck.nada

    def __getitem__(self, index):
        startnote = E9_Neck.tuning[index]
        return [self.tuning[index]+i for i in range(25)]
        
        
            
        
