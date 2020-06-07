from Classes.PMD import PMD
from typing import List, Dict
from utils.Functions import check_int, check_index
from Classes.Sistema_de_ecuaciones import SistemaDeEcuaciones
import numpy as np


class MejoramientoPoliticas(PMD):
    def __init__(self, m: int, k: int, matrices_decision: Dict = None):
        super().__init__(m, k, matrices_decision)
        self.matriz_de_coeficientes = []
        self.variables = [{'name': f'V{i}', 'value': 0} for i in range(0, self.m)]
        self.get_costos()
        self.politica = []
        self.matriz_politica = []

    def get_politica_arbitraria(self):
        print('Ingrese la política arbitraria con la que desea comenzar el procedimiento.')
        while len(self.politica) <= self.m:
            self.politica.append(self.get_k(len(self.politica)))

    def get_k(self, e: int):
        ks = self.posibles_k_para_e(e)
        while True:
            k = check_int(input(f'Ingrese k para el estado {e}: '))
            if (k is not None and (k in ks) 
            and check_index(e, self.matrices_decision[k].estados) is not None):
                break
            print('Opción inválida, intente de nuevo...')
            print(f'Las posibles k para el estado {e} son: ', ks)
        return k

    def set_matriz(self):
        for i in range(0, self.m + 1):
            self.matriz_politica.append(self.get_row(i))

    def get_row(self, i: int, k: int = None, initial: List = None) -> List:
        if initial is None:
            result = [1]
        else:
            result = [val for val in initial]
        if not k:
            k = self.politica[i]

        e = self.matrices_decision[k].estados.index(i)
        for j in range(0, self.m):
            p = self.matrices_decision[k].matriz[e][j]
            result.append(-p)

        if initial is not None:
            if not i == self.m:
                result[i + len(initial)] += 1
        else:
            if not i == self.m:
                result[i + 1] += 1
        return result

    def resolver_matriz(self):
        lado_derecho = self.get_lado_derecho()
        costos = [self.costos[costo] for costo in self.costos]
        sistema = SistemaDeEcuaciones(self.matriz_politica, costos, self.m, lado_derecho=lado_derecho)
        sistema.resolver_sistema()
        coeficientes = sistema.coeficientes_variables
        for i, var in enumerate(self.variables):
            var['value'] = coeficientes[i + 1]

    def get_lado_derecho(self) -> List:
        lado_derecho = []
        for i, k in enumerate(self.politica):
            costo = self.matrices_decision[k].costos[f'c{i}{k}']
            lado_derecho.append(costo)
        return lado_derecho

    def mejoramiento_politicas(self):
        n_politica = []
        for i in range(0, self.m + 1):
            n_politica.append(self.comparacion_politicas(i))
        return n_politica

    def comparacion_politicas(self, i: int) -> int:
        mejor = {'k': 0, 'val': None}
        posibles_k = self.posibles_k_para_e(i)
        if len(posibles_k) == 1:
            return posibles_k[0]
        else:
            for k in posibles_k:
                row = self.get_row(i, k, [])
                coeficientes = [var['value'] for var in self.variables]
                val = np.dot(row, coeficientes) - self.costos[f'c{i}{k}']
                if mejor['val'] is None or mejor['val'] < val:
                    mejor = {'k': k, 'val': val}
        return mejor['k']

    def resolver(self):
        self.get_politica_arbitraria()
        self.set_matriz()
        while True:
            self.resolver_matriz()
            n_politica = self.mejoramiento_politicas()
            if n_politica == self.politica:
                break
            else:
                self.politica = n_politica
                print(f'\tLa nueva politica es {self.politica}')
        costo = self.evaluar_politica(self.politica)['costo']
        return {'costo': costo, 'politica': self.politica}
