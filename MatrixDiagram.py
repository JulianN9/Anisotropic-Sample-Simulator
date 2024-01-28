import argparse
from ast import Not
from itertools import product, repeat
from multiprocessing import Pool
from timeit import repeat
from math import exp, ceil
from turtle import color
import numpy as np
import matplotlib.pyplot as plt 

def plotMatrix(ax,Nx,Ny,Ix,Iy,Ox,Oy):
  X = []; Y = []; pX = []; pY = []; rx = []; rxY =[]; ryX = []; ry =[]
  for i in range(1,Nx+1):
    for j in range(1,Ny+1):
      X.append(i)
      Y.append(j)
  for i in range(1,Ny+1):
    ax.plot([1,Nx],[i,i],color='peru')
  for i in range(1,Nx+1):
    ax.plot([i,i],[1,Ny],color='brown')
  ax.plot(X,Y,'ko')
  # ax.plot([I_in,Nx+1-I_in],[1,1],'ro')
  # ax.plot([I_out,Nx+1-I_out],[Ny,Ny],'bo')
  ax.plot(pX,pY, 'o',color='0.8')
  # for i in range(0,Ny-2):
  #   ax.plot([1,Nx],[i+2,i+2],'o',color='purple')
  ax.plot([Ix,Ox],[Iy,Oy],'o',color='purple')

  #ax.axes.xaxis.set_visible(False)
  # ax.axes.set_xlabel('a-b plane',fontsize=24)
  # ax.axes.set_ylabel('c-axis',fontsize=24)
  # ax.axes.set_ylabel('a-b plane',fontsize=24)
  # ax.axes.set_xlabel('c-axis',fontsize=24)
  ax.set_yticks([])
  ax.spines['top'].set_visible(False)
  ax.spines['right'].set_visible(False)
  ax.spines['bottom'].set_visible(False)
  ax.spines['left'].set_visible(False)
  xrange = []
  for i in range(1,Nx+1):
    if (i % 2) and (i<ceil(Nx/2)):
      xrange.append(i)
    elif not (i % 2) and (i>ceil(Nx/2)):
      xrange.append(i)
  ax.set_xticks([])
  #ax.axes.yaxis.set_visible(False)0
  # plt.show()


# Nx = 12
# Ny = 4
# I_in = 3
# I_out = 4
# T = 300

# fig = plt.figure(figsize=(6,4))
# ax = fig.add_axes([0.2,0.2,0.7,0.6])

# plotMatrix(ax,Nx,Ny,I_in,1,I_out,Ny)