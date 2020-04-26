import numpy as np
m = np.array([[.4, .6],[.5,.5]])
m = m.T
print(m)
m[0][0] = m[0][0] - 1
m[len(m) - 1] = [1 for x in m]
print(m)
coeficientes = np.linalg.solve(m, [0, 1])
solucion = np.dot(coeficientes, [60, 0])
print(solucion)