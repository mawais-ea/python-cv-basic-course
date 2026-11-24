import numpy as np


a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

# get a specific element[r,c]
print(a[1,5])
# get a specific element row
print(a[0,3])
# get a specific element column
print(a[:,3])
# get a more fancy 
print(a[0,1:6:2])


b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)
print(b[0,1,1])