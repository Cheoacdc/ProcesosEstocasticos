from Classes.PMD import PMD
from typing import List, Dict
from utils.Functions import check_index
import numpy as np
from Classes.PPL import PPL


class ProgLineal(PMD):
    def __init__(self, m: int, k: int, matrices_decision: Dict = None):
        super().__init__(m, k, matrices_decision)
        self.matriz_de_coeficientes = []
        self.variables = []
        self.get_costos()
        self.set_variables()

    def set_variables(self):
        for costo in self.costos:
            self.variables.append(f'y{costo[-2:]}')

    def fill_matriz_coeficientes(self):
        for j in range(0, self.m):
            self.generate_row_coeficientes(j)
        last_row = [1 for var in self.variables]
        self.matriz_de_coeficientes.append(last_row)

    def generate_row_coeficientes(self, j: int):
        suma_y = self.suma_y(j)
        doble_suma = self.doble_suma(j)
        row = np.subtract(suma_y, doble_suma)
        self.matriz_de_coeficientes.append(row)

    def suma_y(self, j: int) -> List:
        result = [0 for var in self.variables]
        for k in range(1, self.k + 1):
            y = f'y{j}{k}'
            index = check_index(y, self.variables)
            if index is not None:
                result[index] = 1
        return result

    def doble_suma(self, j: int) -> List:
        result = [0 for y in self.variables]
        for i in range(0, self.m + 1):
            for k in range(1, self.k + 1):
                y = f'y{i}{k}'
                index = check_index(y, self.variables)
                if index is not None:
                    e = self.matrices_decision[k].estados.index(i)
                    p = self.matrices_decision[k].matriz[e][j]
                    result[index] = p
        return result

    def minimizar(self):
        self.fill_matriz_coeficientes()
        costos = [self.costos[costo] for costo in self.costos]
        ppl = PPL(costos, self.matriz_de_coeficientes)
        return ppl.solve()

    def get_politica(self, sol) -> List:
        print('Al optimizar, se obtiene: ')
        politica = [None for x in range(0, self.m + 1)]
        for i, val in enumerate(sol.x):
            if val > .0001:
                y = self.variables[i]
                print(f'\t{y} = {val}')
                e = int(y[1])
                k = int(y[2])
                politica[e] = k
        return politica

    def resolver(self):
        sol = self.minimizar()
        if sol.success:

            politica = self.get_politica(sol)
            return {'costo': sol.fun, 'politica': politica}
        else:
            return {'costo': sol.message, 'politica': 'Hubo un error en el proceso de optimización'}
