import numpy as np


def est_Pw(s):



    Pw = np.zeros([4, 3])
    Pw[0,0]= -s/2
    Pw[0, 1] = -s / 2
    Pw[0, 2] = 0
    Pw[1, 0] = s / 2
    Pw[1, 1] = -s / 2
    Pw[1, 2] = 0
    Pw[2, 0] = s / 2
    Pw[2,1]= s/2
    Pw[2, 2] = 0
    Pw[3,0]= -s/2
    Pw[3,1]= s/2
    Pw[3,2]= 0
    

    return Pw
