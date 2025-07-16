## Aggreation functions gives summary of  your data 
import numpy as np

arr = np.array([10,20,30,40,50,60])

print("Sum of array is : " , np.sum(arr))
print("variance of array is : " , np.var(arr))
print("product of array is : " , np.prod(arr))
print("minimum of array is : " , np.min(arr))
print("maximum of array is : " , np.max(arr))
print("median of array is : " , np.median(arr))
print("Standard deviation of array is : ", np.std(arr))
print("Calculate nth percentile  of array is : ", np.percentile(arr))
print("any  of array is : " , np.any(arr))
print("all of array is : " , np.all(arr))