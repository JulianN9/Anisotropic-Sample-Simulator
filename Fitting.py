import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from scipy import interpolate
from ResistivityFunctions import userfunction
from Simulator3d import simulate

def rho(T,Nlist,Ilist,Olist,VIO,IPx,IPy,IPz,OPx,OPy,OPz,Rx,Ry,Rz,P1a,P1b,P1c,P2a,P2b,P2c,P3a,P3b,P3c,P4a,P4b,P4c,P5a,P5b,P5c,B1a,B1b,B1c,B2a,B2b,B2c,B3a,B3b,B3c,B4a,B4b,B4c,mode=0):
    if mode == 1:
        Rx = userfunction(T,[P1a,P1b,P1c],[P2a,P2b,P2c],[P3a,P3b,P3c],[P4a,P4b,P4c],[P5a,P5b,P5c],[B1a,B1b,B1c],[B2a,B2b,B2c],[B3a,B3b,B3c],[B4a,B4b,B4c])
    elif mode == 2:
        Ry = userfunction(T,[P1a,P1b,P1c],[P2a,P2b,P2c],[P3a,P3b,P3c],[P4a,P4b,P4c],[P5a,P5b,P5c],[B1a,B1b,B1c],[B2a,B2b,B2c],[B3a,B3b,B3c],[B4a,B4b,B4c])
    elif mode == 3:
        Rz = userfunction(T,[P1a,P1b,P1c],[P2a,P2b,P2c],[P3a,P3b,P3c],[P4a,P4b,P4c],[P5a,P5b,P5c],[B1a,B1b,B1c],[B2a,B2b,B2c],[B3a,B3b,B3c],[B4a,B4b,B4c])
    Rlist = [Rx,Ry,Rz]

    df = simulate(Nlist,Ilist,Olist,VIO,T,Rlist)

    inputpin = "V["+str(IPx)+","+str(IPy)+","+str(IPz)+"]" 
    outputpin = "V["+str(OPx)+","+str(OPy)+","+str(OPz)+"]"

    Rsim = (df[outputpin]-df[inputpin])/df["I"]

    return Rsim/max(Rsim)

def fitR(Rdata,Tdata,T,Nlist,Ilist,Olist,VIO,Rx,Ry,Rz,IPlist,OPlist,RP,RB,mode):
    [IPx,IPy,IPz] = IPlist[0]; [OPx,OPy,OPz] = OPlist[0]
    Rdata = Rdata/max(Rdata)

    Rinterp = interpolate.interp1d(Tdata,Rdata)(T)
    count = 1

    if mode>0:
        [[P1a,P1b,P1c],[P2a,P2b,P2c],[P3a,P3b,P3c],[P4a,P4b,P4c],[P5a,P5b,P5c]] = RP
        [[B1a,B1b,B1c],[B2a,B2b,B2c],[B3a,B3b,B3c],[B4a,B4b,B4c]] = RB

        RPLBounds = [0.0001,0,-50]; RPUBounds = [1,5,50]
        RBLBounds = [0.001,0.001]; RBUBounds = [300,1000]
        TRPLBounds = []; TRPUBounds = []
        TRBLBounds = []; TRBUBounds = []
        GuessP = RP[0]; GuessB = []

        TRPLBounds += RPLBounds; TRPUBounds += RPUBounds
        for index, RBx in enumerate(RB):
            if RBx[2]:
                count += 1
                GuessP += RP[index+1]; GuessB += RB[index][0:2]
                TRPLBounds += RPLBounds; TRPUBounds += RPUBounds
                TRBLBounds += RBLBounds; TRBUBounds += RBUBounds
        Bounds = [TRPLBounds+TRBLBounds,TRPUBounds+TRBUBounds]
        Guess = GuessP+GuessB
        if count == 5:
            params, cov = curve_fit(lambda T, P1a,P1b,P1c,P2a,P2b,P2c,P3a,P3b,P3c,P4a,P4b,P4c,P5a,P5b,P5c, B1a,B1b,B2a,B2b,B3a,B3b,B4a,B4b: rho(T,Nlist,Ilist,Olist,VIO,IPx,IPy,IPz,OPx,OPy,OPz,Rx,Ry,Rz,P1a,P1b,P1c,P2a,P2b,P2c,P3a,P3b,P3c,P4a,P4b,P4c,P5a,P5b,P5c,B1a,B1b,B1c,B2a,B2b,B2c,B3a,B3b,B3c,B4a,B4b,B4c,mode), T, Rinterp, p0=Guess, bounds=Bounds, sigma=0.001*np.ones_like(T))
            P1a,P1b,P1c,P2a,P2b,P2c,P3a,P3b,P3c,P4a,P4b,P4c,P5a,P5b,P5c, B1a,B1b,B2a,B2b,B3a,B3b,B4a,B4b = params
        elif count == 4:
            params, cov = curve_fit(lambda T, P1a,P1b,P1c,P2a,P2b,P2c,P3a,P3b,P3c,P4a,P4b,P4c, B1a,B1b,B2a,B2b,B3a,B3b: rho(T,Nlist,Ilist,Olist,VIO,IPx,IPy,IPz,OPx,OPy,OPz,Rx,Ry,Rz,P1a,P1b,P1c,P2a,P2b,P2c,P3a,P3b,P3c,P4a,P4b,P4c,P5a,P5b,P5c,B1a,B1b,B1c,B2a,B2b,B2c,B3a,B3b,B3c,B4a,B4b,B4c,mode), T, Rinterp, p0=Guess, bounds=Bounds, sigma=0.001*np.ones_like(T))
            P1a,P1b,P1c,P2a,P2b,P2c,P3a,P3b,P3c,P4a,P4b,P4c, B1a,B1b,B2a,B2b,B3a,B3b = params
        elif count == 3:
            params, cov = curve_fit(lambda T, P1a,P1b,P1c,P2a,P2b,P2c,P3a,P3b,P3c, B1a,B1b,B2a,B2b: rho(T,Nlist,Ilist,Olist,VIO,IPx,IPy,IPz,OPx,OPy,OPz,Rx,Ry,Rz,P1a,P1b,P1c,P2a,P2b,P2c,P3a,P3b,P3c,P4a,P4b,P4c,P5a,P5b,P5c,B1a,B1b,B1c,B2a,B2b,B2c,B3a,B3b,B3c,B4a,B4b,B4c,mode), T, Rinterp, p0=Guess, bounds=Bounds, sigma=0.001*np.ones_like(T))
            P1a,P1b,P1c,P2a,P2b,P2c,P3a,P3b,P3c, B1a,B1b,B2a,B2b = params
        elif count == 2:
            params, cov = curve_fit(lambda T, P1a,P1b,P1c,P2a,P2b,P2c, B1a,B1b: rho(T,Nlist,Ilist,Olist,VIO,IPx,IPy,IPz,OPx,OPy,OPz,Rx,Ry,Rz,P1a,P1b,P1c,P2a,P2b,P2c,P3a,P3b,P3c,P4a,P4b,P4c,P5a,P5b,P5c,B1a,B1b,B1c,B2a,B2b,B2c,B3a,B3b,B3c,B4a,B4b,B4c,mode), T, Rinterp, p0=Guess, bounds=Bounds, sigma=0.001*np.ones_like(T))
            P1a,P1b,P1c,P2a,P2b,P2c, B1a,B1b = params
        else:
            params, cov = curve_fit(lambda T, P1a,P1b,P1c: rho(T,Nlist,Ilist,Olist,VIO,IPx,IPy,IPz,OPx,OPy,OPz,Rx,Ry,Rz,P1a,P1b,P1c,P2a,P2b,P2c,P3a,P3b,P3c,P4a,P4b,P4c,P5a,P5b,P5c,B1a,B1b,B1c,B2a,B2b,B2c,B3a,B3b,B3c,B4a,B4b,B4c,mode), T, Rinterp, p0=Guess, bounds=Bounds, sigma=0.001*np.ones_like(T))
            P1a,P1b,P1c = params

    else:
        Bounds = [[1,1,1,1,1,1],Nlist+Nlist]
        Guess = IPlist[0]+OPlist[0]
        params, cov = curve_fit(lambda T, IPx,IPy,IPz,OPx,OPy,OPz: rho(T,Nlist,Ilist,Olist,VIO,IPx,IPy,IPz,OPx,OPy,OPz,Rx,Ry,Rz,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,mode), T, Rinterp, p0=Guess, bounds=Bounds)

    Rfit = rho(T,Nlist,Ilist,Olist,VIO,IPx,IPy,IPz,OPx,OPy,OPz,Rx,Ry,Rz,P1a,P1b,P1c,P2a,P2b,P2c,P3a,P3b,P3c,P4a,P4b,P4c,P5a,P5b,P5c,B1a,B1b,B1c,B2a,B2b,B2c,B3a,B3b,B3c,B4a,B4b,B4c,mode)

    return list(params)+[1], count, Rfit