import itertools as it

Nx = 5
Ny = 3
Nz = 2
N = Nx*Ny*Nz
L = it.product(*[range(Nx),range(Ny),range(Nz)])
for i,j,k in L:
    print(str(i)+' and '+str(j)+' and '+str(k))
# print(L)