from typing import Dict, List
from Metodos.Mejoramiento_Politicas import MejoramientoPoliticas
from Classes.Sistema_de_ecuaciones import SistemaDeEcuaciones
from utils.Functions import get_alpha


class MejoramientoPoliticasDescuento(MejoramientoPoliticas):
    def __init__(self, m: int, k: int, matrices_decision: Dict = None):
        super().__init__(m, k, matrices_decision)
        self.variables.append({'name': f'V{self.m}', 'value': 0})
        self.alpha = get_alpha()

    def get_row(self, i: int, k: int = None, initial: List = None) -> List:
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
