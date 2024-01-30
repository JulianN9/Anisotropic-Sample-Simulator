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

def plotLeads(ax,Ix,Iy,Iz,Ox,Oy,Oz,c,m):
  ax.scatter([Ix-1],[Iz-1],[Iy-1],s=50,c=c,marker=m)
  ax.scatter([Ox-1],[Oz-1],[Oy-1],s=50,c=c,marker=m)

if __name__ == "__main__":
  Nx = 24; Ny =12; Nz = 2
  fig = plt.figure()
  ax = fig.add_subplot(projection='3d')
  plotMatrix(ax,Nx,Ny,Nz)
  plt.show()