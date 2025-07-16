'''
Stacking in NumPy refers to the process of joining multiple arrays along a new dimension or axis. 
This differs from concatenation, which combines arrays along an existing axis. Stacking results 
in a new array with a higher dimensionality than the input array

vertically 
horizontally 

vstack() row wiese vertically
hstack() column wise horizontally 

'''

import numpy as np


import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print(np.vstack((arr1 , arr2))) # vertically  -- two_D
print(np.hstack((arr1 , arr2))) # horizontally  -- one_D

