# if we wanto to convert the existing type into new type 
# in this case we can us [astype]

import numpy as np

arr = np.array([1.2, 2.5, 3.4 , 4.3])
int_arr = arr.astype(int)

print(arr.dtype)
print(int_arr)
print(int_arr.dtype)