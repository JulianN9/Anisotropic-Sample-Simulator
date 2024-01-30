import argparse
from ast import Not
from itertools import product, repeat
from multiprocessing import Pool
from timeit import repeat
from math import exp, ceil
from turtle import color
import numpy as np
import matplotlib.pyplot as plt 


def plotMatrix(ax,Nx,Ny,Nz):
  X = []; Y = []; Z= []
  for i in range(Nx):
    for j in range(Ny):
      for k in range(Nz):
        X.append(i)
        Y.append(j)
        Z.append(k)
  for j in range(Nz):
    for i in range(Ny):
      ax.plot([0,Nx-1],[j,j],[i,i],color='peru')
    for i in range(Nx):
      ax.plot([i,i],[j,j],[0,Ny-1],color='brown')
  for i in range(Nx):
    for j in range(Ny):
      ax.plot([i,i],[0,Nz-1],[j,j],color='black')
  ax.scatter(X,Z,Y)
  
  ax.set_aspect('equal')
  ax.set_yticks([])
  ax.set_xticks([])
  ax.set_zticks([])
  ax.axis('off')

Nx = 24; Ny =12; Nz = 2
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
plotMatrix(ax,Nx,Ny,Nz)
plt.show()