import numpy as np


a= np.zeros(3)
# print(a)
# b= np.zeros((2,3))
# print(b)
c = np.zeros((2,3,3,3))
print(c)

# any other value
d = np.full((2,2),4)
print(d)
# random numner

e = np.random.rand(4,2)
print (e)

f = np.ones((5,5))
z = np.zeros((3,3))
f[1:4,1:4]  = z

print(f)
print(z)