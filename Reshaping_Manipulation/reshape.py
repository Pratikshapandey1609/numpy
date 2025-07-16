'''
reshape (rows , columns) specify new shape 
if dimension matches
'''

import numpy as np

arr = np.array([1,2,3,4,5,6])
reshapes_arr = arr.reshape(2,3)

print("Reshaped Array is :" , reshapes_arr)