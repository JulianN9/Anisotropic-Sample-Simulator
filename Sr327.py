import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import interpolate
from ResistivityFunctions import userfunction, poly, boltz


def newfunc(T,p1a,p1b,p1c,p2a,p2b,p2c,p3a,p3b,p3c,b1a,b1b,b2a,b2b):
    P1 = poly(T,p1a,p1b,p1c); P2=poly(T,p2a,p2b,p2c); P3=poly(T,p3a,p3b,p3c)
    B1 = boltz(T,b1a,b1b,True); B2 = boltz(T,b2a,b2b,True)
    return P1*B1+(1-B1)*P2*B2+(1-B2)*P3 

# Constants and Variables
def sr327globalsetup():
    global A, L, j_path, d_path
    j_path = '../../Data/Sr327/Julian_Tom_data/'
    d_path = '../../Data/Sr327/Di_Tom_data/'
    A = 1260*(23)**3*(10**(-3))**2
    L = 0.46*10**(-3)

def rhofactor(V,R,A,L):
    # Multiplication factor:
    I = V/R
    mrho = A/(L*I)
    return mrho

# ab Data from Di from cambridge
def loadabdata():
    abpath = '../../Data/Sr327/Sr327_ab_plane_data_Cambridge/uptoroomtemp/sample2/filtered/'
    abheader = ['Temperature','Resistivity']
    abdata = []; ablabels = []
    for file in os.listdir(os.getcwd()+'/'+abpath):
        abdata.append(pd.read_csv(abpath+file, sep=' ', names=abheader))
        ablabels.append(file)
    for data in abdata:
        data[abheader[0]] = data[abheader[0]]/1000
    ablabels = [2,4,5,6,7]
    ablabels, abdata = zip(*sorted(zip(ablabels,abdata)))
    return [abdata, ablabels]

# c-axis Data from Di, 2016 is first sample, 2017 is second sample
def loadcxdata2016():
    cxpath = '../../Data/Sr327/Di_Tom_data/filtered/'
    cxheader = ['Unknown','Resistivity','Temperature']
    cxdata = []; cxlabels = []
    for file in os.listdir(os.getcwd()+'/'+cxpath):
        if '2016' in file:
            cxdata.append(pd.read_csv(cxpath+file, skiprows=23, sep='\t', names=cxheader))
            cxlabels.append(file)
            if 'Sep' in file:
                cxdata[-1]['Resistivity'] = cxdata[-1]['Resistivity']/10
    for data in cxdata:
        data['Resistivity'] = np.abs(data['Resistivity'])
    cxlabels = [4.9,3.3,1.8,2.8,5.8]
    cxlabels, cxdata = zip(*sorted(zip(cxlabels,cxdata)))
    return [cxdata, cxlabels]

def loadcxdata2017():
    cxpath = '../../Data/Sr327/Di_Tom_data/filtered/'
    cxheader = ['Unknown','Resistivity','Temperature','AlsoUnknown']
    cxdata = []; cxlabels = []
    for file in os.listdir(os.getcwd()+'/'+cxpath):
        if '2017' in file:
            cxdata.append(pd.read_csv(cxpath+file, skiprows=23, sep='\t', names=cxheader))
            cxlabels.append(file)
    for data in cxdata:
        data['Resistivity'] = np.abs(data['Resistivity'])
    cxlabels = [3.7,1.6,5.0,4.7,3.1,2.4,4.2]
    cxlabels, cxdata = zip(*sorted(zip(cxlabels,cxdata)))
    return [cxdata, cxlabels]

# Load lock-in data from DATA
def loadoldDATAlockin(path):
    cxheader = ['SignalY','SignalX','Temperature','Unknown']
    cxdata = pd.read_csv(path, skiprows=23, sep='\t', names=cxheader) 
    cxdata['SignalR'] = np.sqrt((cxdata['SignalX'])**2+(cxdata['SignalY'])**2)
    return cxdata

def loadDATAlockin(folder):
    cxpath = folder+'/'
    cxheader = ['Index','Temperature','SignalX','SignalY','Capacitancex','Capacitancey']
    cxtempdata = pd.read_csv(cxpath+'Data.csv', skiprows=1, names=cxheader)
    cxtempdata['SignalR'] = np.sqrt((cxtempdata['SignalX'])**2+(cxtempdata['SignalY'])**2) 
    return cxtempdata

# Load lock-in data from LARA
def loadLARAlockin(folder):
    cxpath = folder+'/'
    cxheader = ['Index','SignalX','SignalY','Time']
    cxdata = pd.read_csv(cxpath+'data_cropped.csv', skiprows=1, names=cxheader) 
    return cxdata

# Combining data from 2023 jerry-rigged system
def combineDATAnLARA(foldertemp,foldersignal):
    cxtemp = loadDATAlockin(foldertemp)
    cxdata = loadLARAlockin(foldersignal)
    header = ['Index','Temperature','SignalX','SignalY','SignalR','Theta']
    cxcombined = pd.DataFrame(columns=header)
    cxcombined['Index'] = cxtemp['Index']
    cxcombined['Temperature'] = cxtemp['Temperature']
    cxcombined['SignalX'] = cxdata['SignalX']
    cxcombined['SignalY'] = cxdata['SignalY']
    cxcombined['SignalR'] = np.sqrt((cxdata['SignalX'])**2+(cxdata['SignalY'])**2)
    cxcombined['Theta'] = np.arctan2(cxdata['SignalY'],cxdata['SignalX'])
    return cxcombined

# Plotting Data
def plotthetaskew(dataframe,theta):
    plt.plot(dataframe['Temperature'],np.cos(theta)*dataframe['SignalX']+np.sin(theta)*dataframe['SignalY'],label=str(theta))

def plotolddataRvT(datalist, save, name = ''):
    data, labels = datalist
    for i in range(len(data)):
        plt.plot(data[i]['Temperature'],data[i]['Resistivity'],label=labels[i])
    # line = np.linspace(0,300)
    # plt.plot(line, 10**(-5)*line**2)
    # plt.ylim(0,0.05)
    plt.xlim(0,300)
    plt.xlabel(r'$T$ (K)',fontsize=16)
    plt.ylabel(r'$\rho(T)$   (a.u.)',fontsize=16)
    plt.legend()
    if save == True:
        plt.savefig('../../Plots/Sr327/'+name)
    plt.show()

def plotdata(fig,ax,data, yname, save = False, name = '', show = True, scale = False, derive = False,original = True):
    for i in range(len(data)):
        if derive == True:
            T = np.linspace(6,291,100)
            Tp = np.linspace(123,291,100)
            R = interpolate.interp1d(data[i][0]['Temperature'],data[i][2]*data[i][0][yname])
            if i==3:
                ax.plot(Tp,np.gradient(np.gradient(R(Tp))),label=data[i][1],linewidth=4,color = data[i][3])
            else:
                ax.plot(T,np.gradient(np.gradient(R(T))),label=data[i][1],linewidth=4,color = data[i][3])
        elif scale == True:
            if (i==0)&(original == True):
                ax.plot(data[i][0]['Temperature'],0.95*data[i][2]*data[i][0][yname]+0.45,label=data[i][1],linewidth=4,color = data[i][3])  
            elif (i==0)&(original == False):
                pass
            elif i==2:
                ax.plot(data[i][0]['Temperature'],data[i][2]*data[i][0][yname]+0.45,label=data[i][1],linewidth=4,color = data[i][3])        
            else:
                ax.plot(data[i][0]['Temperature'],data[i][2]*data[i][0][yname],label=data[i][1],linewidth=4,color = data[i][3])
        else:
            ax.plot(data[i][0]['Temperature'],data[i][2]*data[i][0][yname],label=data[i][1],linewidth=4,color = data[i][3])
    ax.set_xlabel(r'Temperature (K)',fontsize=24)
    ax.set_ylabel(r'Resistivity (m$\Omega$cm)',fontsize=24)
    ax.tick_params(axis='x', labelsize=16)
    ax.tick_params(axis='y', labelsize=16)
    # ax.set_ylabel(r'$\rho(T)$   (a.u.)',fontsize=16)
    ax.set_xlim(0,300)
    ax.legend(fontsize='16',loc='upper left')
    if save == True:
        fig.savefig('../../Plots/Sr327/Measurements/'+name)
    if show == True:
        plt.show()

#Loading specific data sets:
def loadqualifierdata():
    sr327globalsetup()
    cxcombined = combineDATAnLARA(j_path+'Version4Data/coolingdownP1',j_path+'Version4Data/coolingdownP1signal')
    cxcombinedtwo = combineDATAnLARA(j_path+'Version4Data/coolingdownP2',j_path+'Version4Data/coolingdownP2signal')
    cxcombinedfour = combineDATAnLARA(j_path+'Version4Data/heatingupP1',j_path+'Version4Data/heatingupP1signal')
    ndata = pd.concat([cxcombined[(cxcombined['Temperature']>146)&(cxcombined['Temperature']<292)]+0.0000015,cxcombinedfour[(cxcombinedfour['Temperature']>=7)&(cxcombinedfour['Temperature']<=146)].iloc[::-1],cxcombined[cxcombined['Temperature']<7],cxcombinedtwo])
    data = [[loadoldDATAlockin(d_path+'Sr327_Dec_05_2017_1_new.lvm'),'original c-axis',1.6,'b'],[loadDATAlockin(j_path+'Di_sample/isolation_c_cooling_down_2'),'c-axis',1.6,'C1'],[loadDATAlockin(j_path+'Di_sample/isolation_d_coolingdown'),'diagonal',1.6,'green'],[loadDATAlockin(j_path+'Di_sample/isolation_x_coolingdown'),'in-plane',1.6,'red'],[ndata,'long c-axis',100*10**(-3)*rhofactor(5,1200,A,L)/83.35,'purple']]
    return data

if __name__ == "__main__":
    sr327globalsetup()

    data = loadqualifierdata()

    fig = plt.figure(figsize=(10,8))
    ax = fig.add_axes([0.1,0.1,0.85,0.85])
    # plotdata(fig,ax,data,'SignalR',False,'QualifierMeasurementFigure.svg',scale=True)


    # for i in np.linspace(1.76+3*np.pi/2,1.762+3*np.pi/2,10):
    #     plotthetaskew(ndata,i)
    # plt.plot(ndata['Temperature'],ndata['SignalR'], c='blue', label='C-axis')

    # plotthetaskew(cxcombined,np.pi/4)

    # Attempting to fit a function to the new "intrinsic" value:

    # def R_c(T,A,B,C,D,E,F,G,H):  # in m-Ohm-cm (hence factor of )
    #   f = 1.0/(np.exp((T-10)/10.) + 1.)
    #   g = 1.0/(np.exp((T-40)/20.) + 1.)
    #   return (f*(A+E*T*T) + F*T*g*(B-f) + (G+H*T)*(C-g)*(D-f))
    
    def R_c(T,A,B,C,E,F,H,I):  # in m-Ohm-cm (hence factor of )
        f = 1.0/(np.exp((T-E)/F) + 1.)
        return (A+f*(B*pow(T,2+H)) + (C*pow(T,1+I))*(1.-f))

    ndata = data[4][0]
    # T = np.linspace(4.5,291,500)
    Tlow = np.linspace(4.5,50,100)
    Thigh = np.linspace(51,291,100)
    T = np.append(Tlow,Thigh)
    R_i = interpolate.interp1d(ndata['Temperature'],ndata['SignalR']*100*10**(-3)*rhofactor(5,1200,A,L)/83.35)
    R_data = R_i(T)
    plt.scatter(T,R_data,label='interpolation', color='black')

    p1 = [0.022,2,1]; p2 = [0.1,1,0]; p3 = [30*0.0005,1,7.5]
    b1 = [10,10]; b2 = [40,20]

    
    guess = [*p1,*p2,*p3,*b1,*b2]
    bounds = [[0,0,0,0,0,0,0,0,0,1,1,35,1],[1,5,100,1,5,100,1,5,100,30,50,45,50]]
    plt.plot(T,newfunc(T,*guess),label='guess')

# Y best fit:
#     [3.76429264e-02 2.26258146e+00 5.04930673e-38 1.75885465e-01
#  8.58953358e-01 3.50487700e-38 6.65212472e-02 7.64536696e-01
#  6.73322021e+00 1.00000211e+00 7.71994651e+00 3.50000035e+01
#  1.15517153e+01]


    popt, pcov = curve_fit(newfunc,T,R_data, p0=guess, bounds=bounds)
    plt.plot(ndata['Temperature'],newfunc(ndata['Temperature'],*popt),label='fit')
    p1 = popt[0:3]
    p2 = popt[3:6]
    p3 = popt[6:9]
    b1 = popt[9:11]
    b2 = popt[11:]
    print(p1)
    print(p2)
    print(p3)
    print(b1)
    print(b2)
    plt.legend()
    plt.show()