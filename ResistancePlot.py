
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def RVTaxes(ax,ur = False):
    ax.set_xlabel(r'Temperature  (K)',fontsize=16)
    ax.set_ylabel(r'$\rho(T)$  (a.u.)',fontsize=16)
    ax.set_yticks([])
    ax.legend(loc='upper right',prop={'size': 10})
    ax.tick_params(axis='x', labelsize=16)
    if ur == False:
        ax.set_xlim(0,300)
        ax.legend(fontsize='16')

def ResistancePlot(ax,df,IPx,IPy,OPx,OPy,CheckX,CheckY):
    ax.clear()

    inputpin = "V["+str(IPx)+","+str(IPy)+"]" 
    outputpin = "V["+str(OPx)+","+str(OPy)+"]"

    lengthscale = np.sqrt((IPx-OPx)**2+(IPy-OPy)**2)

    if CheckX == True:
        ax.scatter(df["T"],df["rx"],color='red',s=4.0,label= r'$\rho_{ab}$(T)')
    if CheckY == True:
        ax.scatter(df["T"],df["ry"],color='blue',s=4.0,label= r'$\rho_c$(T)')
    ax.scatter(df["T"],(df[outputpin]-df[inputpin])/df["I"],color='black',s=8.0,marker='v',label='Input')
    # ax.scatter(df["T"],2.65*(df[outputpin]-df[inputpin]),color='black',s=8.0,marker='v',label='Input')
    
    # plt.show()
    return 0