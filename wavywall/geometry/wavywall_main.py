import numpy as np
import matplotlib.pyplot as plt
from wavywall_functions import *

x, y = get_geompoints()
coords = get_3dgeompoints()

for i in range(1, len(x)):
    print(x[i], "Vertex_{0}".format(i))