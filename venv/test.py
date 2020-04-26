import numpy as np
m = np.array([[1,2,3],[2,3,4]])
print(m)
a = np.linalg.solve([[1,2,3],[1,0,0],[0,2,2]], [1,1,1])
print(a)