import numpy as np
import pickle
from main import flags

##################################### write
arr = np.zeros((flags.grid_size + 1, flags.grid_size + 1))

roads = [0, 25, 50, 75, 100]
# change this array roads to vary the position of rods in the map

for i in range(len(roads)):
	ind = roads[i]
	arr[ind, :] = 1
	arr[:, ind] = 1

with open('map', 'wb') as fp:
    pickle.dump(arr, fp)

####################################### read 

# with open ('map', 'rb') as fp:
#     itemlist = pickle.load(fp)

# print (itemlist)

#######################################
