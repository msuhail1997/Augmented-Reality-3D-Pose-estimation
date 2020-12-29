import numpy as np
from est_homography import est_homography
from est_Pw import est_Pw
from numpy.linalg import inv


def PnP(Pc, Pw, K):

    Pw = np.delete(Pw, -1, axis=1)
    H=est_homography(Pw,Pc)
    R = np.eye(3)
    t = np.zeros([3])
    K= inv(K)
    h=np.matmul(K,H)
    t=h[:,2]/np.linalg.norm(h[:,0])
    h = np.delete(h, -1, axis=1)
    h1=h[:,[0]]
    h2=h[:,[1]]
    h1=h1.transpose()
    h2=h2.transpose()
    y=np.cross(h1,h2)
    y=y.transpose()
    h=np.append(h, y, axis=1)
    U, S, V = np.linalg.svd(h)
    I=np.identity(3)
    final=np.matmul(U,V)
    I[2,2]=np.linalg.det(final)
    R=np.matmul(U,np.matmul(I,V))
    R=R.transpose()
    t=np.matmul(-R,t)



    return R, t
