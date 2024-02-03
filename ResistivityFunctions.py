import numpy as np
import matplotlib.pyplot as plt
from math import exp

def poly(T,a,b,c=0):
    return a*np.power(T,b)+c

def boltz(T,A,B,check=True):
    if check:
        return 1.0/(np.exp((T-A)/B) + 1.)
    else:
        return 1

# Defaults: P = [[]]
def userfunction(T,p1a,p1b,p1c,p2a,p2b,p2c,p3a,p3b,p3c,p4a,p4b,p4c,p5a,p5b,p5c,b1a,b1b,b1c,b2a,b2b,b2c,b3a,b3b,b3c,b4a,b4b,b4c):
    p1 = [p1a,p1b,p1c]; p2 = [p2a,p2b,p2c]; p3 = [p3a,p3b,p3c]; p4 = [p4a,p4b,p4c]; p5 = [p5a,p5b,p5c]
    b1 = [b1a,b1b]; b2 = [b2a,b2b]; b3 = [b3a,b3b]; b4 = [b4a,b4b]
    P1 = poly(T,*p1); P2 = poly(T,*p2); P3 = poly(T,*p3); P4 = poly(T,*p4); P5 = poly(T,*p5)
    B1 = boltz(T,*b1,b1c); B2 = boltz(T,*b2,b2c); B3 = boltz(T,*b3,b3c); B4 = boltz(T,*b4,b4c); 
    uf = P1*B1 + (1-B1)*P2*B2 + (1-B2)*P3*B3 + (1-B3)*P4*B4 + (1-B4)*P5
    return uf

def R_c(T):  # in mu-Ohm-cm (hence factor of 1000.0)
    f = 1.0/(np.exp((T-10.0)/10.) + 1.)
    g = 1.0/(np.exp((T-40.0)/20.) + 1.)
    return 1000.0*(f*(1.0+0.022*T*T) + 0.1*T*g*(1.-f) + (7.5+0.0005*30*T)*(1.-g)*(1.-f))

# a-b plane resistivity
def R_ab(T): 
    f = 1.0/(np.exp((T-20.)/10.) + 1.0)
    return (1.7+0.03*T*T)*f + 0.68*T*(1.0-f)

if __name__ == "__main__":
    T = np.linspace(4,300,100)
    p1 = [0.022,2,1]; p2 = [0.1,1,0]; p3 = [30*0.0005,1,7.5]; p4 = [0,0,0]; p5 = [0,0,0]
    b1 = [10,10]; b2 = [40,20]; b3 = [1,1]; b4 = [1,1]

    plt.plot(T,userfunction(T,*p1,*p2,*p3,*p4,*p5,*b1,*b2,*b3,*b4,0,True,True),c='blue')
    plt.plot(T,R_c(T)/1000, c='black')
    plt.show()