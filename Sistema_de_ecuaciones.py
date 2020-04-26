import numpy as np
from typing import List


class SistemaDeEcuaciones:
    def __init__(self, matriz: List, costos: List, m: int):
        self.sistema = np.array(matriz).T
        self.costos = costos
        self.m = m
        self.solucion = 0
        self.lado_derecho = [0 if i < self.m else 1 for i in range(0, self.m + 1)]

    def resolver_sistema(self):
        self.preparar_sistema()
        coeficientes = np.linalg.solve(self.sistema, self.lado_derecho)
        self.solucion = np.dot(coeficientes, self.costos)

    def preparar_sistema(self):
        for i in range(0, self.m + 1):
            if i < self.m:
                self.sistema[i][i] = self.sistema[i][i] - 1
            else:
                self.sistema[i] = [1 for x in self.sistema]
