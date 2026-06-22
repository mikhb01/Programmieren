import numpy as np

# x = np.array([[1, 0, 1], [2, 2, 2]])
# y = x[0:2, 2]
# print(y)

a = np.array([[1,0], [0,1]])
b = np.array([[2,2], [2, 2]])
c = np.dot(a, b)
print(c)