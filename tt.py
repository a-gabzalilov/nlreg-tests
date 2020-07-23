import ast
import math

import h5py
import numpy as np


def func(x):
    i = 0
    fu = 0
    while i < 20-1:
        #fu =+ x[i]
        fu += x[i] ** 2 - 10 * math.cos(2 * math.pi * x[i]) + 10
        #fu += x[i]**2
        #fu += 100*(x[i]**2-x[i+1])-(x[i]-1)
        i += 1
    return fu
    #return x[0]**2 + math.pow(10, 6) * fu


arr = np.random.rand(30, 20)
arr2 = np.zeros(30)
for j in range(30):
    arr2[j] = func(arr[j])
arr2.shape = (30, 1)
#print(arr2)
D = 20
j = 0
# arr_mes = []
# while j < 20:
#     arr_mes.append('x'+str(j))
#     j += 1
# arr2_spec = []
# j = 0
# while j < 30:
#     arr2_spec.append('y'+str(j))
#     j += 1
dt = h5py.string_dtype(encoding='ASCII')


arr_mes = np.chararray(20, itemsize=4)
while j < 20:
    arr_mes[j] = 'x'+str(j)
    j += 1
arr2_species = np.chararray(30, itemsize=4)
for j in range(30):
    arr2_species[j] = 'y'+str(j)
# arr_mes = np.array(arr_mes, dtype="V")
# arr2_species = np.array(arr2_species, dtype="V")
#arr2_species.shape = (30, 1)
#print(arr2_spec)
#print (arr2_species)
with h5py.File('random3.h5', 'w') as f:
    dset = f.create_dataset("data", data=arr)
    ddset = f.create_dataset("measurements", (20,), data=arr_mes,  dtype=dt)
    gset = f.create_dataset("response", data=arr2)
    ggset = f.create_dataset("species",  (30,), data=arr2_species, dtype=dt)

    #ddset.astype(dtype=str)
   #ggset.astype(dtype=str)
    # dset.attrs['measurements'] = arr_mes
    # gset.attrs['species'] = arr2_species
#    print(dset[:15])
