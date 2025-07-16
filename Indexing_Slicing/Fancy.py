'''
fancy Indexing : selecting multiple indexing at once 
if we want elements present in alternate indices
arr[[0,2,4,6]] 
'''

import numpy as np 

arr = np.array([10, 20, 30 , 40, 50 , 60 , 70 ,80])

print(arr[[0,2,4,6]]) #[10 30 50 70]