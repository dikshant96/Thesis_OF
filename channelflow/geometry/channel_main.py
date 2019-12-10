from functions.fluid_basic_functions import *
from Classes.Fluid import *
import os
from functions.postprocess_OF import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

air = Fluid(1.800e-05, 1.0, 2.000e-05, 0.71)
Re = 13350
L = 2
h = L/2.
air.nu = 2e-05
Ub = get_meanvelocity(Re, air.nu, L)
I: float = 5 / 100.
k = get_turbkineticenergy(Ub, I)
epsilon = get_epsilon(k, h)
omega = get_omega(k, epsilon)
nut = get_nutkOmega(k, omega)