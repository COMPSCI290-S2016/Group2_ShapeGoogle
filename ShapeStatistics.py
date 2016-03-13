import sys
sys.path.append("S3DGLPy")
from Primitives3D import *
from PolyMesh import *

import numpy as np
import scipy.io as sio

def samplePointCloud(mesh, N):
    (Ps, Ns) = mesh.randomlySamplePoints(N)
    return (Ps, Ns)

#Inputs: Ps (3 x N array of points), Ns (3 x N array of estimated normals)
def exportPointCloud(Ps, Ns, filename):
    N = Ps.shape[1]
    fout = open(filename, "w")
    fmtstr = "%g" + " %g"*5 + "\n"
    for i in range(N):
        fields = np.zeros(6)
        fields[0:3] = Ps[:, i]
        fields[3:] = Ns[:, i]
        fout.write(fmtstr%tuple(fields.flatten().tolist()))
    fout.close()


if __name__ == '__main__':
    m = PolyMesh()
    m.loadFile("models_off/biplane0.off")
    (Ps, Ns) = samplePointCloud(m, 20000)
    exportPointCloud(Ps, Ns, "test.pts")
