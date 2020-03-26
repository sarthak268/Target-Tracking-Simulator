import numpy as np
import pickle

##################################### write
arr = np.zeros((102, 102))

roads = [0, 25, 50, 75, 100]

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
