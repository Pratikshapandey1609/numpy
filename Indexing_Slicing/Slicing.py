'''
Extracting  the  subsat of array / range of array

arr[start : stop : step]
'''

import numpy as np 

arr = np.array([10, 20, 30 , 40, 50 , 60])
print(arr[2:5])  # [30 40 50] accessing subsat of array
print(arr[:4])   # [10 20 30 40]
print(arr[::2])  # [10 30 50]
print(arr[:-2])