'''
Splitting arrays in NumPy is the reverse operation of joining (concatenation). 
It involves dividing a single array into multiple smaller sub-arrays. 
This is a crucial operation for tasks like processing data in chunks, 
distributing data for parallel computation, or separating features from target variables in machine learning datasets.

np.split() --- equal 
np.hsplit() ---  horizontal parts 
np.vsplit() ---  vertical parts

'''

import numpy as np

arr = np.array([10,20,30,40,50,60])
print(np.split(arr , 3))

