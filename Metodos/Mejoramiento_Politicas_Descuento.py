from typing import Dict, List
from Metodos.Mejoramiento_Politicas import MejoramientoPoliticas
from Classes.Sistema_de_ecuaciones import SistemaDeEcuaciones
from utils.Functions import get_alpha
import numpy as np


class MejoramientoPoliticasDescuento(MejoramientoPoliticas):
    def __init__(self, m: int, k: int, matrices_decision: Dict = None, tipo: str = 'min'):
        super().__init__(m, k, matrices_decision, tipo)
        self.variables.append({'name': f'V{self.m}', 'value': 0})
        self.alpha = get_alpha()

    def get_row(self, i: int, k: int = None, initial: List = None, intact: bool = False) -> List:
        if initial is None:
            result = []
        else:
            result = [val for val in initial]
        if not k:
            k = self.politica[i]

        e = self.matrices_decision[k].estados.index(i)
        for j in range(0, self.m + 1):
            p = self.matrices_decision[k].matriz[e][j]
            result.append(-p*self.alpha)
        if intact:
            return result
        if initial is not None:
            result[i + len(initial)] += 1
        else:
            result[i] += 1
        return result

    def resolver_matriz(self):
        lado_derecho = self.get_lado_derecho()
        costos = [self.costos[costo] for costo in self.costos]
        sistema = SistemaDeEcuaciones(self.matriz_politica, costos, self.m, lado_derecho=lado_derecho)
        sistema.resolver_sistema()
        coeficientes = sistema.coeficientes_variables
        for i, var in enumerate(self.variables):
            var['value'] = coeficientes[i]

    def comparacion_politicas(self, i: int) -> int:
        mejor = {'k': 0, 'val': None}
        posibles_k = self.posibles_k_para_e(i)
        if len(posibles_k) == 1:
            return posibles_k[0]
        else:
            for k in posibles_k:
                row = self.get_row(i, k, [], intact=True)
                coeficientes = [var['value'] for var in self.variables]
                val = np.dot(row, coeficientes) - self.costos[f'c{i}{k}']
                if mejor['val'] is None or mejor['val'] < val:
                    mejor = {'k': k, 'val': val}
        return mejor['k']
