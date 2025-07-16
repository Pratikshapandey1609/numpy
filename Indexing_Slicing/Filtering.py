'''
filter the element based  on certain condition 
if condition is true return true  otherwise return false

'''
import numpy as np 

arr = np.array([10, 20, 30 , 40, 50 , 60 , 70 ,80])


print(arr[arr <= 30])
print(arr[arr > 30])