'''
np.insert(array , index , value , axis= value)

array --> original_array
index --> in which  new value have to insert
value --> in value which have to insert
axis = 0 , row wise insert kerna hai 
       1 , column wise insert kerna h 
'''

import numpy as np

arr = np.array([10 , 20, 30, 40, 50, 60])
new_arr = np.insert(arr , 2, 100)
print(new_arr)