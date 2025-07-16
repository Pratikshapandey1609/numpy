'''
.ravel() -> views [means it basically affect the original array]

.flatten() -> copy [ make a copy of array do changes and return
                    it not doing any changes in original array...]
'''

import numpy as np

arr_2d = np.array([[1,2,3] , [4,5,6]])

print("ravel works on original array : ", arr_2d.ravel())
print("flatten works on copy   array : ", arr_2d.flatten())