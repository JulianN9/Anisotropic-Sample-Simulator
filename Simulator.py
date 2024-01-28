import os
import scipy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import floor, exp
# from multiprocessing import Pool
# from itertools import product, repeat, permutations, chain

# Defining Resitivities:
# c-axis resistivity
def pfactor(p):
    return (1+(p-1)/10)

def R_c(T):  # in mu-Ohm-cm (hence factor of 1000.0)
    f = 1.0/(exp((T-10.0)/10.) + 1.)
    g = 1.0/(exp((T-40.0)/20.) + 1.)
    return 1000.0*(f*(1.0+0.02*T*T) + 0.08*T*g*(1.-f) + (8.0+0.0005*T)*(1.-g)*(1.-f))

def newR_c(T,pone=1,ptwo=1,pthree=1,alpha=0,beta=0,gamma=0,Oone=0,Otwo=0,xone=0,xtwo=0,widthone=1,widthtwo=1):
    # [A,B,C,D,E,F,G,H] = [3.04684366e-17,10.6253646,37.8301757,12.6081855,8.31419655e-02,7.26861931e-17,7.49548715,1.51364092e-02]
    [A,B,C,D,E,F,G,H] = [ 10, 10, 40, 20,  0.022, 0.1, 7.5, 0.0005*30]
    f = 1.0/(np.exp((T-(A+xone))/(B*widthone)) + 1.)
    g = 1.0/(np.exp((T-(C+xtwo))/(D*widthtwo)) + 1.)
    return 1000.0*(f*(1.0+E*pow(T,2+alpha))/pone + F*(pow(T,1+beta))*g*(1.-f)/ptwo + (G+Oone+H*pow(T,1+gamma))*(1.-g)*(1.-f)/pthree+Otwo)

# def newR_c(T,pone=1,ptwo=1,pthree=1,alpha=0,beta=0,gamma=0,Oone=0,Otwo=0,xone=0,xtwo=0,widthone=1,widthtwo=1):
#     [A,B,C,D,E,F,G,H] = [ 7.17, 4.505, 25, 26.32,  0.022, 0.1, 7.5, 0.0005*30]
#     [ponep,ptwop,pthreep]=[1.05612133803642,0.0362736909584287,0.909962571848726]
#     [alphap,betap,gammap,Oonep,Otwop]=[-0.9999923091780474,-0.7267621943510602,-0.0194249762674677,0.7291489076029753,-1.469578510681581]
#     f = 1.0/(np.exp((T-(A+xone))/(B*widthone)) + 1.)
#     g = 1.0/(np.exp((T-(C+xtwo))/(D*widthtwo)) + 1.)
#     return 1000.0*(f*(1.0+E*pow(T,1+alpha))/(ponep*pone) + F*(pow(T,0.25+beta))*g*(1.-f)/(ptwo*ptwop) + (G+Oone+Oonep+H*pow(T,1+gamma))*(1.-g)*(1.-f)/(pthree*pthreep)+Otwo+Otwop)

# a-b plane resistivity
def R_ab(T): 
    f = 1.0/(exp((T-20.)/10.) + 1.0)
    return (1.7+0.03*T*T)*f + 0.68*T*(1.0-f)

# Dividing by size of lattice to get strength of resistors, 160 and 20 are arbitrary scaling factors
def rx(T,Nx):
    return 300*R_ab(T)/(Nx-1) #For summer 2023 data
    # return R_ab(T)/(Nx-1)

def ry(T,Ny):
    return 20*R_c(T)/(Ny-1) #For summer 2023 data
    # return R_c(T)/(Ny-1)

def newry(T,Ny,pone=1,ptwo=1,pthree=1,alpha=0,beta=0,gamma=0,Oone=0,Otwo=0,xone=0,xtwo=0,wone=1,wtwo=1):
    return 20*newR_c(T,pone,ptwo,pthree,alpha,beta,gamma,Oone,Otwo,xone,xtwo,wone,wtwo)/(Ny-1)

# Setting up the Inverse Connectivity Matrix
def poissonmatrix(Nx,Ny,rx,ry,plot=False):
    N = Nx*Ny
    A = np.zeros((N,N))
    gamma = 1/rx
    delta = 1/ry

    # Diagonal
    for i in range(1,Nx-1):
        A[i+Nx*(Ny-1),i+Nx*(Ny-1)]=-2*gamma-delta
        A[i,i]=-2*gamma-delta
        for j in range(1,Ny-1):
            A[i+Nx*j,i+Nx*j]=-2*gamma-2*delta
    A[Nx-1,Nx-1]=-gamma-delta
    A[0,0]=-gamma-delta
    A[Nx-1+Nx*(Ny-1),Nx-1+Nx*(Ny-1)]=-gamma-delta
    A[Nx*(Ny-1),Nx*(Ny-1)]=-gamma-delta
    for j in range(1,Ny-1):
        A[Nx-1+Nx*j,Nx-1+Nx*j]=-gamma-2*delta
        A[Nx*j,Nx*j]=-gamma-2*delta

    # Tri-Diagonal
    for i in range(0,Nx-1):
        for j in range(0,Ny):
            A[i+Nx*j+1,i+Nx*j]=gamma
            A[i+Nx*j,i+Nx*j+1]=gamma
    
    # Off-Diagonal
    for j in range(0,Ny-1):
        for i in range(0,Nx):
            A[i+Nx*j,i+Nx*(j+1)]=delta
            A[i+Nx*(j+1),i+Nx*j]=delta
    
    if plot==True:
        fig = plt.figure(figsize=(12,4))
        plt.subplot(111)
        plt.imshow(A,interpolation='none')
        clb=plt.colorbar()
        clb.set_label('Matrix elements values')
        plt.title('Matrix A ',fontsize=24)

        fig.tight_layout()
        plt.show()
    return A

# Calculating the Voltage
def voltagematrix(A,L,Nx,Ny,Vin,Vout):
    V = np.zeros(Nx*Ny)
    for count,value in enumerate(L):
        if count < floor(len(L)/2):
            V[value] = Vout
        else:
            V[value] = Vin

    b = np.matmul(A,V)
    Ar = A
    b = np.delete(b,L,0)
    Ar = np.delete(np.delete(Ar,L,0),L,1)

    Arinv = np.linalg.inv(Ar)
    Vr = np.matmul(Arinv,b)
    rcount = 0
    for i in range(Nx*Ny):
        if (not(i in L))&(not(-Nx*Ny+i in L)):
            V[i] = -Vr[i-rcount]
        else:
            rcount = rcount + 1
    return(V)

# Simulated for a given set of input/output pins
def simulate(Nx,Ny,Ix,Iy,Ox,Oy,Vin,Vout):
    data = []
    N = 100
    L = [(Ix-1)+Nx*(Iy-1),(Ox-1)+Nx*(Oy-1)]
    save = False

    for Tctr in range(0,N):
        T = 300.0-Tctr*(300.-2.)/(N-1)
        Rx = rx(T,Nx); Ry = newry(T,Ny)
        A = poissonmatrix(Nx,Ny,Rx,Ry,False)

        V = voltagematrix(A,L,Nx,Ny,Vin,Vout)

        # dQ = [ np.matmul(A,V)[i] for i in iolist[count] ]
        dQ = np.matmul(A,V)

        V = V.reshape(Ny,Nx)

        Vlist = [T,Rx,Ry,np.sum(np.abs(dQ[L]))/len(L)]
        for i in range(1,Nx+1):
            for j in range(1,Ny+1):
                Vlist.append(V[j-1,i-1])
        data.append(Vlist)
        # data[count].append(converge(V,(1/Ry)*Alist[count],iolist[count],T,Rx,Ry))

    headerlist = ['T','rx','ry','I'] # Header for the output file
    for i in range(1,Nx+1):
        for j in range(1,Ny+1):
            headerlist.append('V['+str(i)+','+str(j)+']')

    df = pd.DataFrame(data,columns=headerlist) # Making a dataframe from the data
    return df