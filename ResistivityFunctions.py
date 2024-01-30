import numpy as np
from math import exp

def R_c(T):  # in mu-Ohm-cm (hence factor of 1000.0)
    f = 1.0/(exp((T-10.0)/10.) + 1.)
    g = 1.0/(exp((T-40.0)/20.) + 1.)
    return 1000.0*(f*(1.0+0.022*T*T) + 0.1*T*g*(1.-f) + (7.5+0.0005*30*T)*(1.-g)*(1.-f))

# a-b plane resistivity
def R_ab(T): 
    f = 1.0/(exp((T-20.)/10.) + 1.0)
    return (1.7+0.03*T*T)*f + 0.68*T*(1.0-f)