from PMD import PMD
from typing import List, Dict
from Sistema_de_ecuaciones import SistemaDeEcuaciones


class PMDExahustivo(PMD):
    def __init__(self, m: int, k: int, matrices_decision: Dict = None):
        super().__init__(m, k, matrices_decision)
        self.matrices_de_politica = {}

    def generar_politicas(self) -> None:
        self.get_politica([])

    def get_politica(self, nums: List) -> None:
        if len(nums) < self.m + 1:
            e = len(nums)
            for d in range(1, self.k + 1):
                if e not in self.matrices_decision[d].estados:
                    continue
                else:
                    aux_nums = [num for num in nums]
                    aux_nums.append(d)
                    self.get_politica(aux_nums)
        else:
            self.politicas.append(nums)

    def fill_matrices_de_politica(self):
        for i, politica in enumerate(self.politicas):
            self.set_matriz_de_politica(politica, i)

    def set_matriz_de_politica(self, politica: List, num: int = None):
        matriz = []
        costos = []
        for e, k in enumerate(politica):
            mat_k = self.matrices_decision[k]
            index = mat_k.estados.index(e)
            row = [val for val in mat_k.matriz[index]]
            matriz.append(row)
            costo = mat_k.costos[f'c{e}{k}']
            costos.append(costo)
        costo_esperado = self.costo_esperado(matriz, costos)
        self.matrices_de_politica[f'R{num}'] = {'matriz': matriz, 'costo_esperado': costo_esperado, 'politica': politica}

    def costo_esperado(self, matriz: List, costos: List):
        sistema_ecuaciones = SistemaDeEcuaciones(matriz, costos, self.m)
        sistema_ecuaciones.resolver_sistema()
        return sistema_ecuaciones.solucion

    def get_mejor_politica(self) -> Dict:
        mejor = {'costo': ''}
        for i, nombre in enumerate(self.matrices_de_politica):
            if mejor['costo'] == "" or mejor['costo'] > self.matrices_de_politica[nombre]['costo_esperado']:
                mejor['costo'] = self.matrices_de_politica[nombre]['costo_esperado']
                mejor['politica'] = self.matrices_de_politica[nombre]['politica']
                mejor['nombre'] = nombre
        return mejor

    def resolver(self) -> Dict:
        self.generar_politicas()
        self.fill_matrices_de_politica()
        return self.get_mejor_politica()
