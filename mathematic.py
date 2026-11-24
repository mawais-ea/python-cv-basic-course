import numpy as np
a = np.array([1,2,3,4,5])
b = a+2
print(b)
#  linear algebra

a = np.full((2,3),1)
b = np.full((3,2),3)
print(a,b)
c= np.matmul(a,b)
print (c)

bef = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print (bef)
reshap = bef.reshape((3,4))
print(reshap)

# vertical stacking
ac =np.array([1,2,3,4,5])
bc =np.array([6,7,8,9,10])

cc = np.vstack([ac,bc])
print(cc)