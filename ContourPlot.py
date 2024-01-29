
from email.mime import image
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from math import ceil
from pathlib import Path
import argparse
# import imageio.v2 as imageio
import os

fontsize = 24

def f(data,X,Y,zp,T):
    Z = []
    z = []
    for y in Y:
        z = []
        for x in X:
            name = "V["+str(x)+","+str(y)+","+str(zp)+"]"
            z.append(data[name][T])
        Z.append(z)
    return Z

def RVTaxes(ax,ur = False):
    ax.set_xlabel(r'Temperature  (K)',fontsize=fontsize)
    ax.set_ylabel(r'$\rho(T)$  (a.u.)',fontsize=fontsize)
    ax.set_yticks([])
    ax.legend(loc='upper right',prop={'size': 10})
    ax.tick_params(axis='x', labelsize=16)
    if ur == False:
        ax.set_xlim(0,300)
        ax.legend(fontsize='16')

def contouraxes(ax,heatmap,Nx,Ny,axtitle=1,gift = False,mixed = 'none'):
    ax.set_xticks([1,ceil(Nx/2),Nx])
    ax.set_yticks([1,ceil(Ny/2),Ny])
    if (gift == False)&(mixed == 'none'):
        ax.tick_params(axis='x', labelsize=fontsize)
        ax.tick_params(axis='y', labelsize=fontsize)
        if axtitle == True:
            ax.set_xlabel('a-b plane',fontsize=fontsize)
            ax.set_ylabel('c-axis',fontsize=fontsize)
        cbr = plt.colorbar(heatmap,ax=ax)
        cbr.set_label('Voltage (V)', rotation=270,fontsize=fontsize)
        cbr.ax.get_yaxis().set_ticks([-0.5,0,0.5])
        cbr.ax.tick_params(labelsize=fontsize)
        cbr.ax.set_yticklabels(['-0.5','0','0.5'])
    # elif(gift==True):
    #     ax.set_xticks([])
    #     ax.set_yticks([])
    #     ax.tick_params(axis='x')
    #     ax.tick_params(axis='y')
    #     if axtitle > 0:
    #         ax.set_xlabel('a-b plane')
    #         ax.set_ylabel('c-axis')
        # cbr = plt.colorbar(heatmap,ax=ax)
        # cbr.set_label('Voltage (V)', rotation=270)
        # cbr.ax.get_yaxis().set_ticks([-0.5,0,0.5])
        # cbr.ax.set_yticklabels(['-0.5','0','0.5'])
    else:
        if axtitle == 2:
            ax.set_ylabel('a-b plane')
            ax.set_xlabel('c-axis')
        elif axtitle > 0:
            ax.set_xlabel('a-b plane')
            ax.set_ylabel('c-axis')
        if(mixed == 'top'):
            ax.set_xticks([])
            ax.set_yticks([])
        if(mixed == 'left'):
            ax.set_xticks([])
            if (gift==False):
                ax.set_ylabel(r'$\bf{300 K}$' '\n' 'c-axis')
        if(mixed == 'corner'):
            if (gift==False):
                ax.set_ylabel(r'$\bf{2 K}$' '\n' 'c-axis')
        if(mixed == 'bottom'):
            ax.set_yticks([])

def contourfit(ax,df,Nx,Ny,zp,T):
    x = []; y = []
    for i in range(1,Nx+1):
        x.append(i)
    for j in range(1,Ny+1):
        y.append(j)
    X, Y = np.meshgrid(x,y)
    Z = f(df,x,y,zp,T)
    # fig = plt.figure(figsize=(6,4))
    # ax = fig.add_axes([0.2,0.2,0.7,0.6])
    heatmap = ax.contourf(X,Y, Z,cmap='RdGy')

    # contouraxes(ax,heatmap,Nx,Ny)

    # plt.show()
    return 0