import numpy as np

def get_geompoints():
    A = 0.1 / 2
    x = np.linspace(0, 1, 1000)
    y = np.array([A * np.cos(2 * np.pi * xi) for xi in x])
    return x, y

def get_3dgeompoints():
    x, y = get_geompoints()
    coords = np.zeros((len(x),3))
    for i in range(len(x)):
        coords[i, 0] = x[i]
        coords[i, 1] = y[i]
    return coords