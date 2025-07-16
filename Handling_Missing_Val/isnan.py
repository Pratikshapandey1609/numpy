# np.isnan(array)

import numpy as np

arr = np.array([1,2,3,np.nan  , 5 , 6 , 7 , np.nan, 8])

print(np.isnan(arr))

'''
Q- can we compare nan value
A- No we can't compare nan to nan

like print(np.nan == np.nan)
'''