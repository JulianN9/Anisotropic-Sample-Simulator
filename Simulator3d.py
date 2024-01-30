import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import floor
from ResistivityFunctions import R_c, R_ab

# Dividing by size of lattice to get strength of resistors, 160 and 20 are arbitrary scaling factors
def rx(T,Nx):
    Nx = max(2,Nx)
    return 300*R_ab(T)/(Nx-1) #For summer 2023 data
    # return R_ab(T)/(Nx-1)

def ry(T,Ny):
    Ny = max(2,Ny)
    return 20*R_c(T)/(Ny-1) #For summer 2023 data
    # return R_c(T)/(Ny-1)

# Setting up the Inverse Connectivity Matrix
def poissonmatrix(Nx,Ny,Nz,rx,ry,rz,plot=False):
    N = Nx*Ny*Nz
    A = np.zeros((N,N))
    Ly = Nx
    Lz = Nx*Ny
    gamma = min(1,Nx-1) * (1/rx)
    delta = min(1,Nx-1) * (1/ry)
    eta = min(1,Nz-1) * (1/rz)

    # Diagonal
    for i in range(N):
        A[i,i] += - gamma - delta - eta
    for i in range(Nx):
        for j in range(Ny):
            for k in range(Nz):
                if i in range(0,Nx-1):
                    if i>0:
                        # Diagonal 
                        A[i+j*Ly+k*Lz,i+j*Ly+k*Lz] += -gamma
                    # Off-Diagonal
                    A[(i+1)+Ly*j+Lz*k,i+Ly*j+Lz*k] += gamma
                    A[i+Ly*j+Lz*k,(i+1)+Nx*j+Lz*k] += gamma
                if j in range(0,Ny-1):
                    if j>0:
                        # Diagonal
                        A[i+j*Ly+k*Lz,i+j*Ly+k*Lz] += -delta
                    # Off-Diagonal
                    A[i+Ly*(j+1)+Lz*k,i+Ly*j+Lz*k] += delta
                    A[i+Ly*j+Lz*k,i+Nx*(j+1)+Lz*k] += delta
                if k in range(0,Nz-1):
                    if k>0:
                        # Diagonal
                        A[i+j*Ly+k*Lz,i+j*Ly+k*Lz] += -eta
                    # Off-Diagonal
                    A[i+Ly*j+Lz*(k+1),i+Ly*j+Lz*k] += eta
                    A[i+Ly*j+Lz*k,i+Nx*j+Lz*(k+1)] += eta
    
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
def voltagematrix(A,L,Nx,Ny,Nz,Vin,Vout,plot=False):
    V = np.zeros(Nx*Ny*Nz)
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
    for i in range(Nx*Ny*Nz):
        if (not(i in L))&(not(-Nx*Ny*Nz+i in L)):
            V[i] = -Vr[i-rcount]
        else:
            rcount = rcount + 1

    if plot==True:
        fig = plt.figure(figsize=(12,4))
        plt.subplot(111)
        plt.imshow(V.reshape(Nz,Ny,Nx)[1],interpolation='none')
        clb=plt.colorbar()
        clb.set_label('Matrix elements values')
        plt.title('Matrix A ',fontsize=24)

        fig.tight_layout()
        plt.show()
    return(V)

# Simulated for a given set of input/output pins
def simulate(Nx,Ny,Nz,Ilist,Olist,Vin,Vout,Tlist):
    data = []
    AL = np.array([1,Nx,Nx*Ny])
    L = [np.dot(np.array(p)-1,AL) for p in Ilist+Olist]
    save = False

    for T in Tlist:
        Rx = rx(T,Nx); Ry = ry(T,Ny); Rz = rx(T,Nz)
        A = poissonmatrix(Nx,Ny,Nz,Rx,Ry,Rz,False)

        V = voltagematrix(A,L,Nx,Ny,Nz,Vin,Vout)

        # dQ = [ np.matmul(A,V)[i] for i in iolist[count] ]
        dQ = np.matmul(A,V)

        V = V.reshape(Nz,Ny,Nx)

        Vlist = [T,Rx,Ry,Rz,np.sum(np.abs(dQ[L]))/len(L)]
        for i in range(1,Nx+1):
            for j in range(1,Ny+1):
                for k in range(1,Nz+1):
                    Vlist.append(V[k-1,j-1,i-1])
        data.append(Vlist)
        # data[count].append(converge(V,(1/Ry)*Alist[count],iolist[count],T,Rx,Ry))

    headerlist = ['T','rx','ry','rz','I'] # Header for the output file
    for i in range(1,Nx+1):
        for j in range(1,Ny+1):
            for k in range(1,Nz+1):
                headerlist.append('V['+str(i)+','+str(j)+','+str(k)+']')

    df = pd.DataFrame(data,columns=headerlist) # Making a dataframe from the data
    return df

if __name__ == "__main__":
    T = 300; Nx =4; Ny = 3; Nz =2
    # Rx = 1; Ry = 2; Rz = 2
    # L = [(2)+Nx*(0),(2)+Nx*(Ny-1)]
    # Vin = 5; Vout =-5
    # A = poissonmatrix(Nx,Ny,Nz,Rx,Ry,Rz,True)
    # V = voltagematrix(A,L,Nx,Ny,Nz,Vin,Vout,True)

    simulate(Nx,Ny,Nz,[[1,1,1],[2,1,1]],[[1,3,1]],5,-5,np.linspace(2,300,100))