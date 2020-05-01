from typing import Dict, List
from Classes.PMD import PMD
from utils.Functions import get_alpha, get_param, check_index
import numpy as np


class AproximacionesSucesivas(PMD):
    def __init__(self, m: int, k: int, matrices_decision: Dict = None):
        super().__init__(m, k, matrices_decision)
        self.matriz_de_coeficientes = []
        self.variables = [{'name': f'V{i}', 'value': 0} for i in range(0, self.m + 1)]
        self.get_costos()
        self.politica = []
        self.matriz_politica = None
        self.alpha = get_alpha()
        self.epsilon = get_param('epsilon (error tolerado)', 'float')
        self.n = get_param('n (número de iteraciones)')

    def calcular_variables(self, iteracion: int, coeficientes: List):
        variables = self.variables
        if iteracion == 1:
            for i in range(0, self.m + 1):
                variables[i]['value'], k = self.get_min_cost(i)
                self.politica.append(k)
        else:
            for i in range(0, self.m + 1):
                matriz = self.get_matriz_de_i(i)
                self.set_v(i, coeficientes, matriz)

    def get_matriz_de_i(self, i: int) -> np.ndarray:
        matriz = []
        for k in range(1, self.k + 1):
            row = self.get_row(i, k)
            if row:
                matriz.append(row)
        return np.array(matriz).T

    def get_row(self, i: int, k: int = None) -> List:
        if not k:
            k = self.politica[i]
        result = []
        e = check_index(i, self.matrices_decision[k].estados)
        if e is not None:
            for j in range(0, self.m + 1):
                p = self.matrices_decision[k].matriz[e][j]
                result.append(p*self.alpha)
        return result

    def set_v(self, i: int, coeficientes: List, matriz: np.ndarray) -> None:
        variables = self.variables
        coeficientes = np.array(coeficientes)
        suma = np.matmul(coeficientes, matriz)
        arr = np.add(suma, self.arr_costos(i))
        minimo = None
        politica = None
        for k, val in enumerate(arr):
            if minimo is None or val < minimo:
                minimo = val
                posibles_k = self.posibles_k_para_e(i)
                politica = posibles_k[k]
        variables[i]['value'] = minimo
        self.politica[i] = politica

    def get_min_cost(self, i: int) -> tuple:
        minimo = None
        politica = None
        for costo in self.costos:
            if int(costo[1]) == i and (minimo is None or self.costos[costo] < minimo):
                minimo = self.costos[costo]
                politica = int(costo[2])
        return minimo, politica

    def arr_costos(self, i: int) -> np.ndarray:
        costos = []
        for k in self.posibles_k_para_e(i):
            costos.append(self.costos[f'c{i}{k}'])
        return np.array(costos)

    def resolver(self):
        for i in range(1, self.n + 1):
            last_vs = [self.variables[i]['value'] for i in range(0, len(self.variables))]
            self.calcular_variables(i, last_vs)
            self.matriz_politica = self.get_matriz_de_politica(self.politica)

            print(f'\nDespués de la iteración {i}:')
            print(f'\tPolítica: {self.politica}')
            costo = self.matriz_politica["costo_esperado"]
            print(f'\tCosto esperado: {costo}')

            new_vs = [self.variables[i]['value'] for i in range(0, len(self.variables))]
            diffs = np.subtract(new_vs, last_vs)
            diffs = [abs(dif) for dif in diffs]
            if max(diffs) < self.epsilon:
                print('Se superó el error mínimo esprado.')
                break
        return {'costo': costo, 'politica': self.politica}
