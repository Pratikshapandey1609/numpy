'''
np.delete(array , index , axis = none)
'''

import numpy as np

arr = np.array([10,20,30,40,50,60])
print(arr)

new_arr = np.delete(arr , 2 , axis = None)
print(new_arr) #[10 20 40 50 60]


