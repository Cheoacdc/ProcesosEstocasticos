import numpy as np
from typing import List


class SistemaDeEcuaciones:
    def __init__(self, matriz: List, costos: List, m: int, metodo: str = '', lado_derecho: List = None):
        self.sistema = matriz
        self.costos = costos
        self.metodo = metodo
        self.coeficientes_variables = None
        self.m = m
        self.solucion = 0
        if lado_derecho is None:
            self.lado_derecho = [0 if i < self.m else 1 for i in range(0, self.m + 1)]
        else:
            self.lado_derecho = lado_derecho

    def resolver_sistema(self):
        if not self.metodo == 'exhaustivo':
            self.coeficientes_variables = np.linalg.solve(self.sistema, self.lado_derecho)
        else:
            self.preparar_sistema_exhaustivo()
            self.coeficientes_variables = np.linalg.solve(self.sistema, self.lado_derecho)
            self.solucion = np.dot(self.coeficientes_variables, self.costos)

    def preparar_sistema_exhaustivo(self):
        self.sistema = np.array(self.sistema).T
        for i in range(0, self.m + 1):
            if i < self.m:
                self.sistema[i][i] = self.sistema[i][i] - 1
            else:
                self.sistema[i] = [1 for x in self.sistema]
